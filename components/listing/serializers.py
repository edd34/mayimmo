from rest_framework import serializers
from components.listing.models import Listing
from components.property.models import Property


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
