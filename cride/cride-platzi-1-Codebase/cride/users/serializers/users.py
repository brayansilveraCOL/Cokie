from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from cride.users.models import User, Profile
from django.core.validators import RegexValidator
from datetime import timedelta
from cride.taskapp.tasks import send_confirmation_email
import jwt
from django.conf import settings
from cride.users.serializers.profiles import ProfileModelSerializer

class UserModelSerializer(serializers.ModelSerializer):
    profile = ProfileModelSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'profile']
        
class UserSignupSerializer(serializers.Serializer):
    #User signup Serializer
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
         validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
        )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="No admitido"
    )
    phone = serializers.CharField(validators=[phone_regex])
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Not mach")
        password_validation.validate_password(passwd)
        return data
    
    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False, is_client=True) #Cambios clase 35 solo is client
        Profile.objects.create(user=user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user

    



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet :(')
        self.context['user'] = user
        return data
    def create(self, data):
        #Generar Token
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class AccountVerificationSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, data):
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Link expiro.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token1')
        if payload['type'] !=  'email_confirmation':
            raise serializers.ValidationError('Invalid token2')
        self.context['payload'] = payload
        return data
    def save(self):
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified =True
        user.save()
