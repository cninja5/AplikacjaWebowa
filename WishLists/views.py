from django.http import HttpResponse
# Create your views here.

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ListyForm, DodajPrezentDoListyForm
from main.models import Listy, ZawartoscListy, Znajomi
from django.contrib import messages


def createList(request):
    if request.method == 'POST':
        form = ListyForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.loginWlasciciel = request.user
            new_list.save()
            idList = new_list.id

        return redirect('/addPresents/' + str(idList) + '/')
    else:
        form = ListyForm()
    return render(request, 'createList.html', {'form': form})


def addPresents(request, idList):
    list_object = get_object_or_404(Listy, pk=idList)
    zawartosc_listy = ZawartoscListy.objects.filter(idListy=list_object)
    numerListy = idList
    if list_object.loginWlasciciel != request.user:
        return redirect('myLists')
    if request.method == 'POST':
        form = DodajPrezentDoListyForm(request.POST)
        if form.is_valid():
            new_prezent = form.save(commit=False)
            new_prezent.idListy = list_object
            new_prezent.save()
            # Możesz przekazać dodatkowe dane z obiektu Listy do szablonu
            return render(request, 'addPresentsToList.html',
                          {'form': DodajPrezentDoListyForm(), 'zawartosc_listy': zawartosc_listy,
                           'tytul': list_object.tytul, 'opis': list_object.opis, 'numerListy': numerListy})
    else:
        form = DodajPrezentDoListyForm()

    return render(request, 'addPresentsToList.html',
                  {'form': form, 'zawartosc_listy': zawartosc_listy, 'tytul': list_object.tytul,
                   'opis': list_object.opis, 'numerListy': numerListy})


def myLists(request):
    listy_uzytkownika = Listy.objects.filter(loginWlasciciel=request.user).order_by('-id')
    return render(request, 'myLists.html', {'listy': listy_uzytkownika})


def friendsLists(request):
    result = Znajomi.objects.filter(status="Przyjaciele", idZapraszajacego=request.user.id).values_list(
        'idZapraszanego', flat=True)
    listy_uzytkownika = Listy.objects.filter(loginWlasciciel__in=result).order_by('-id')
    return render(request, 'friendsLists.html', {'listy': listy_uzytkownika})


def deleteList(request, idList):
    list_object = get_object_or_404(Listy, pk=idList)

    if request.method == 'POST':
        if list_object.loginWlasciciel != request.user:
            return redirect('myLists')
        list_object.delete()
        messages.success(request, 'Lista została pomyślnie usunięta.')
        return redirect('myLists')

    return redirect('myLists')  # Przekierowanie w przypadku innych metod HTTP niż POST


def specificList(request, idList):
    list_object = get_object_or_404(Listy, pk=idList)
    zawartosc_listy = ZawartoscListy.objects.filter(idListy=list_object).order_by('id')
    listOwnerId = list_object.loginWlasciciel.id

    return render(request, 'mySpecificList.html',
                  {'zawartosc_listy': zawartosc_listy, 'tytul': list_object.tytul, 'opis': list_object.opis,
                   'numerListy': idList, 'ownerId': listOwnerId})


def deletePresent(request, idPrezent, idList):
    prezent = get_object_or_404(ZawartoscListy, pk=idPrezent)
    prezent.delete()

    return redirect('addPresents', idList=idList)


def makeGiftReservation(request, idList, idGift):
    prezent = get_object_or_404(ZawartoscListy, id=idGift)
    prezent.loginRezerwacji = request.user
    prezent.save()

    return redirect('specificList', idList=idList)


def cancelGiftReservation(request, idList, idGift):
    prezent = get_object_or_404(ZawartoscListy, id=idGift)
    prezent.loginRezerwacji = None
    prezent.save()

    return redirect('specificList', idList=idList)


def myGiftReservations(request):

    return render(request, "myGiftReservations.html")
