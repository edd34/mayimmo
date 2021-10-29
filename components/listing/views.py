from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from components.listing.serializers import ListingSerializer
from components.property.serializers import PropertySerializer
from components.listing.models import Listing
from components.property.models import Property


@api_view(['POST', 'OPTIONS'])
def create_listing_create_property(request):
    data = JSONParser().parse(request)
    property_serializer = PropertySerializer(data=data)
    listing_serializer = ListingSerializer(data=data)
    if property_serializer.is_valid() and listing_serializer.is_valid():
        property_serializer.save()
        listing_serializer.save()
        return JsonResponse(listing_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(listing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'OPTIONS'])
def create_listing_existing_property(request, property_id=None):
    try:
        Property.objects.get(pk=property_id)
    except Property.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    data["property"] = property_id
    listing_serializer = ListingSerializer(data=data)
    if listing_serializer.is_valid():
        listing_serializer.save()
        return JsonResponse(listing_serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(listing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'OPTIONS'])
def delete_listing(request, property_id=None):
    try:
        property = Property.objects.get(pk=property_id)
    except Property.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)
    property.delete()
    return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'OPTIONS'])
def get_all_listing(request):
    listing = Listing.objects.all()
    serializer = ListingSerializer(listing, many=True)
    return JsonResponse(serializer.data, safe=False)
