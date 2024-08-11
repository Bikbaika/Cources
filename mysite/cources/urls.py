from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$',views.course_detail,name='course_detail'),
    url(r'^$',views.course_list,name='course_list'),
]