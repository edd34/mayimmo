from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from components.address.models import Address
from components.address.serializers import AddressSerializer


@api_view(['GET', 'OPTIONS'])
def get_address(request):
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST', 'OPTIONS'])
def add_address(request):
    data = JSONParser().parse(request)
    serializer = AddressSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
