from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from components.property.serializers import PropertySerializer
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

    min_area = request.query_params.get('min_area')
    max_area = request.query_params.get('max_area')
    min_price = request.query_params.get('min_price')
    max_price = request.query_params.get('max_price')
    min_price_per_area = request.query_params.get('min_price_per_area')
    max_price_per_area = request.query_params.get('max_price_per_area')

    order_field = request.query_params.get('order_by')
    sort_order = request.query_params.get('sort_order')

    # todo faire la gestion d'erreur
    # todo deplacer dans une fonction et prendre en compte tous les champs
    if min_area is not None:
        property = property.filter(area__gte=min_area)
    if max_area is not None:
        property = property.filter(area__lte=max_area)
    if min_price is not None:
        property = property.filter(price__gte=min_price)
    if max_price is not None:
        property = property.filter(price__lte=max_price)
    if min_price_per_area is not None:
        property = property.filter(price_per_area__gte=min_price_per_area)
    if max_price_per_area is not None:
        property = property.filter(price_per_area__lte=max_price_per_area)

    if order_field is not None and sort_order == "asc":
        property = property.order_by(order_field)
    elif order_field is not None and sort_order == "desc":
        property = property.order_by("-"+order_field)
    elif order_field is not None and sort_order not in ["asc", "desc"]:
        return JsonResponse("Error in field sort order", status=status.HTTP_400_BAD_REQUEST)

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
