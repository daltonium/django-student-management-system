from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment, Grade


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'enrolled_on')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department')
    search_fields = ('first_name', 'last_name', 'department')
    list_filter = ('department',)
    ordering = ('department', 'last_name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'teacher')
    search_fields = ('code', 'title', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('teacher',)
    ordering = ('code',)

class GradeInline(admin.StackedInline):
    model = Grade
    extra = 0
    fields = ('score', 'letter_grade', 'remarks')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_on', 'get_grade')
    search_fields = (
        'student__first_name',
        'student__last_name',
        'course__title',
        'course__code'
    )
    list_filter = ('course',)
    inlines = [GradeInline]

    @admin.display(description='Grade')
    def get_grade(self, obj):
        try:
            return obj.grade.letter_grade
        except Grade.DoesNotExist:
            return 'Not graded'

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'score', 'letter_grade', 'graded_on')
    list_filter = ('letter_grade',)
    search_fields = (
        'enrollment__student__first_name',
        'enrollment__student__last_name',
        'enrollment__course__title'
    )
    ordering = ('-graded_on',)

admin.site.site_header = "Student Management Admin"
admin.site.site_title = "SMS Admin"
admin.site.index_title = "Dashboard"
