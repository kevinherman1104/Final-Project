from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "original" ),#refers to index function in views.py file
    path("delete/<city_name>/", views.delete_city_option , name = "delete_city_option"), #"delete/<city_name>/" means in the html we need that form of delete 
]
