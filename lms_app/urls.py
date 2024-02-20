from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
]

