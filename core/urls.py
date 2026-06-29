from django.urls import path
from .views import project_create_view, project_update_view, project_delete_view, explorer_view

urlpatterns = [
    path('explore/', explorer_view, name='explorer'),
    path('project/new/', project_create_view, name='project_create'),
    path('project/<int:pk>/edit/', project_update_view, name='project_update'),
    path('project/<int:pk>/delete/', project_delete_view, name='project_delete'),
]