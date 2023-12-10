from django.db import models
from django.contrib.auth.models import User

# Create your models here.
RodzajePlci = (
    ('M', 'Mężczyzna',),
    ('K', 'Kobieta',),
)


class ProfilUzytkownika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/')


class Znajomi(models.Model):
    idZapraszajacego = models.ForeignKey(User, default='0', on_delete=models.CASCADE, related_name='senderId')
    idZapraszanego = models.ForeignKey(User, default='0', on_delete=models.CASCADE, related_name='invitedId')
    status = models.CharField(max_length=30, default='Wysłano')


class Listy(models.Model):
    loginWlasciciel = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=50)
    opis = models.CharField(max_length=300)
    dataUtworzenia = models.DateField(auto_now_add=True)


class ZawartoscListy(models.Model):
    idListy = models.ForeignKey(Listy, on_delete=models.CASCADE)
    nazwaPrezentu = models.CharField(max_length=254)
    loginRezerwacji = models.ForeignKey(User, db_column="username", on_delete=models.CASCADE, null=True)
    linkDoPrezentu = models.CharField(max_length=1024, blank=True, null=True)
    cenaPrezentu = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.nazwaPrezentu
