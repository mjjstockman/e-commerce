from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name='all_products'),
    path('add/', views.add, name='add_products'),
]