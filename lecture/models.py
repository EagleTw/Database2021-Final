from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student_Status(models.Model):
    status = models.CharField(max_length=20)    # 在學/休學/停學

    def __str__(self):
        return self.status

class Student_Grade(models.Model):
    grade = models.CharField(max_length=3, default="")
    verbose_grade = models.CharField(max_length=20, default="")  # e.g. 大一、大二

    def __str__(self):
        return self.verbose_grade


class Student_Class(models.Model):
    student_class = models.CharField(max_length=1, default="")

    def __str__(self):
        if self.student_class:
            return self.student_class
        else:
            return ' '

class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    student_name =  models.CharField(max_length=20, default="")
    student_dept = models.ForeignKey(Department, blank=False, null=True, on_delete=models.RESTRICT)
    student_status = models.ForeignKey(Student_Status, blank=False, null=True, on_delete=models.RESTRICT)
    grade = models.ForeignKey(Student_Grade, blank=False, null=False, on_delete=models.RESTRICT)
    student_class = models.ForeignKey(Student_Class, blank=True, null=True, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.student_dept) + str(self.student_class)  + " - " + self.id + " - " + self.student_name

# --------------------------------------------------------------

class Selected_Result(models.Model):
    result = models.CharField(max_length=20, default="")    # 選課結果, e.g. 中選、落選

    def __str__(self):
        return self.result

class Feedback_Result(models.Model):
    rank = models.IntegerField()                  # 教學評量, 1~5

    def __str__(self):
        return str(self.rank)

# --------------------------------------------------------------

class Teacher(models.Model):
    name = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name

class Course_Status(models.Model):
    course_status = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.course_status

class Course_Credit(models.Model):
    course_credit = models.IntegerField()

    def __str__(self):
        return str(self.course_credit)

class Semester(models.Model):
    semester = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.semester

class Course_Type(models.Model):
    course_type = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.course_type

class Building(models.Model):
    name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name

class Location(models.Model):
    building = models.ForeignKey(Building, blank=False, null=False, on_delete=models.RESTRICT)
    room = models.ForeignKey(Room, blank=False, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.building) + "-" + str(self.room)

class Course_Time(models.Model):
    course_time = models.CharField(max_length=10)

    def __str__(self):
        return self.course_time

# --------------------------------------------------------------

class Course_Info(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    semester  = models.ForeignKey(Semester, blank=False, null=False, on_delete=models.RESTRICT)
    course_name = models.CharField(max_length=20)

    course_type  = models.ForeignKey(Course_Type, blank=False, null=False, on_delete=models.RESTRICT)
    location  = models.ForeignKey(Location, blank=False, null=False, on_delete=models.RESTRICT)
    course_time = models.ForeignKey(Course_Time, blank=False, null=False, on_delete=models.RESTRICT)
    course_credit = models.ForeignKey(Course_Credit, blank=False, null=False, on_delete=models.RESTRICT)
    course_max_count = models.IntegerField()
    course_status = models.ForeignKey(Course_Status, blank=False, null=False, on_delete=models.RESTRICT)

    teacher = models.ForeignKey(Teacher, blank=False, null=False, on_delete=models.RESTRICT)
    student = models.ManyToManyField(Student, through='Enroll')

    course_class = models.CharField(max_length=10)  # A班、B班
    department = models.ForeignKey(Department, blank=False, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return self.course_name + '-' + str(self.semester)

class Enroll(models.Model):
    course = models.ForeignKey(Course_Info, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    selected_result = models.ForeignKey(Selected_Result, on_delete=models.CASCADE)
    course_score = models.IntegerField(blank=True, null=True)
    feedback_rank = models.ForeignKey(Feedback_Result, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['course', 'student']]
