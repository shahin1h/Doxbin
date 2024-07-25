from django.shortcuts import render, redirect
from .models import doxbin
from .forms import DoxbinForm


# Create your views here.
def index(request):
    doxes = doxbin.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'doxes': doxes})


def dox(request, slug):
    doxes = doxbin.objects.get(slug=slug)
    title = doxes.title
    return render(request, 'dox.html', {'doxes': doxes, 'title': title})


def new_dox(request):
    if request.method == 'POST':
        form = DoxbinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'new_dox.html', {'form': form})
    form = DoxbinForm()
    return render(request, 'new_dox.html', {'form': form})


def error_404(request):
    title = 'Not Found'
    return render(request, '404.html', {'title': title})
