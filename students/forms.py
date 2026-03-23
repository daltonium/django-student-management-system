from django import forms
from .models import Student, Teacher, Course, Enrollment, Grade


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'department']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'teacher']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['enrollment', 'score', 'letter_grade', 'remarks']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show enrollments that don't have a grade yet
        graded_ids = Grade.objects.values_list('enrollment_id', flat=True)
        self.fields['enrollment'].queryset = Enrollment.objects.exclude(
            id__in=graded_ids
        ).select_related('student', 'course')