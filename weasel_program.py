# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Prosty program symulujący kumulowanie się mutacji na podstawie pomysłu Richarda Dawkinsa z książki "The Blind Watchmaker"

      #zaimportowanie bibliotek potrzebnych do działania programu
import random
import Sekwencja
from time import sleep

#klasa posiadająca metody do zapisu i odzczytu danych
class Wynik():
    ''' Zapisuje i odczytuje wyniki ewolucji sekwencji'''
        
    def zapisz_wynik(self, lista_wynikow):
        plik_sekw = open('wyniki_ewolucji_sekwencji', 'wt')
        for sekw in lista_wynikow:
            plik_sekw.write(sekw + '\n')
        plik_sekw.close()

    def odczytaj_wynik(self):
        l = 1 
        plik_odczyt = open('wyniki_ewolucji_sekwencji', 'rt')
        for linia in plik_odczyt:
            print(linia, end='')
            l+=1
            sleep(1)
        print(plik_odczyt.read())
        plik_odczyt.close()

       #funkcje używane w dalszej części programu

def pobierz_dane():
    #ciąg znaków, do którego będzie dążył program
    while True:
        try:
            sekwencja_wzor = input(f'Do jakiego ciągu znaków ma dążyć program? \n'+
                         '(Nie używaj dużych liter, cyfr, polskich liter, ani znaków przystankowych!)  ')
            int(sekwencja_wzor)
        except ValueError:
            break
        else:
            print('-----Nie używaj liczb-----')
    #lista utwożona by program nie działa  na ciągach znaków
    lista_wzor = []
    for i in sekwencja_wzor.lower():
        lista_wzor.append(i)
    while True:  
        try:
            prawdopodobienstwo_mutacji = float(input(f'Jakie jest prawdopodobieństwo zajścia mutacji? \n'+
                                          'Pamiętaj, że ma to być liczba od 0 do 1 (przy pisaniu ułamka użyj kropki, a nie przecinka!) '))
        except ValueError:
            print('-----Wpisz liczbę!-------')
        else:
            if prawdopodobienstwo_mutacji <= 0 or prawdopodobienstwo_mutacji > 1:
                print('-----Wpisz liczbę z przedziału (0,1)-------')
            else:
                break
    return lista_wzor, prawdopodobienstwo_mutacji


def losuj_sekwencje(dlugosc):
    '''losuje listę  o podanej liczbie elementów'''
    losowa_sekwencja=[]
    #lista losowe_znaki zawiera wszystkie znaki jakie mogą zostać wylosowane
    losowe_znaki=['q', 'w', 'e', 'r' ,'t', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                      'z', 'x', 'c', 'v', 'b', 'n', 'm', ' ',]
    #pętla uzupełnia pustą listę o pseudolosowe znaki losując tym samym sekwencje, która będzie ewoluować w dalszej części programu
    for i in range(1,dlugosc+1):
        # zmienna los określa jaki będzie kolejny znak w losowanej liście
        los=random.choice(losowe_znaki)
        losowa_sekwencja.append(los)
    return losowa_sekwencja

           # Główna częsc programu

lista_wzor, prawdopodobienstwo_mutacji = pobierz_dane()
dlugosc_sekw = len(lista_wzor)
sekwencja = Sekwencja.Sekwencja(losuj_sekwencje(dlugosc_sekw), prawdopodobienstwo_mutacji)
zmutowana_lista = sekwencja.losowa_sekwencja
#print(zmutowana_lista)
print('----------------------------------')

#lista przechowująca wyniki działania programu i przekazująca je do wydruku
lista_wynikow = []

#pętla wykonująca się do czsu, aż mutująca sekwencja pokryje się ze wzorem
while True:
    lista_podobienstw, lista_losowych_sekwencji = sekwencja.generuj_potomstwo(lista_wzor, zmutowana_lista)
    zmutowana_lista = sekwencja.wybierz_sekwencje(lista_podobienstw, lista_losowych_sekwencji)
    #print(zmutowana_lista)
    #print(losowa_sekwencja)
    wynik = sekwencja.zamien_na_str(zmutowana_lista)
    #print(wynik)
    lista_wynikow.append(wynik)
    if zmutowana_lista == lista_wzor:
        break

#zapisanie i wydruk wyników        
wynik_ewolucji = Wynik()
wynik_ewolucji.zapisz_wynik(lista_wynikow)
wynik_ewolucji.odczytaj_wynik()

