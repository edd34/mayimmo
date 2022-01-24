from rest_framework import serializers

from components.address.serializers import AddressSerializer
from components.property.models import Property
from components.users.serializers import UserSerializer
from components.helpers.POI.POI import POI


class PropertySerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    owner = UserSerializer()

    class Meta:
        model = Property
        fields = "__all__"

    def create(self, validated_data):
        return Property.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        x_lon = representation['address']['longitude']
        y_lat = representation['address']['latitude']

        poi = POI()
        res = poi.get_close_node(float(500), float(y_lat), float(x_lon))

        representation['POI'] = poi.clean_output_format(res)['result']
        return representation
