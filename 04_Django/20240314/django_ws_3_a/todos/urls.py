from django.urls import path
# 명시적 상대경로
from . import views

app_name = 'todos'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<str:work>/', views.detail, name='detail'),
    path('create_todo/', views.create_todo, name='create_todo'),
]