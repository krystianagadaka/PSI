from .models import Klient,Kategoria,Produkt,Zamowienie
from .serializers import KlientSerializer,KategoriaSerializer,ProduktSerializer,ZamowienieSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse



class KlientList(generics.ListAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'
class KlienteDetail(generics.RetrieveDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'

class KategoriaList(generics.ListAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-list'
class KategoriaDetail(generics.RetrieveDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-detail'

class ProduktList(generics.ListAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name='produkt-list'
class ProduktDetail(generics.RetrieveDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkt-detail'

class ZamowienieList(generics.ListAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-list'
class ZamowienieDetail(generics.RetrieveDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-detail'

class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self,request,*args,**kwargs):
        return Response({'produkty':reverse(ProduktList.name, request=request),
                         'klienci':reverse(KlientList.name,request=request),
                         'kategorie':reverse(KategoriaList.name,request=request),
                         'zamowienia':reverse(ZamowienieList.name,request=request)})