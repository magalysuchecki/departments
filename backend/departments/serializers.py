from rest_framework import serializers 
from departments.models import department 
 
 
class DepartmentSerializer(serializers.Serializer): 
    description = serializers.CharField()
    rooms = serializers.CharField()
    monthly_amount = serializers.CharField()
    guarantee = serializers.IntegerField()
    floor = serializers.IntegerField()
    bathroom = serializers.IntegerField()
    photos = serializers.CharField()
    state = serializers.CharField()
    pets = serializers.BooleanField()
    kids = serializers.BooleanField()
    parking = serializers.BooleanField()
    created_at = serializers.DateTimeField(auto_now=True)