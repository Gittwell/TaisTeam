from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('cats/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
]