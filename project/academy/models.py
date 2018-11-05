from django.db import models

# Create your models here.



class Instructor(models.Model):
    class Meta:
        db_table = 'Instructor'

    firstname = models.CharField(max_length=200,default = "FN")
    lastname = models.CharField(max_length=200,default = "LN")
    email = models.EmailField(max_length=200,default = "email")

    def __str__(self):
        return self.firstname


class Course(models.Model):
    class Meta:
        db_table = 'Course'

    name = models.CharField(max_length=200,default = "Cname")
    #Instructor = models.CharField(max_length=200,default = "Instructor")
    #year = models.SmallIntegerField(default = 2015)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE)
    semester_year = models.CharField(max_length=200,default = "Sem")
    def __str__(self):
        return self.name

class Student(models.Model):
    class Meta:
        db_table = 'Student'

    firstname = models.CharField(max_length=200,default = "FN")
    lastname = models.CharField(max_length=200,default = "LN")
    email = models.CharField(max_length=200,default = "email")
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.firstname

'''
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
'''
