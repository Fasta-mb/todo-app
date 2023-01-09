from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from app.form import TodoForm

from app.models import Todo

# Create your views here.

def index(request):
    # weekly = Todo.objects.filter(type=type)
    forms = Todo.objects.all().order_by('-date')
    todoforms = TodoForm()
    if request.POST:
        todoforms = TodoForm(request.POST)
        if todoforms.is_valid():
            todoforms.save()
            for form in forms:
                if form.type == 'weekly':
                    return redirect(reverse('weekly-task'))
                else:
                    return redirect(reverse('home'))
                
            
    context = {'todoforms': todoforms, 'forms': forms}
    
    return render(request, 'app/index.html', context)


def delete(request, id):
    delete = Todo.objects.get(id=id)
    delete.delete()
    return HttpResponseRedirect(reverse('home'))

def updateTodo(request, id):
    form = Todo.objects.get(id=id)
    todoforms = TodoForm(instance=form)
    if request.method == 'POST':
        todoforms = TodoForm(request.POST, instance=form)
        if todoforms.is_valid():
            todoforms.save()
            return redirect('home')
    return render(request, 'app/index.html', {'todoforms': todoforms})

def weekly_task(request):
    forms = Todo.objects.all().order_by('-date')
    todoforms = TodoForm()
    if request.POST:
        todoforms = TodoForm(request.POST)
        if todoforms.is_valid():
            todoforms.save()
            for form in forms:
                if form.type == 'daily':
                    return redirect(reverse('home'))
                else:
                    return redirect(reverse('weekly-task'))
            
    context = {'todoforms': todoforms, 'forms': forms}
    return render(request, 'app/weekly_task.html', context)