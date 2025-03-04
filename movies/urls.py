from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.show, name='show'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
]