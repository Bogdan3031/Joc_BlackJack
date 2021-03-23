import random

nume=[]
prenume=[]
varsta=[]
tara=[]
jetoane=[]

with open('ListaParticipanți.txt','r') as f: #extragerea datelor din fisier si punerea lor in cate o lista
    file_words=[]
    for i in f:
        i_words=i.split()
        for j in i_words:
            file_words.append(j)
for j in file_words:
    if not j.isnumeric():
        if j=='George' or j=='Deroi' or j=='Joudl' or j=='Rosa':
            nume.append(j)
        elif j=='Mihai' or j=='Xavier' or j=='Petr' or j=='Ana':
            prenume.append(j)
        elif j=='Romania' or j=='Franta' or j=='Cehia' or j=='Italia':
            tara.append(j)
    elif int(j)<100:
        varsta.append(j)
    else:
        jetoane.append(j)

class Carte:
    def __init__(self, valoare_carte, tip_carte):
        self.valoare_carte = valoare_carte
        self.tip_carte = tip_carte

    def Afisare_carte(self):
        print('%s de %s' % (self.valoare_carte,self.tip_carte))

class Pachet(Carte):
    def __init__(self):
        self.deck=[Carte(i,j) for i in ['A','2','3','4','5','6','7','8','9','10','J', 'Q','K'] for j in ['Romb','Trefla'
                                                                                        ,'Inima Neagra','Inima Rosie']]
    def Afisare_Pachet(self):
            for i in self.deck:
                i.Afisare_carte()

    def Amestecare_Pachet(self):
        random.shuffle(self.deck)

    def Trage_Carte(self):
        return self.deck.pop()


class Jucator:

    def __init__(self,nume,prenume,varsta,tara,jetoane):
        self.deck = [Carte(i, j) for i in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] for j in
                     ['Romb', 'Trefla', 'Inima Neagra', 'Inima Rosie']]
        self.mana=[]
        self.valoare=0
        self.nume=nume
        self.prenume=prenume
        self.varsta=varsta
        self.tara=tara
        self.jetoane=jetoane
        self.suma=0


    def Trage_carte(self):
        carte_extrasa=random.choice(self.deck)
        self.mana.append(random.choice(self.deck))
        self.deck.remove(carte_extrasa)
        return self

    def Calculeaza_Valoarea(self):
        ace=False
        self.valoare=0
        for i in self.mana:
            if i.valoare_carte.isnumeric():
                self.valoare+=int(i.valoare_carte)
            else:
                if i.valoare_carte=='A':
                    ace=True
                    self.valoare+=10
                else:
                    self.valoare+=10
        if ace==True and self.valoare > 21:
            self.valoare-=10
        return self.valoare


    def Afiseaza_mana(self,nume):
        print('Mana lui %s este: \n' % (nume))
        for i in self.mana:
            print(i.valoare_carte,'de',i.tip_carte)

    def Bet(self,nume,prenume,total_jetoane):
        print('Acum pariaza %s %s \n' % (nume,prenume))
        while True:
            self.suma=int(input('Ce suma doresti sa pariezi?\n'))
            if self.suma<=int(total_jetoane):
                total_jetoane=int(total_jetoane)-self.suma
                print('%s a pariat %s jetoane si a ramas cu %s jetoane\n' % (nume,self.suma,total_jetoane))
                break
            else:
                print('Nu ai suficiente jetoane %s, introdu o suma mai mica de jetoane\n' % (nume))

    def Hit(self,nume,prenume):
        while True:
            raspuns=input('%s, doresti inca o carte?\n' % (nume))
            if raspuns=='da' and self.Calculeaza_Valoarea()<=21:
                self.Trage_carte()
                if self.Calculeaza_Valoarea()>21:
                    print('Jucatorul %s a iesit din joc\n' % (nume))
                    break
                if self.Calculeaza_Valoarea()==21:
                    print('BlackJack, %s %s a castigat!\n' % (nume,prenume))
                    break
            elif raspuns=='da' and self.Calculeaza_Valoarea()>21:
                self.Trage_carte()
                print('Jucatorul %s a iesit din joc\n' % (nume))
                while Dealer.Calculeaza_Valoarea()<17 and Dealer.Calculeaza_Valoarea()<self.Calculeaza_Valoarea():
                    Dealer.Trage_carte()
                break
            elif raspuns=='nu':
                while Dealer.Calculeaza_Valoarea()<17 and Dealer.Calculeaza_Valoarea()<self.Calculeaza_Valoarea():
                    Dealer.Trage_carte()
                break

    def Compare(self,nume,total_jetoane):
        if Dealer.Calculeaza_Valoarea()>self.Calculeaza_Valoarea() and Dealer.Calculeaza_Valoarea()<=21:
            print('Dealer-ul l-a batut pe %s in aceasta runda!\n' % (nume))
        else:
            print('%s a castigat aceasta runda si a castigat %s jetoane!\n' % (nume,2*self.suma))
            total_jetoane = int(total_jetoane) - self.suma
            print('%s are in acest moment %s jetoane\n' % (nume,2*self.suma+total_jetoane))

    def Reset_Mana_Dealer(self,nume):
        self.mana.clear()




p=Pachet()  # am declarat un obiect din clasa Pachet
p.Amestecare_Pachet()
George=Jucator('','',0,'',0) #am declarat 5 obiecte din clasa jucator goale
Deroi=Jucator('','',0,'',0)
Joudl=Jucator('','',0,'',0)
Rosa=Jucator('','',0,'',0)
Dealer=Jucator('','',0,'',0)

for j in [George,Deroi,Joudl,Rosa]: #utilizand listele am printat mesajele initiale cu datele fiecarui jucator
    for i in range(4):
        j=Jucator(nume[i],prenume[i],varsta[i],tara[i],jetoane[i])
        print('Jucatorul %s %s are %s ani si s a nascut in %s, acesta avand un numar total de %s jetoane' % (
        nume[i], prenume[i],
        varsta[i], tara[i], jetoane[i]))
        print('-----')
    break


George.Trage_carte().Trage_carte() #fiecare jucator trage 2 carti, iar dealer ul una singura
Deroi.Trage_carte().Trage_carte()
Joudl.Trage_carte().Trage_carte()
Rosa.Trage_carte().Trage_carte()
Dealer.Trage_carte()

playing=True

while playing:
    George.Bet(nume[0],prenume[0],jetoane[0])
    George.Afiseaza_mana(nume[0])
    George.Hit(nume[0],prenume[0])
    George.Afiseaza_mana(nume[0])
    Dealer.Afiseaza_mana('Dealer')
    if George.Calculeaza_Valoarea()>21:
        print('Jucatorul %s a pierdut!' % (nume[0]))
    else:
        George.Compare(nume[0],jetoane[0])
    Dealer.Reset_Mana_Dealer('Dealer')
    Dealer.Trage_carte()
    raspuns=input('%s, doresti sa joci din nou?\n' % (nume[0]))
    if raspuns=='da':
        George.Reset_Mana_Dealer(nume[0])
        George.Trage_carte().Trage_carte()
        continue
    else:
        playing=False


input('Apasa tasta ENTER pentru a continua cu urmatorul jucator:')

play=True

while play:
    Deroi.Bet(nume[1],prenume[1],jetoane[1])
    Deroi.Afiseaza_mana(nume[1])
    Deroi.Hit(nume[1],prenume[1])
    Deroi.Afiseaza_mana(nume[1])
    Dealer.Afiseaza_mana('Dealer')
    if Deroi.Calculeaza_Valoarea()>21:
        print('Jucatorul %s a pierdut!\n' % (nume[1]))
    else:
        Deroi.Compare(nume[1],jetoane[1])
    Dealer.Reset_Mana_Dealer('Dealer')
    Dealer.Trage_carte()
    rasp = input('%s, doresti sa joci din nou?\n' % (nume[1]))
    if rasp == 'da':
        Deroi.Reset_Mana_Dealer(nume[1])
        Deroi.Trage_carte().Trage_carte()
        continue
    else:
        play = False


input('Apasa tasta ENTER pentru a continua cu urmatorul jucator:')

Joaca=True

while Joaca:
    Joudl.Bet(nume[2],prenume[2],jetoane[2])
    Joudl.Afiseaza_mana(nume[2])
    Joudl.Hit(nume[2],prenume[2])
    Joudl.Afiseaza_mana(nume[2])
    Dealer.Afiseaza_mana('Dealer')
    if Joudl.Calculeaza_Valoarea()>21:
        print('Jucatorul %s a pierdut!\n' % (nume[2]))
    else:
        Joudl.Compare(nume[2],jetoane[2])
    Dealer.Reset_Mana_Dealer('Dealer')
    Dealer.Trage_carte()
    ras = input('%s, doresti sa joci din nou?\n' % (nume[2]))
    if ras == 'da':
        Joudl.Reset_Mana_Dealer(nume[2])
        Joudl.Trage_carte().Trage_carte()
        continue
    else:
        Joaca = False

input('Apasa tasta ENTER pentru a continua cu urmatorul jucator:')

joc=True

while joc:
    Rosa.Bet(nume[3],prenume[3],jetoane[3])
    Rosa.Afiseaza_mana(nume[3])
    Rosa.Hit(nume[3],prenume[3])
    Rosa.Afiseaza_mana(nume[3])
    Dealer.Afiseaza_mana('Dealer')
    if Rosa.Calculeaza_Valoarea()>21:
        print('Jucatorul %s a pierdut!\n' % (nume[3]))
    else:
        Rosa.Compare(nume[3],jetoane[3])
    Dealer.Reset_Mana_Dealer('Dealer')
    r = input('%s, doresti sa joci din nou?\n' % (nume[3]))
    if r == 'da':
        Rosa.Reset_Mana_Dealer(nume[3])
        Rosa.Trage_carte().Trage_carte()
        continue
    else:
        joc = False

if playing==False and joc==False and play==False and Joaca==False:
    print('Jocul de BlackJack s a incheiat!!!')








