# Generated by Django 2.0.9 on 2020-03-20 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pharma', '0003_invitation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time on which the object was created.', verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time on which the object last Modified', verbose_name='Modified at')),
                ('avaliable_seats', models.PositiveSmallIntegerField(default=1)),
                ('comments', models.TextField(blank=True)),
                ('departure_location', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('arrival_location', models.CharField(max_length=255)),
                ('arrival_date', models.DateTimeField()),
                ('rating', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Used for diabling the ride or marking it as finished', verbose_name='active status')),
                ('offered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('offered_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pharma.Circle')),
                ('passengers', models.ManyToManyField(related_name='passengers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': ('created',),
                'abstract': False,
            },
        ),
    ]
