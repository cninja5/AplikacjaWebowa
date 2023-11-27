from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
RodzajePlci = (
    ('M', 'Mężczyzna',),
    ('K', 'Kobieta',),
)

class Uzytkownicy(AbstractUser):
    plec = models.CharField(
        max_length=20,
        choices=RodzajePlci,
        default='1'
    )
    zdjProfilu = models.ImageField(upload_to='uploads/')
    groups = models.ManyToManyField(
        "auth.Group", related_name="customuser_set", blank=True, related_query_name="user"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
        related_query_name="user",
    )

class Znajomi(models.Model):
    idOsoba1 = models.ForeignKey(Uzytkownicy,on_delete=models.CASCADE)
    idOsoba2 = models.CharField(max_length=30)

class Listy(models.Model):
    loginWlasciciel = models.ForeignKey(Uzytkownicy,on_delete=models.CASCADE)
    tytul = models.CharField(max_length=50)
    opis = models.CharField(max_length=300)
    dataStworzenia = models.DateField(auto_now_add=True)

class Prezent(models.Model):
    idListy = models.ForeignKey(Listy,on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=254)
    loginRezerwacji = models.IntegerField()