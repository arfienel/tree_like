from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name='index'),
    path('article/<slug:slug>/', article, name='article'),
]