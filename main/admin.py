from django.contrib import admin
from .models import Uzytkownicy,Znajomi,Listy,Prezent,ZawartoscListy

admin.site.register(Uzytkownicy)
admin.site.register(Znajomi)
admin.site.register(Listy)
admin.site.register(Prezent)
admin.site.register(ZawartoscListy)

# Register your models here.
