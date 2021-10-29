from rest_framework import serializers
from components.property.models import Property
from components.address.serializers import AddressSerializer


class PropertySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        return Property.objects.create(**validated_data)
