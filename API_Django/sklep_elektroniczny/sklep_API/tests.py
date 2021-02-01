from rest_framework.test import APITestCase
from . import views
from .models import Produkt, Klient, Kategoria
from rest_framework import status
from rest_framework.reverse import reverse
from django import urls
class KlientTests(APITestCase):
    def post_klient(self,imie,nazwisko,email):
        url = reverse(views.KlientList.name)
        data = {'imie':imie,'nazwisko':nazwisko,'email':email}
        response = self.client.post(url, data, fromat='json')
        return response
    def test_post_and_get_klient(self):
        nowe_imie = 'Adam'
        nowe_nazwisko = 'Kszczot'
        nowy_email = 'szczota@interia.pl'
        response = self.post_klient(nowe_imie,nowe_nazwisko,nowy_email)
        assert response.status_code == status.HTTP_201_CREATED
        assert Klient.objects.count() == 1
        assert Klient.objects.get().imie == nowe_imie
        assert Klient.objects.get().nazwisko == nowe_nazwisko
        assert Klient.objects.get().email == nowy_email

    def test_get_klient(self):
        gimie = 'Tomasz'
        gnazwisko = 'Brzęczyszczykiewicz'
        gemail = 'brze@interia.pl'
        self.post_klient(gimie,gnazwisko,gemail)
        url = reverse(views.KlientList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['imie'] == gimie
        assert response.data['results'][0]['nazwisko'] == gnazwisko
        assert response.data['results'][0]['email'] == gemail
class KategoriaTests(APITestCase):
    def post_kategoria(self, nazwa):
        url = reverse(views.KategoriaList.name)
        data = {'nazwa':nazwa}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_book_category(self):
        nowa_kategoria = 'Słuchawki'
        response = self.post_kategoria(nowa_kategoria)
        print("PK {0}".format(Kategoria.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Kategoria.objects.count() == 1
        assert Kategoria.objects.get().nazwa == nowa_kategoria


    def test_get_kategoria(self):
        nowa_kategoria = 'Słuchawki'
        response = self.post_kategoria(nowa_kategoria)
        url = urls.reverse(views.KategoriaDetail.name, None, {response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert get_response.data['nazwa'] == nowa_kategoria


