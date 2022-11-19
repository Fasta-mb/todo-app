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
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            
            return HttpResponseRedirect(reverse('home'))
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
        forms = TodoForm(request.POST, instance=form)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    return render(request, 'app/index.html', {'todoforms': todoforms})

def weekly_task(request):
    forms = Todo.objects.all().order_by('-date')
    todoforms = TodoForm()
    if request.POST:
        forms = TodoForm(request.POST)
        if forms.is_valid():
            forms.save()
            
            return HttpResponseRedirect(reverse('weekly-task'))
    context = {'todoforms': todoforms, 'forms': forms}
    return render(request, 'app/weekly_task.html', context)