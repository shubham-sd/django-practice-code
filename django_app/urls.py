from django.urls import path
from . import views 

urlpatterns = [
    path("", views.insert_data),
    path("show_data/", views.show_data),
]