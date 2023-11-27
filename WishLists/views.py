from django.http import HttpResponse
# Create your views here.

# views.py

from django.shortcuts import render
from .forms import ListyForm


def createList(request):
    if request.method == 'POST':
        form = ListyForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.loginWlasciciel = request.user  # Ustaw właściciela listy na aktualnego użytkownika
            new_list.save()
            form.save_m2m()  # Zapisz many-to-many relacje, jeśli istnieją
            # Możesz dodać tutaj przekierowanie do innej strony po utworzeniu listy
    else:
        form = ListyForm()

    return render(request, 'createList.html', {'form': form})