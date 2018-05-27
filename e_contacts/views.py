from django.shortcuts import render, redirect
from .forms import AddContact
from .models import Contacts

# Create your views here.

def index(request):
    return render(request, 'home.html')

def list(request):
    contacts = Contacts.objects.all()
    return render(request, 'list.html', {'contacts': contacts})

def add(request):
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return redirect('add')

    else:
        form = AddContact()
        return render(request, 'add.html', {'form':form})