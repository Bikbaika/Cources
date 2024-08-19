from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from mysite.cart.cart import Cart
from mysite.cources.models import Course
from .forms import CartAddCourseForm

@require_POST
def cart_add(request, course_id):
    cart=Cart(request)
    course = get_object_or_404(Course, id = course_id)
    form = CartAddCourseForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(course=course, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, course_id):
    cart=Cart(request)
    course = get_object_or_404(Course, id = course_id)
    cart.remove(course)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart=Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})
# Create your views here.
