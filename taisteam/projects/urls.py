from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('letters_tais/', views.letters_tais, name='letters_tais'),
    path('letters_teks/', views.letters_teks, name='letters_teks'),
    path('cats/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
]