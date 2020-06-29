from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('survey_page', views.survey_page),
    path('new_survey', views.new_survey),
    path('about/', views.about),
    path('interesting_finds/', views.interesting_finds),
    path('portfolio/', views.portfolio),
]