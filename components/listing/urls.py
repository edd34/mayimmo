from django.urls import path
from components.listing import views

urlpatterns = [
    path('listing/',
         views.create_listing_create_property,
         name='create-listing-property'),
    path('listing/<int:property_id>',
         views.create_listing_existing_property,
         name='create-listing-existing-property'),
    path('delete-listing/<int:pk>/',
         views.delete_listing,
         name='delete-listing'),
    path('listing/',
         views.get_all_listing,
         name='word-find'),
]
