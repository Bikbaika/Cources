from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Course,CourseAdmin)

# Register your models here.
