from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('notice/', views.NoticeView.as_view(), name='notice'),
    path('letters_tais/', views.LettersTaisView.as_view(), name='letters_tais'),
    path('letters_teks/', views.LettersTeksView.as_view(), name='letters_teks'),
    path('letters_tech_bureau/', views.LettersTechBureauView.as_view(), name='letters_tech_bureau'),
    path('incoming_letters/', views.IncomingLettersView.as_view(), name='incoming_letters'),
    path('team/', views.TeamView.as_view(), name='team'),
]