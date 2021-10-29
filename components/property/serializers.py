from rest_framework import serializers
from components.property.models import Property
from components.address.serializers import AddressSerializer
from components.users.serializers import UserSerializer


class PropertySerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    owner = UserSerializer()

    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        return Property.objects.create(**validated_data)
