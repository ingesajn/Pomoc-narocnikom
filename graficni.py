import sqlite3 as dbapi
import tkinter as tk
import datetime
import tkinter.ttk

class PomocNarocnikom:
    def __init__(self):
        #okno
        self.okno = tk.Tk()
        self.okno.configure(background = 'papaya whip')
        self.okno.resizable(0, 0)   
        self.okno.title('Pomoč naročnikom')
        self.okno.geometry('+300+30')

        self.povezava = dbapi.connect('baza.sqlite3')  #vzpostavimo povezavo
        self.rezultat = self.povezava.cursor()   #vključimo cursor

        #meni
        self.meni = tk.Menu(self.okno)

        
        podmeni1 = tk.Menu(self.meni)
        self.meni.add_cascade(label = 'O meni', menu = podmeni1)
        podmeni1.add_command(label = 'Moj naročniški profil', command = self.narocniskiProfil)
        
        self.okno.config(menu = self.meni)

        self.vhodnoPlatno()    #ustvarimo še začetno platno
        self.okno.mainloop()

    def vhodnoPlatno(self):
        ''' platno s podatki, ki ga vidimo, ko program zaženemo '''
        #platno velikosti 500x650
        self.platno = tk.Canvas(self.okno, width = 500, height = 650, background = 'papaya whip')
        
        #naslov
        self.platno.create_text(250, 50, text = 'Pomoč naročnikom', font = 'Calibri 20', fill = 'royal blue')
        self.platno.grid(row = 0, columnspan = 2)
        
        #aktualni naročniški paketi
        self.platno.create_text(20, 120, anchor = 'w', text = 'Paketi trenutno na voljo: ', font = 'Calibri 14', fill = 'royal blue')
        self.seznam = []
        sql = "SELECT id, ImePaketa, CenaPaketa, KolicinaMinut, KolicinaMinut, KolicinaSMS FROM Narocniski_paketi"
        self.rezultat.execute(sql)
        zapisi = self.rezultat.fetchall()
        for paket in zapisi:
            novPaket1 = paket[1] + ' - ' + 'Cena: ' + paket[2] + '€'+ ' (min:' + paket[3] + ')' 
            self.seznam.append(novPaket1)
        n = len(self.seznam)
        stevec = 140
        for i in range(n):
            paketiii = self.seznam[i]    
            self.platno.create_text(20, stevec, anchor = 'w', text = paketiii, font = 'Calibri 10', fill = 'black')
            stevec += 20
        self.platno.grid(row = 1, column = 0)
        
        #aktualni mobilniki
        self.platno.create_text(320, 120, anchor = 'w', text = 'Aktualni mobilniki: ', font = 'Calibri 14', fill = 'royal blue')
        self.seznamMob = []
        sql = "SELECT Telefoni.Ime FROM Telefoni"
        self.rezultat.execute(sql)
        zapisi = self.rezultat.fetchall()
        for mobi in zapisi:
            novMobi = mobi[0]
            self.seznamMob.append(novMobi)
        n = len(self.seznamMob)
        stevec = 140
        for i in range(n):
            mobijiii = self.seznamMob[i]  
            self.platno.create_text(320, stevec, anchor = 'w', text = mobijiii, font = 'Calibri 10', fill = 'black')
            stevec += 20
        self.platno.grid(row = 1, column = 1)





        #izpis današnjega datuma
        datum = str(datetime.date.today())
        datumSeznam = datum.split('-')   #datum z ukazom split ločimo pri -, dobimo seznam
        dan = datumSeznam[2]
        mesec = datumSeznam[1]
        leto = datumSeznam[0]
        lepDatum = dan + '.' + mesec + '.' + leto
        self.platno.create_text(20, 580, anchor = 'w', text = 'Današnji datum:', font = 'Calibri 14', fill = 'royal blue')
        self.platno.create_text(20, 600, anchor = 'w', text = lepDatum, font = 'Calibri 10', fill = 'black')
        self.platno.grid(row = 2, column = 1)        


    def narocniskiProfil(self):
        
        #odpre novo okno
        self.novoOkno = tk.Tk()
        self.novoOkno.configure(background = 'papaya whip')
        self.novoOkno.title('Moj naročniški profil')
        self.novoOkno.resizable(0, 0)
        self.novoOkno.geometry("%dx%d%+d%+d" % (300, 200, 0, 0))
        self.novoOkno.geometry('+350+70')

        #meni
        self.meni = tk.Menu(self.novoOkno)
        podmeni = tk.Menu(self.meni)
        self.meni.add_cascade(label = 'Izhod', menu = podmeni)
        podmeni.add_command(label = 'Izhod', command = self.novoOkno.destroy)
        self.novoOkno.config(menu = self.meni)      





PomocNarocnikom()
