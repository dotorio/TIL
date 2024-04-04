from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:book_pk>/<int:review_pk>/delete', views.delete, name='delete'),
    path('<int:book_pk>/create/', views.create, name='create'),
]
