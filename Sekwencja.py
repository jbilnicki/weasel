# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random 
class Sekwencja():
    '''Przechowuje sekwencję i wykonuje na niej działania'''
    def __init__(self, losowa_sekwencja, prawdopodobienstwo_mutacji):
        '''Ustalenie wartości artybutów'''
        self.losowa_sekwencja = losowa_sekwencja
        self.dlugosc = len(self.losowa_sekwencja)
        self.prawdopodobienstwo_mutacji = prawdopodobienstwo_mutacji
        
    #metody klasy Sekwencja
    def losuj_symbol(self):
        '''losuje jeden symbol z dostępych'''
        #lista losowe_znaki zawiera wszystkie znaki jakie mogą zostać wylosowane
        losowe_znaki=['q', 'w', 'e', 'r' ,'t', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                          'z', 'x', 'c', 'v', 'b', 'n', 'm', ' ',]
        los = random.choice(losowe_znaki)
        return los
    
    # def losuj_sekwencje(self, dlugosc):
        '''losuje listę  o podanej liczbie elementów'''
        #self.losowa_sekwencja=[]
        #pętla uzupełnia pustą listę o pseudolosowe znaki losując tym samym sekwencje, która będzie ewoluować w dalszej części programu
        #for i in range(1,self.__dlugosc+1):
            # zmienna los określa jaki będzie kolejny znak w losowanej liście
            #los = losuj_symbol(sekwencja)
           # self.losowa_sekwencja.append(los)
        #return self.losowa_sekwencja

    def zamien_na_str(self, losowa_sekwencja):
        ''' tworzy ciąg znaków  na podstawie listy losowa_sekwencja '''
        separator=''
        losowa_sekw=separator.join(losowa_sekwencja)
        #wydrukowany ciąg znaków będzie czytelniejszy dla użytkownika niż lista
        return losowa_sekw

    def porownaj_sekwencje(self, lista_wzor,  ls):
        '''Oblicza jak podobne są dwie sekwencje'''
        podobienstwo = 0
        for litera_1, litera_2 in zip(lista_wzor, ls):
            if litera_1 == litera_2:
                #sumuje różnice pomiędzy poruwnywanymi sekwencjami
                podobienstwo += 1    
        return podobienstwo

    def mutuj(self, ls):
        '''Symuluje mutacje jakie zachodzą w losowej sekwencji'''
        #pętla poruwnująca sekwencję wzór i losową sekwencję i dokonująca zmian w tej drugiej w oparciu o znaki wylosowane z listy losowe_znaki
        for index in range(self.dlugosc):
            mutacja = random.random()
            if mutacja < self.prawdopodobienstwo_mutacji:
                # zmienna los przechowuje znak wylosowany z listy losowe_znaki, któty zostanie wstawiony w listę losowa_sekwencja
                los = self.losuj_symbol()
                #print(los)
                ls[index] = los
        return ls

    def generuj_potomstwo(self, lista_wzor, wybrana_sekwencja):
        '''100 razy mutuje losową_sekwencję i do dalszego"rozrodu" dopuszcza tę najbradziej podobną do wzoru '''
        #lista_losowych_sekwencji przechowuje 100 potomnych list(losowych_sekwencji)
        lista_losowych_sekwencji = []
        #przechowuje podobieństwa między sekwencjami, lista_losowych_sekwencji i lista_podobienstw mają indexy, które odpowiadają sobie
        lista_podobienstw = []
        for i in range(100):
            #zmienna potomna przechowuje listę będącą zmutowaną losową_sekwencją
            potomna = self.mutuj(wybrana_sekwencja.copy())
            lista_losowych_sekwencji.append(potomna)
            #zmnienna roznice przechowuje podobieństwo między sekwenją mutującą a wzorem, wartość ta zostanie potem dodana do listy_podobienstw
            roznice = self.porownaj_sekwencje(lista_wzor, potomna)
            lista_podobienstw.append(roznice)
            #wybrana_sekwencja = self.wybierz_sekwencje(lista_podobienstw, lista_losowych_sekwencji)
        return lista_podobienstw, lista_losowych_sekwencji#, wybrana_sekwencja

    def wybierz_sekwencje(self, lista_podobienstw, lista_losowych_sekwencji):
        '''Wybiera sekwencję która jest najbardziej podobna do wzoru'''
        #zmienna przechowująca sekwencję najbardziej podobną do wzoru (początkowo jest określona jako None żeby mieć pewność,
        #że nie będzie liczby od niej mniejszej
        najwieksza = None
        #z każdą iteracją sprawdza czy jest jeszcze większa wartość
        for i in range(len(lista_podobienstw)):
            if najwieksza == None or lista_podobienstw[najwieksza] < lista_podobienstw[i]:
                najwieksza = i
        #zmienna podobna przechowuje tę listę, która jest najbardziej podobna do wzoru
        podobna = lista_losowych_sekwencji[najwieksza]
        return podobna
  
