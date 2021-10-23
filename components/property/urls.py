from django.urls import path
from components.property import views

urlpatterns = [
    path('get-property/',
         views.get_property,
         name='get-property'),
]
