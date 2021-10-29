from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from components.property.serializers import PropertySerializer
from components.property.models import Property
from rest_framework.pagination import PageNumberPagination
paginator = PageNumberPagination()


@api_view(['POST', 'OPTIONS'])
def add_property(request):
    data = JSONParser().parse(request)
    serializer = PropertySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'OPTIONS'])
def get_property(request):
    property = Property.objects.all()
    result_page = paginator.paginate_queryset(property, request)
    serializer = PropertySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
