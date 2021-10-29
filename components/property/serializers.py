from rest_framework import serializers
from components.property.models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        return Property.objects.create(**validated_data)
