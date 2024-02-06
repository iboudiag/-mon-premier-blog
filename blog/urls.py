# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:29:18 2024

@author: DIAGNE Ibrahima
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
