from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Assignment, Question
from .forms import AssignmentForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

def assignment_detail(request, assignment_id):

class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'

class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment_detail.html'

class AssignmentCreateView(CreateView):
    model = Assignment
    template_name = 'assignment_form.html'
    fields = ['title']  # Add other fields as needed

class AssignmentUpdateView(UpdateView):
    model = Assignment
    template_name = 'assignment_form.html'
    fields = ['title']  # Add other fields as needed

class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'assignment_confirm_delete.html'
    success_url = reverse_lazy('assignment_list')

def add_question(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.assignment = assignment
            question.save()
            return redirect('assignment_detail', assignment_id=assignment.id)
    else:
        form = AssignmentForm()
    return render(request, 'lms_app/assignment_detail.html', {'assignment': assignment, 'form': form})


def update_question(request, assignment_id, question_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('assignment_detail', assignment_id=assignment.id)
    else:
        form = AssignmentForm(instance=question)
    return render(request, 'lms_app/update_question.html', {'assignment': assignment, 'question': question, 'form': form})

def delete_question(request, assignment_id, question_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('assignment_detail', assignment_id=assignment.id)

def assignment_list(request):
    assignments = Assignment.objects.all()
    paginator = Paginator(assignments, 5)  # Show 5 assignments per page

    page = request.GET.get('page')
    try:
        assignments = paginator.page(page)
    except PageNotAnInteger:
        assignments = paginator.page(1)
    except EmptyPage:
        assignments = paginator.page(paginator.num_pages)

    return render(request, 'lms_app/assignment_list.html', {'assignments': assignments})