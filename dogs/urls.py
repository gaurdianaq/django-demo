from django.urls import path
from . import views

urlpatterns = [path("createDog/", views.create_dog, name="createDog")]
