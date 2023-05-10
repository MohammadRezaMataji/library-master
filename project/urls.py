from django.urls import path
from . import views
urlpatterns = [
    path('project/<str:pk>/', views.project, name='project'),
    path('',views.projects, name='projects'),
    path('create-book/', views.createbook, name='create-book'),
    path('update-book/<str:pk>/', views.updatebook, name='update-book'),
    path('delete-book/<str:pk>/', views.deletebook, name='delete-book'),
]