from django.shortcuts import render, redirect, get_object_or_404
from .forms import mainForm
from .models import MainDB

def starting(request):
    if request.method=='POST':
        form = mainForm(request.POST or None)
        if form.is_valid():
            new_gamers = form.save()
            return redirect('detail', new_gamers.id)
    else:
        form = mainForm()
    
    return render(request, 'starting.html', {'form': form})

def detail(request, pk):
    game = get_object_or_404(MainDB, id=pk)
    return render(request, 'home.html', {'data': game})