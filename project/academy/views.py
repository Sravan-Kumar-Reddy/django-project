from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def index(request):
    student_entries = Student.objects.all()
    course_entries = Course.objects.all()
    instructor_entries = Instructor.objects.all()

    template = loader.get_template('academy/index.html')
    context = {
        'student_entries' : student_entries,
        'course_entries' : course_entries,
        'instructor_entries' : instructor_entries
    }
    return HttpResponse(template.render(context,request))

