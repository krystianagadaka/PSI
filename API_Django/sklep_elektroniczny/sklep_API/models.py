from django.db import models

# Create your models here.

class Klient(models.Model):
    imie=models.CharField(max_length=40,null=False)
    nazwisko=models.CharField(max_length=40,null=False)
    email=models.CharField(max_length=40,null=False)

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return self.imie+' '+self.nazwisko+' '+self.email


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=40, null=False)

    class Meta:
        ordering = ('nazwa',)

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
        id_kategoria = models.ForeignKey(Kategoria, related_name='pro', on_delete=models.CASCADE)
        nazwa = models.CharField(max_length=40, null=False)
        producent = models.CharField(max_length=40, null=False)
        opis = models.TextField(max_length=200, null=False)
        cena = models.DecimalField(max_digits=20, decimal_places=2)

        class Meta:
            ordering = ('nazwa',)

        def __str__(self):
            return self.nazwa+' - '+self.producent+' - '+self.opis+' - '+self.cena.__str__()+'zl'


class Zamowienie(models.Model):
    id_klient = models.ForeignKey(Klient, related_name='zamowienia', on_delete=models.CASCADE)
    id_produkt = models.ForeignKey(Produkt, related_name='pro', on_delete=models.CASCADE)
    kwota = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        ordering = ('kwota',)

    def __str__(self):
        return str(self.id_klient) + ' ' + str(self.kwota) + 'zl'

