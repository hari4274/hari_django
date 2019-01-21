from django.contrib import admin

# Register your models here.
from .models import Student, Task

admin.site.register(Student)
admin.site.register(Task)
