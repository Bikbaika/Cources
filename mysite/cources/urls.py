from django.urls import path
from . import views

app_name = 'cources'

urlpatterns = [
    path('<int:id>/',views.course_detail,name='course_detail'),
    path('',views.course_list,name='course_list'),
]