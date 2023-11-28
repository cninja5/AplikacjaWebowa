from django.http import HttpResponse
# Create your views here.

# views.py

from django.shortcuts import render,redirect
from .forms import ListyForm, DodajPrezentDoListyForm


def createList(request):
    if request.method == 'POST':
        form = ListyForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.loginWlasciciel = request.user
            new_list.save()
            idList = new_list.id

        return redirect('/addPresents/',idList=idList)
    else:
        form = ListyForm()
    return render(request, 'createList.html', {'form': form })

def addPresents(request,idList):
    if request.method == 'POST':
        form = DodajPrezentDoListyForm(request.POST)
        if form.is_valid():
            new_prezent = form.save(commit=False)
            new_prezent.idListy =idList
            new_prezent.save()
#        return redirect('/addPresents')
    else:
        form = DodajPrezentDoListyForm()
    return render(request, 'addPresentsToList.html', {'form': form })
