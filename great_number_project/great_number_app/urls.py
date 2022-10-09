from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('number_route', views.form),
    path('destroy', views.destroy)
]