from .models import Klient,Kategoria,Produkt,Zamowienie
from .serializers import KlientSerializer,KategoriaSerializer,ProduktSerializer,ZamowienieSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'
    filter_fields = ['imie','nazwisko','email']
    ordering_fields = ['nazwisko']
   # permission_classes = [permissions.IsAuthenticated]

class KlientDetail(generics.RetrieveDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'
    permission_classes = [permissions.IsAuthenticated]

class KategoriaList(generics.ListCreateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-list'
    permission_classes = [permissions.IsAuthenticated]

class KategoriaDetail(generics.RetrieveDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-detail'
    permission_classes = [permissions.IsAuthenticated]

class ProduktFilter(FilterSet):
    min_cena = NumberFilter(field_name='cena',lookup_expr='gte')
    max_cena = NumberFilter(field_name='cena', lookup_expr='lte')
    class Meta:
        model = Produkt
        fields = ['min_cena','max_cena']
class ProduktList(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name='produkt-list'
    filter_class = ProduktFilter
    search_fields = ['nazwa', 'producent']
    ordering_fields = ['cena']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProduktDetail(generics.RetrieveDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer
    name = 'produkt-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ZamowienieList(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-list'
    ordering_fields = ['kwota']
    permission_classes = [permissions.IsAuthenticated]

class ZamowienieDetail(generics.RetrieveDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = 'zamowienie-detail'
    permission_classes = [permissions.IsAuthenticated]

class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self,request,*args,**kwargs):
        return Response({'produkts':reverse(ProduktList.name, request=request),
                         'klients':reverse(KlientList.name,request=request),
                         'kategorias':reverse(KategoriaList.name,request=request),
                         'zamowienies':reverse(ZamowienieList.name,request=request)})