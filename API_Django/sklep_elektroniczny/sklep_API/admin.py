from django.contrib import admin
from .models import Klient,Produkt,Zamowienie,Kategoria
# Register your models here.
admin.site.register(Klient)
admin.site.register(Produkt)
admin.site.register(Zamowienie)
admin.site.register(Kategoria)