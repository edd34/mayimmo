from django.urls import path
from components.address import views

urlpatterns = [
    path('get-address/',
         views.get_address,
         name='get-address'),
    path('add-address/',
         views.add_address,
         name='add-address'),
]
