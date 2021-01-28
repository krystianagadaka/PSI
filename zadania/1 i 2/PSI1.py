#1
tekst="Czym jest Lorem Impsum"
print(tekst)
#2
imie="Krystian"
nazwisko="Nagadowski"
liczba_liter1=imie.count(imie[1])
liczba_liter2=nazwisko.count(nazwisko[2])
print(f"W tekście jest {liczba_liter1} liter oraz {liczba_liter2}")
#4
#tekst1='Tomek w krainie kangurów'
#print(dir(tekst1))
#help(tekst1.format_map())
#5
print(imie[::-1].capitalize() + " " + nazwisko[::-1].capitalize())
#6
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1=lista[0:5]
lista2=lista[5:11]
#7
lista1.extend(lista2)
lista1.insert(0,0)
lista_copy=lista1.copy()
lista_copy.sort(reverse=True)
print(lista_copy)
#8
pierwszy = (123532,'Adam','Kowalski')
drugi = (335643,'Euzebiusz','Smolarek')
lista_studentow = []
lista_studentow.append(pierwszy)
lista_studentow.append(drugi)
print(lista_studentow)
#9
student1 = {'imie':'Adam','nazwisko':'Kowalski','nrIndeksu':123532,'wiek':22,'adres e-mail':"kowalski1230@wp.pl",'Adres zamieszkania':'Piłsudskiego 25/3'}
student2 = {'imie':'Euzebiusz','nazwisko':'Smolarek','nrIndeksu':335643,'wiek':31,'adres e-mail':"smolariusz@wp.pl",'Adres zamieszkania':'Mickiewicza 5'}
student3 = {'imie':'Mariusz','nazwisko':'Kołowrotek','nrIndeksu':666333,'wiek':55,'adres e-mail':"kołowrotek@interia.pl",'Adres zamieszkania':'Słoneczna 12'}
#10
numery=[333221523,333221532,999324563,333221523]
numery=set(numery)
print(numery)
#11
for i in range(11):
    print(i)
print()
#12
for j in range(100,19,-5):
    print(j)
