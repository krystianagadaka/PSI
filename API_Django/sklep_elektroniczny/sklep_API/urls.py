from django.urls import path
from . import views

urlpatterns = [
    path('klient', views.KlientList.as_view(), name=views.KlientList.name),
    path('klients/<int:pk>', views.KlientDetail.as_view(), name=views.KlientDetail.name),
    path('kategoria', views.KategoriaList.as_view(), name=views.KategoriaList.name),
    path('kategorias/<int:pk>', views.KategoriaDetail.as_view(), name=views.KategoriaDetail.name),
    path('produkt',views.ProduktList.as_view(), name=views.ProduktList.name),
    path('produkts/<int:pk>', views.ProduktDetail.as_view(), name=views.ProduktDetail.name),
    path('zamowienie', views.ZamowienieList.as_view(), name=views.ZamowienieList.name),
    path('zamowienies/<int:pk>', views.ZamowienieDetail.as_view(), name=views.ZamowienieDetail.name),
    path('',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]