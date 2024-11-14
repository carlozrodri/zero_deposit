from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Property
        fields = ['id', 'address', 'postcode', 'city', 'rooms', 'created_by']
