from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    questions = models.ManyToManyField('Question')

class Question(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    answer = models.CharField(max_length=255)
    choices = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.question_text
