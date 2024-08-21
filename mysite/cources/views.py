from django.shortcuts import render, get_object_or_404
from .models import Course, Category
from cart.forms import CartAddCourseForm

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

def course_detail(request, id, slug):
    course = get_object_or_404(Course, id=id, slug= slug, available = True)

    cart_course_form = CartAddCourseForm()
    return render(request,
                  'cources/course/detail.html',
                  {'course':course,
                   'cart_course_form':cart_course_form})
# Create your views here.


