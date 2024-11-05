from django.db import models

class CoursLevel(models.Model):
    level_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cours_level'

    def __str__(self):
        return f"Level: {self.level_name}"


class Course(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.ForeignKey(CoursLevel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'

    def __str__(self):
        return f"Course: {self.name}, Duration: {self.duration} hours, Price: ${self.price}"


class Group(models.Model):
    group_name = models.CharField(unique=True, max_length=45)
    number_of_students = models.IntegerField()
    instructor = models.ForeignKey('Instructor', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group'

    def __str__(self):
        return f"Group: {self.group_name}, Students: {self.number_of_students}"


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'

    def __str__(self):
        return f"Instructor: {self.first_name} {self.last_name}, Specialization: {self.specialization}"


class Mark(models.Model):
    mark = models.DecimalField(max_digits=5, decimal_places=1)
    date_mark = models.DateField()
    comment = models.TextField(blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mark'

    def __str__(self):
        return f"Mark: {self.mark} for {self.student}, Date: {self.date_mark}"


class Material(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    file_path = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material'

    def __str__(self):
        return f"Material for {self.course}: {self.file_path}"


class Payment(models.Model):
    registration = models.ForeignKey('Registration', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'

    def __str__(self):
        return f"Payment: ${self.amount} on {self.payment_date} for registration {self.registration}"


class Registration(models.Model):
    registration_date = models.DateField()
    payment_status = models.CharField(max_length=20)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'registration'

    def __str__(self):
        return f"Registration: {self.course} on {self.registration_date}, Status: {self.payment_status}"


class Schedule(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)
    session_date = models.DateField()
    duration_hours = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schedule'

    def __str__(self):
        return f"Schedule: {self.course} - {self.group} on {self.session_date}, Duration: {self.duration_hours} hours"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(unique=True, max_length=45)
    registration_date = models.DateField()
    registration = models.ForeignKey(Registration, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Email: {self.email}"


class StudentCourse(models.Model):
    student = models.OneToOneField(Student, models.DO_NOTHING, primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_course'
        unique_together = (('student', 'course'),)

    def __str__(self):
        return f"StudentCourse: {self.student} enrolled in {self.course}"
