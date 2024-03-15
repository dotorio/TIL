from django.urls import path
# 명시적 상대경로
from . import views

app_name = 'acounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]