from django.db import models

# Create your models here.


class Login(models.Model):
    Username = models.CharField(max_length=80)
    Password = models.CharField(max_length=20)
    Type = models.CharField(max_length=70)


class College(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=20)


class Feedback(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    date = models.DateField()


class Department(models.Model):
    department = models.CharField(max_length=40)


class Student(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    COLLEGE = models.ForeignKey(College, on_delete=models.CASCADE)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField()
    place = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=30)


class Complaint(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    reply = models.CharField(max_length=300)


class Camera(models.Model):
    COLLEGE = models.ForeignKey(College, on_delete=models.CASCADE)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    camera = models.CharField(max_length=500)
    date = models.DateField()


class Notification(models.Model):
    notification = models.CharField(max_length=200)
    date = models.DateField()


class Rating(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.CharField(max_length=100)
    date = models.DateField()


class Staff(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    DEPARTMENT_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    COLLEGE = models.ForeignKey(College, on_delete=models.CASCADE)


class CollegeNotification(models.Model):
    COLLEGE = models.ForeignKey(College, on_delete=models.CASCADE)
    notification = models.CharField(max_length=200)
    date = models.DateField()


class StudentComplaint(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=300)
    date = models.DateField()
    reply = models.CharField(max_length=200)


class Attendance(models.Model):
    Date = models.CharField(max_length=20)
    Attendance = models.CharField(max_length=20)
    STUDENT_ID = models.ForeignKey(Student, on_delete=models.CASCADE)


class Emotions(models.Model):
    Emotion = models.CharField(max_length=30)
    Date = models.DateField()
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
