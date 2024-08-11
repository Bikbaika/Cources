from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    courses= Course.objects.filter(available = True)
    return render(request,
                  'cources/course/list.html',
                  {'courses':courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id, available = True)

    return render(request,
                  'cources/course/detail.html',
                  {'course':course})
# Create your views here.
