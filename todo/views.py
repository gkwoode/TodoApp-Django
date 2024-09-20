from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# View to display tasks
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/home.html', context)


# View to delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')


# View to edit a task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'task': task}
    return render(request, 'todo/edit_task.html', context)
