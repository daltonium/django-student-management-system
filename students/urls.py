from django.urls import path
from .views import (
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
    CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView,
    EnrollmentListView, EnrollmentCreateView, EnrollmentDeleteView,
    GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView,
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

    # Courses
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/add/', CourseCreateView.as_view(), name='course-add'),
    path('courses/<int:pk>/edit/', CourseUpdateView.as_view(), name='course-edit'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    
    # Enrollments
    path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/add/', EnrollmentCreateView.as_view(), name='enrollment-add'),
    path('enrollments/<int:pk>/delete/', EnrollmentDeleteView.as_view(), name='enrollment-delete'),
    
    # Grades
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('grades/add/', GradeCreateView.as_view(), name='grade-add'),
    path('grades/<int:pk>/edit/', GradeUpdateView.as_view(), name='grade-edit'),
    path('grades/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade-delete'),
    
]