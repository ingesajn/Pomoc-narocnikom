import sqlite3
import time
import datetime


datoteka_baze = "Baza.sqlite3"



def cena_telefona_v_prosti_prodaji(telefon):
    '''Funkcija, ki preveri ceno izbranega telefona v prosti prodaji.'''    
    c = baza.cursor()

    c.execute("""SELECT CenaProstaProdaja FROM Telefoni""")
    res = c.fetchone()
    if res is None:
        c.close()
        raise Exception('Noben telefon ni na voljo!')
    else:
        cena_telefona = res[0]  #vrnemo prvo komponento
    

def cena_telefona(narocniskiPaket, telefon):
    '''Funkcija, ki izračuna ceno izbranega telefona na izbranem naročniškem paketu.'''
    cena_v_prosti_prodaji=cena_telefona_v_prosti_prodaji(telefon)
    popust = c.execute("""SELECT Popust FROM Narocniski_paketi""")
    return cena_v_prosti_prodaji - (cena_v_prosti_prodaji * (popust/100))




def moznost_nove_vezave_in_menjave_paketa(narocnik):
    '''Funkcija, ki preverja, če lahko naročnik kupi nov telefon oziroma izbere nov paket.'''
    
    cur = baza.execute("SELECT datum_vezave FROM narocnik limit 1")
    datum = cur.fetchone()
    datum = datum[0]

    danes = datetime.date.today()
    razlika = danes - datum
    razlika.days
    
    if razlika.days < 730:
        print('Vezava s prejšnjim telefonskim aparatom žal še ni potekla!')
    else:
        print('Izberite si nov naročniški paket in željeni telefon!')

#iskanje telefonov po lastnostih
##def telefon_po_lastnostih(seznam_lastnosti):
##    '''Funkcija prejme seznam id-jev lastnosti in vrne seznam imen telefonov'''
##    
##    lastnost = c.execute("""SELECT id FROM lastnosti""")
##    telefon = c.execute("""SELECT id FROM Telefoni""")
##
##



baza = sqlite3.connect(datoteka_baze, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
