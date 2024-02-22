from django.urls import path
from . import views
from .views import AssignmentListView, AssignmentDetailView, AssignmentCreateView, AssignmentUpdateView, AssignmentDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('', AssignmentListView.as_view(), name='assignment_list'),
    path('<int:pk>/', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('create/', AssignmentCreateView.as_view(), name='assignment_create'),
    path('<int:pk>/update/', AssignmentUpdateView.as_view(), name='assignment_update'),
    path('<int:pk>/delete/', AssignmentDeleteView.as_view(), name='assignment_delete'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('assignments/<int:assignment_id>/add_question/', views.add_question, name='add_question'),
path('assignments/<int:assignment_id>/update_question/<int:question_id>/', views.update_question, name='update_question'),
    path('assignments/<int:assignment_id>/delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
]