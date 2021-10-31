from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from components.property.serializers import PropertySerializer, PropertyFilterSerializer
from components.property.models import Property
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg, Max, Min, Sum
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
def get_paginated_property(request):
    property = Property.objects.all()
    paginator.page_size = 10
    paginator.page_query_param = 'page'
    paginator.page_size_query_param = 'per_page'
    result_page = paginator.paginate_queryset(property, request)
    serializer = PropertySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'OPTIONS'])
def get_all_property(request):
    property = Property.objects.all()
    serializer = PropertySerializer(property, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'OPTIONS'])
def get_property_filter(request):
    query = Property.objects.all()
    data = query.aggregate(
        min_area=Min('area'),
        max_area=Max('area'),
        avg_area=Avg('area'),
        min_price=Min('price'),
        max_price=Max('price'),
        avg_price=Avg('price'),
        min_price_per_area=Min('price_per_area'),
        max_price_per_area=Max('price_per_area'),
        avg_price_per_area=Avg('price_per_area'),
    )

    return JsonResponse(data, safe=False)
