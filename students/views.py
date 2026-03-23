from .models import Student, Teacher, Course, Enrollment, Grade
from .forms import StudentForm, TeacherForm, CourseForm, EnrollmentForm, GradeForm

from django.db.models import Avg, Count, Max, Min

from .models import Student, Teacher, Course, Enrollment
from .forms import StudentForm, TeacherForm, CourseForm, EnrollmentForm
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
    