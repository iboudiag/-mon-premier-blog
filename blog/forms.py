# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:06:48 2024

@author: DIAGNE Ibrahima
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)