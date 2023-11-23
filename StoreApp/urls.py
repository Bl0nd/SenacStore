from django.urls import path
from StoreApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
