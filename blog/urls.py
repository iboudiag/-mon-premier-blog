# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:29:18 2024

@author: DIAGNE Ibrahima
"""

from django.urls import path
from . import views
from .views import symptomes

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('symptomes/', symptomes, name='symptomes'),
]
