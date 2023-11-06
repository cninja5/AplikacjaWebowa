from django.db import models

# Create your models here.
RodzajePlci = (
    ('M', 'Mężczyzna',),
    ('K', 'Kobieta',),
)

class Uzytkownicy(models.Model):
    login = models.CharField(max_length=30)
    haslo = models.CharField(max_length=30)

class DaneUzytkownicy(models.Model):
    login = models.ForeignKey(Uzytkownicy,on_delete=models.CASCADE)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    plec = models.CharField(
        max_length=20,
        choices=RodzajePlci,
        default='1'
    )
    zdjProfilu = models.ImageField(upload_to='uploads/')

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