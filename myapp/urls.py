from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.TeamList.as_view(), name='team_list'),
    path('team/<int:pk>/players/', views.PlayerList.as_view(), name='player_list'),
    path('sample', views.SampleTemplateViews.as_view()),
    path('input', views.input, name='input'),
]
