from django.shortcuts import redirect, render

from django.http import HttpResponse

from .models import List
from .form import ListForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('added success'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Deleted'))
    return redirect('home')

def TaskDone(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False

    item.save()
    return redirect('home')

def TaskUndone(request, list_id):
    item = List.objects.get(pk=list_id)
 
    item.completed = True
    item.save()
    return redirect('home')