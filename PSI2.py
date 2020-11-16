#1
def funkcja(a_lista,b_lista):
    c_lista=[]

    for i in enumerate(a_lista):
        if(i[0]%2==0):
            c_lista.append(i[1])

    for j in enumerate(b_lista):
        if(j[0]%2!=0):
            c_lista.append(j[1])

    return c_lista


print(funkcja([1,2,3,4],[5,6,7,8]))
#2
def funkcja2(data_text):
    slow={"length":"","letters":"","big_letters":"","small_letters":""}
    l=0
    a_lista=[]
    napis=""
    a_napis=""
    for i in data_text:
        l=l+1
    slow["length"]=l
    for j in data_text:
        a_lista.append(j)
    slow["letters"]=a_lista
    for k in data_text:
        napis=napis+k.capitalize()
    slow["big_letters"]=napis
    for l in data_text:
        a_napis=a_napis+l.lower()
    slow["small_letters"]=a_napis
    return(slow)
print(funkcja2("pies"))
#3
def funkcja3(letter,text):
    napis=""
    for i in text:
        if(i!=letter):
            napis=napis+i
        else:
            continue
    return napis
print(funkcja3("a","ada"))
#4
def funkcja4(C,temperature_type):
    K=C + 273.15
    F=(C * 1.8)+32
    R = (C + 273.15) * 1.8
    if(temperature_type=="K"):
        print(K)
    elif(temperature_type=="F"):
        print(F)
    elif(temperature_type=="R"):
        print(R)
    else:
        print("błąd")
funkcja4(55,"K")
#5
class Calculator:
    def __init__(self, a_liczba, b_liczba):
        self.a_liczba = a_liczba
        self.b_liczba = b_liczba
    def dod(self):
        return self.a_liczba+self.b_liczba
    def ode(self):
        return self.a_liczba-self.b_liczba
    def mno(self):
        return self.a_liczba*self.b_liczba
    def dzie(self):
        return self.a_liczba/self.b_liczba

pierwsza=Calculator(5,3)
print(pierwsza.dod())
#6
class ScienceCalculator(Calculator):

    def pot(self):
        return self.a_liczba**self.b_liczba
druga=ScienceCalculator(5,2)
print(druga.pot())
#7
def funkcja5(slowo):
    print(slowo[::-1])
funkcja5("pies")
#8










