from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('cats/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
]