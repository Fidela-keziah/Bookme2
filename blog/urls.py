from django.urls import path
from .views import article_view, article_admin_view

urlpatterns = [
    path('', article_view, name='blog'),
    path('article_admin_view/', article_admin_view, name='article_admin_view'),
]