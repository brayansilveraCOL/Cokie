
#Rides Serializer

from rest_framework import serializers
from cride.pharma.models.membership import Membership
from cride.rides.models.rides import Ride
from datetime import timedelta
from django.utils import timezone

class RideModelSerializer(serializers.ModelSerializer):
    """Ride Model Serializer"""
    class Meta:
        """Meta Class"""
        model = Ride
        fields = '__all__'
        read_only_fields = [
            'offered_in',
            'offered_by'
            'rating'
            
        ]

class CreateRideSerializer(serializers.ModelSerializer):
    #Create ride Serializer
    
    offered_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    avaliable_seats = serializers.IntegerField(min_value=1, max_value=15)
    class Meta:
        model = Ride
        exclude = ['offered_in','passengers', 'rating', 'is_active']
    
    def validate_departure_date(self, data):
        """Verify date is not in the past"""

        min_date = timezone.now() + timedelta(minutes=10)
        if data < min_date:
            raise serializers.ValidationError(
                'Departure time must be at least passing the next 20 minuts window.'
            )   
        return data
    
    def validate(self, data):
        
        """Validate
        Verify that the person who offers the ride is member
        and also the same user making the request
        """
        
        if self.context['request'].user != data['offered_by']:
            raise serializers.ValidationError('Rides offered on  behalf of others are not allowed')
        user = data['offered_by']
        circle = self.context['circle']
        try:
           membership =  Membership.objects.get(
                user=user, 
                circle=circle, 
                is_active=True)
        except Membership.DoesNotExist:
            raise serializers.ValidationError('User us not an active member of the circle')
        if data['arrival_date'] <= data['departure_date']:
            #import pdb; pdb.set_trace()
            raise serializers.ValidationError('Departure date must happen after arrival date.')
        self.context['membership'] = membership
        return data
    
    def create(self, data):
        #Create ride and update stats

        circle = self.context['circle']
        ride = Ride.objects.create(**data, offered_in=circle)
        

        #Circle
        circle.rides_offered +=1
        circle.save()

        #Membership
        membership = self.context['membership']
        membership.rides_offered +=1
        membership.save()

        #Profile
        profile = data['offered_by'].profile
        profile.rides_offered += 1
        profile.save()

        return ride


