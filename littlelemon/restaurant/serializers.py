from rest_framework import serializers
from . import models

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = '__all__'
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'
        
class TestMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ['title', 'price']