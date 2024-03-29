from django.urls import path
from . import views
from django.conf.urls.static import static
from BurmachachDevSearch import settings

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>', views.project, name="project"),

    path('create-project/', views.createProject, name='create-project'),
    path('edit-project/<str:pk>', views.editProject, name='edit-project'),
    path('delete-project/<str:pk>', views.deleteProject, name='delete-project'),
    path('delete-review/<str:pk>', views.deleteReview, name='delete-review')
]

