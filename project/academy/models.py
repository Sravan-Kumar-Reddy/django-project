from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        db_table = 'Student'

    FirstName = models.CharField(max_length=200,default = "FN")
    LastName = models.CharField(max_length=200,default = "LN")
    Email = models.CharField(max_length=200,default = "email")
    Courses = models.CharField(max_length=200,default = "Cou")
    def __str__(self):
        return self.FirstName

'''
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
'''


class Instructor(models.Model):
    class Meta:
        db_table = 'Instructor'

    FirstName = models.CharField(max_length=200,default = "FN")
    LastName = models.CharField(max_length=200,default = "LN")
    Email = models.CharField(max_length=200,default = "email")

    def __str__(self):
        return self.FirstName


class Course(models.Model):
    class Meta:
        db_table = 'Course'

    Name = models.CharField(max_length=200,default = "Cname")
    #Instructor = models.CharField(max_length=200,default = "Instructor")
    Instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    Semester = models.CharField(max_length=200,default = "Sem")
    Year = models.SmallIntegerField(default = 2015)
    def __str__(self):
        return self.Name