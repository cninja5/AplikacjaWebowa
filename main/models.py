from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
RodzajePlci = (
    ('M', 'Mężczyzna',),
    ('K', 'Kobieta',),
)


class Znajomi(models.Model):
    idOsoba1 = models.ForeignKey(User, on_delete=models.CASCADE)
    idOsoba2 = models.CharField(max_length=30)

class Listy(models.Model):
    loginWlasciciel = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=50)
    opis = models.CharField(max_length=300)
    dataUtworzenia = models.DateField(auto_now_add=True)
    # zawartosc = models.ManyToManyField('ZawartoscListy', related_name='zawartoscListy', blank=True)

class Prezent(models.Model):
    idListy = models.ForeignKey(Listy, on_delete=models.CASCADE)
    nazwaPrezentu = models.CharField(max_length=254)
    loginRezerwacji = models.IntegerField()

class ZawartoscListy(models.Model):
    idListy = models.ForeignKey(Listy, on_delete=models.CASCADE)
    nazwaPrezentu = models.CharField(max_length=254)

    def __str__(self):
        return self.nazwaPrezentu
