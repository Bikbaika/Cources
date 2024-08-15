from django.urls import path
from . import views

app_name = 'cources'

urlpatterns = [
    path('<int:id>/',views.course_detail,name='course_detail'),
    path('',views.course_list,name='course_list'),
    path('list_by_category', views.course_list_by_category, name='course_list_by_category')
]