from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
# Read 
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# Create
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

# Update
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'todo/update_task.html', {'task': task})

# Delete
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')