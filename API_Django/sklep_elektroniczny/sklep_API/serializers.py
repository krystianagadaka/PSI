from rest_framework import serializers
from .models import Klient,Produkt,Kategoria,Zamowienie

class KlientSerializer(serializers.HyperlinkedModelSerializer):
    zamowienia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienie-detail')
    class Meta:
        model = Klient
        fields = ['id','url','imie','nazwisko','email','zamowienia']

class KategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kategoria
        fields = ['id','url','nazwa']

class ProduktSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produkt
        fields = ['id','url','id_kategoria','nazwa','producent','opis','cena']

class ZamowienieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Zamowienie
        fields = ['id','url','id_klient','id_produkt','kwota']
