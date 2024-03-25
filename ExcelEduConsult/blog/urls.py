from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:slug>/', views.detail, name='blog-detail'),
    path('tag/<slug:slug>/', views.tag, name='tag'),
]
