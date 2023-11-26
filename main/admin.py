from django.contrib import admin
from .models import Uzytkownicy,DaneUzytkownicy,Znajomi,Listy,Prezent

admin.site.register(Uzytkownicy)
admin.site.register(DaneUzytkownicy)
admin.site.register(Znajomi)
admin.site.register(Listy)
admin.site.register(Prezent)

# Register your models here.
