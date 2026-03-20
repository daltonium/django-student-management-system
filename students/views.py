from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Student, Teacher, Course
from .forms import StudentForm, TeacherForm
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    ordering = ['last_name', 'first_name']

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:student-list')

class TeacherListView(ListView):
    model = Teacher
    template_name = 'students/teacher_list.html'
    context_object_name = 'teachers'
    ordering = ['department', 'last_name']


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'students/teacher_form.html'
    success_url = reverse_lazy('students:teacher-list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'students/teacher_form.html'
    success_url = reverse_lazy('students:teacher-list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'students/teacher_confirm_delete.html'
    success_url = reverse_lazy('students:teacher-list')