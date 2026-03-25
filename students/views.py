from django.db.models import Avg, Count, Max, Min
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Student, Teacher, Course, Enrollment, Grade
from .forms import StudentForm, TeacherForm, CourseForm, EnrollmentForm, GradeForm
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
    
class CourseListView(ListView):
    model = Course
    template_name = 'students/course_list.html'
    context_object_name = 'courses'
    ordering = ['code']


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/course_form.html'
    success_url = reverse_lazy('students:course-list')


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/course_form.html'
    success_url = reverse_lazy('students:course-list')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'students/course_confirm_delete.html'
    success_url = reverse_lazy('students:course-list')
    
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'students/enrollment_list.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        return Enrollment.objects.select_related( 'student', 'course', 'course__teacher').order_by('-enrolled_on')
        
class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'students/enrollment_form.html'
    success_url = reverse_lazy('students:enrollment-list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception:
            form.add_error(None, "This student is already enrolled in this course.")
            return self.form_invalid(form)
        
class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'students/enrollment_confirm_delete.html'
    success_url = reverse_lazy('students:enrollment-list')
    
class GradeListView(ListView):
    model = Grade
    template_name = 'students/grade_list.html'
    context_object_name = 'grades'

    def get_queryset(self):
        return Grade.objects.select_related(
            'enrollment__student',
            'enrollment__course'
        ).order_by('-graded_on')
        
class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'students/grade_form.html'
    success_url = reverse_lazy('students:grade-list')


class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'students/grade_form.html'
    success_url = reverse_lazy('students:grade-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # When editing, add the current enrollment back into the queryset
        # because it already has a grade and __init__ excluded it
        current_enrollment = self.object.enrollment
        form.fields['enrollment'].queryset = (
            form.fields['enrollment'].queryset |
            Enrollment.objects.filter(pk=current_enrollment.pk)
        )
        return form
    
class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'students/grade_confirm_delete.html'
    success_url = reverse_lazy('students:grade-list')
    
class ReportView(TemplateView):
    template_name = 'students/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Per-student report
        context['student_report'] = Student.objects.annotate(
            total_enrollments=Count('enrollments'),
            average_score=Avg('enrollments__grade__score'),
            highest_score=Max('enrollments__grade__score'),
            lowest_score=Min('enrollments__grade__score'),
        ).order_by('last_name')

        # Course-level stats
        context['course_report'] = Course.objects.annotate(
            total_students=Count('enrollments'),
            average_score=Avg('enrollments__grade__score'),
        ).order_by('code')

        return context

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Stat card counts
        context['total_students'] = Student.objects.count()
        context['total_teachers'] = Teacher.objects.count()
        context['total_courses'] = Course.objects.count()
        context['total_enrollments'] = Enrollment.objects.count()

        # Recent enrollments — last 5
        context['recent_enrollments'] = Enrollment.objects.select_related(
            'student', 'course'
        ).order_by('-enrolled_on')[:5]

        # Top 5 students by average score
        context['top_students'] = Student.objects.annotate(
            average_score=Avg('enrollments__grade__score')
        ).filter(
            average_score__isnull=False
        ).order_by('-average_score')[:5]

        return context