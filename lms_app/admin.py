from django.contrib import admin
from .models import Teacher, Student, Assignment, Question

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Question)
