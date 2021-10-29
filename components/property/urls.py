from django.urls import path
from components.property import views

urlpatterns = [
    path('property/',
         views.get_property,
         name='get-property'),
    path('add-property/',
         views.add_property,
         name='add-property'),
]
