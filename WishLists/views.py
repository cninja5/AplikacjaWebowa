from django.http import HttpResponse
# Create your views here.

# views.py

from django.shortcuts import render
from .forms import ListyForm, ZawartoscListyForm


def createList(request):
    if request.method == 'POST':
        form = ListyForm(request.POST)
        zawartosc_form = ZawartoscListyForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.loginWlasciciel = request.user
            new_list.save()

            if zawartosc_form.is_valid():
                nazwy_prezentow = request.POST.getlist('prezenty')
                for nazwa_prezentu in nazwy_prezentow:
                    zawartosc = ZawartoscListy.objects.create(
                        idListy=new_list,
                        nazwaPrezentu=nazwa_prezentu
                    )
                    zawartosc.save()

            form.save_m2m()
            # Dodaj przekierowanie do innej strony po utworzeniu listy
    else:
        form = ListyForm()
        zawartosc_form = ZawartoscListyForm()

    return render(request, 'createList.html', {'form': form, 'zawartosc_form': zawartosc_form})