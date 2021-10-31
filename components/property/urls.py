from django.urls import path
from components.property import views

urlpatterns = [
    path('paginated-property/',
         views.get_paginated_property,
         name='get-paginated-property'),
    path('property/',
         views.get_all_property,
         name='get-property'),
    path('add-property/',
         views.add_property,
         name='add-property'),
    path('get-property-filter/',
         views.get_property_filter,
         name='get-property-filter'),
]
