from django.shortcuts import render, get_object_or_404
from .models import Assignment, Question

def home(request):
    return render(request, 'lms_app/home.html')

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'lms_app/assignment_list.html', {'assignments': assignments})

def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return render(request, 'lms_app/assignment_detail.html', {'assignment': assignment})
