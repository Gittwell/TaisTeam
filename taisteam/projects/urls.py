from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('notice/', views.notice, name='notice'),
    path('letters_tais/', views.letters_tais, name='letters_tais'),
    path('letters_teks/', views.letters_teks, name='letters_teks'),
    path('letters_tech_bureau/', views.letters_tech_bureau, name='letters_tech_bureau'),
    path('incoming_letters/', views.incoming_letters, name='incoming_letters'),
    path('team/', views.team, name='team'),
    path('cats/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
]