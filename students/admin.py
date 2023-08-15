#config file for build in django admin app
##config models here
from django.contrib import admin
from .models import Student
# Register your models here.
admin.site.register(Student)