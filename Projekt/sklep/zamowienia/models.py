from django.db import models

# Create your models here.

class Adres(models.Model):
    ulica = models.CharField(max_length=45,null=False)
    kod = models.CharField(max_length=6,null=False)
    miasto = models.CharField(max_length=45,null=False)

    class Meta:
        ordering = ('miasto',)
    def __str__(self):
        return self.miasto

class Zamowienie(models.Model):
    kwota = models.DecimalField(max_digits=15,decimal_places=2, default=5000)
    numer_zamowienia = models.CharField(max_length=20,null=False)
    zprodukt = models.ForeignKey(Adres, related_name="zadres", on_delete=models.CASCADE)

    class Meta:
        ordering = ('numer_zamowienia',)
    def __str__(self):
        return self.numer_zamowienia

class Pracownik(models.Model):
    imie = models.CharField(max_length=60,null=False)
    nazwisko = models.CharField(max_length=60,null=False)
    telefon = models.CharField(max_length=20,null=False)
    pesel = models.CharField(max_length=20,null=False)
    zarobki = models.DecimalField(max_digits=9,decimal_places=2, default=5000)
    padres = models.ForeignKey(Adres,related_name="padres",on_delete=models.CASCADE)
    pzamowienie = models.ForeignKey(Zamowienie, related_name="pzamowienie", on_delete=models.CASCADE)

    class Meta:
        ordering = ('imie',)
    def __str__(self):
        return self.imie+' '+self.nazwisko


class Klient(models.Model):
    imie = models.CharField(max_length=60,null=False)
    nazwisko = models.CharField(max_length=60,null=False)
    telefon = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=30,null=False)
    kadres = models.ForeignKey(Adres,related_name="kadres",on_delete=models.CASCADE)
    kzamowienie = models.ForeignKey(Zamowienie, related_name="kzamowienie", on_delete=models.CASCADE)

    class Meta:
        ordering = ('imie',)
    def __str__(self):
        return self.imie+' '+self.nazwisko



class Produkt(models.Model):
    nazwa = models.CharField(max_length=60,null=False)
    cena = models.DecimalField(max_digits=15, decimal_places=2, default=5000)
    typ = models.CharField(max_length=60, null=False)
    producent = models.CharField(max_length=60, null=False)
    gwarancja = models.CharField(max_length=60, null=False)

    class Meta:
        ordering = ('nazwa',)
    def __str__(self):
        return self.choice_text


