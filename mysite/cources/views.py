from django.shortcuts import render, get_object_or_404
from .models import Course, Category

def course_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    courses= Course.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        courses = courses.filter(category = category)
    return render(request,
                  'cources/course/list.html',
                  {'courses':courses,
                   'category':category,
                   'categories':categories})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id, available = True)

    return render(request,
                  'cources/course/detail.html',
                  {'course':course})
# Create your views here.

def course_list_by_category(request, slug = None):
    return render(request,
                 'cources/course/course_list_by_category.html' )
