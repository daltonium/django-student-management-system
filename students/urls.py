from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
)

app_name = 'students'

urlpatterns = [
    # Students
    path('', StudentListView.as_view(), name='student-list'),
    path('add/', StudentCreateView.as_view(), name='student-add'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student-edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # Teachers
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/add/', TeacherCreateView.as_view(), name='teacher-add'),
    path('teachers/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher-edit'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
]