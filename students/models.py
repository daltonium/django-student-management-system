from django.db import models

# The Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# The Teacher Model
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# The Course Model
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"

# The Enrollment Model (Junction Table)
class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrolled_on = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} → {self.course}"

# The Grade Model
class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'A - Excellent'),
        ('B', 'B - Good'),
        ('C', 'C - Average'),
        ('D', 'D - Below Average'),
        ('F', 'F - Fail'),
    ]

    enrollment = models.OneToOneField(
        Enrollment,
        on_delete=models.CASCADE,
        related_name='grade'
    )
    score = models.DecimalField(max_digits=5, decimal_places=2)
    letter_grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    remarks = models.TextField(blank=True)
    graded_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.enrollment} - {self.letter_grade}"
