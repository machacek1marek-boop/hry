# Import knihoven
import tkinter as tk
import random
from tkinter import messagebox
import time

##globalní promenne
#NASTAVENÍ:
SIRKA = 10              # Počet sloupců
VYSKA = 10             # Počet řádků
POCET_MIN = 10          # Počet min na mapě
#DATOVÉ STRUKTURY:
herní_pole = []         # 2D pole [řádek][sloupec]  # - 'je_mina': True/False  # - 'počet_sousedů': 0-8                       
odhalené = []           # Které buňky vidíme?
vlajky = []             # Kde jsou vlajky?
#STAV HRY:
hra_bezi = True         # Běží hra?
cas_startu = 0          # Kdy se spustila
prvni_klik = True       # Garantovaně bez miny

##definice command
def prepni_na(cilove_okno):
    # Projdeme všechna okna v seznamu a skryjeme je
    for okno in vsechna_okna:
        okno.withdraw()
    
    # Ukážeme jen to jedno, které chceme
    cilove_okno.deiconify()
    print(f"Přepnuto na: {cilove_okno.title()}")

def settings_back():
    global SIRKA, VYSKA, POCET_MIN
    # 1. Načtení textu z políček
    hodnota_x = nastavovaci_radek_x.get("1.0", "end-1c")
    hodnota_m = nastavovaci_radek_m.get("1.0", "end-1c")
    if hodnota_x == "":
        SIRKA = 10
        VYSKA = 10
        print("sirka chybí, nastavuji 10")
    else:
        SIRKA = int(hodnota_x)
        VYSKA = SIRKA
    if hodnota_m == "":
        POCET_MIN = SIRKA
        print("mina auto")
    else:
        POCET_MIN = int(hodnota_m)
        print("mina nastaven")
    # 4. výpis
    print(f"SIRKA: {SIRKA}")
    print(f"VYSKA: {VYSKA}")
    print(f"p_min: {POCET_MIN}")
    print("zpet do lobby")
    prepni_na(lobby_okno)
    
def kontrola():
    global SIRKA, VYSKA, POCET_MIN
    if SIRKA == "":
        SIRKA = 10
        VYSKA = 10
        rint("sirka chybí, nastavuji 10")
    if POCET_MIN == "":
        POCET_MIN = 10
        print("pocet m chybí, nastavuji 10")
        
def reset():
    global  SIRKA, VYSKA, POCET_MIN, herní_pole, odhalené, prvni_klik, hra_bezi
    prvni_klik = True
    hra_bezi = True
    # Vyčištění okna od starých tlačítek
    for widget in herni_okno.winfo_children():
        if widget != lista_nahore and widget != lista_akci:
            widget.destroy()
    # Zde kompletně vyprázdníme stará data
    herní_pole = []
    odhalené = []

def rozmisteni_min():
    global SIRKA, VYSKA, POCET_MIN, herní_pole, odhalené, prvni_klik, hra_bezi
    #pridat rozmistení

def l_klik_na_poplicko():
    global SIRKA, VYSKA, POCET_MIN, herní_pole, odhalené, prvni_klik, hra_bezi
    if prvni_klik:
        rozmisteni_min()
    if herní_pole[r][s]["je_mina"]:
        print("BUM! Konec hry.")
        odhalené[r][s].config(text="💣", bg="red")
        # Sem pak dodáš zprávu pro hráče a zablokování hry
    else:
        print(f"Klikl jsi na bezpečné políčko [{r}, {s}]")
        # Sem pak dodáš zobrazení čísla (počtu sousedů)

def play():
    global SIRKA, VYSKA, POCET_MIN, herní_pole, odhalené, prvni_klik, hra_bezi
    kontrola()    
    prepni_na(herni_okno)
    herni_okno.geometry(str(31* SIRKA) + "x" + str(26* VYSKA+66))
    lista_akci.grid(row=SIRKA+1, column=0, columnspan=10, sticky="w")
    reset()
    # ==============================================================================
    # ZDE JE TVORBA 2D POLE SE SLOVNÍKY:
    # ==============================================================================
    for r in range(VYSKA):          # Procházíme řádky (např. 0 až 9)
        radek_mapy = []             # Vytvoříme jeden prázdný řádek
        
        for s in range(SIRKA):      # V každém řádku projdeme sloupce (např. 0 až 9)
            # Vytvoříme slovník pro jedno konkrétní políčko
            policko = {
                "je_mina": False,
                "pocet_sousedu": 0
            }
            # Přidáme políčko do aktuálního řádku
            radek_mapy.append(policko)
            
        # Když máme celý řádek plný políček, vložíme ho do hlavní mapy
        herní_pole.append(radek_mapy)
    for r in range(VYSKA):
        radek_tlacitek = []
        for s in range(SIRKA):
            # Vytvoříme tlačítko pro každou souřadnici
            t_tlacitko = tk.Button(
                herni_okno, 
                text=" ", 
                width=3, 
                height=1,
                command=lambda r=r, s=s: klik_na_policko(r, s)
            )
            # Umístíme ho do mřížky (grid)
            t_tlacitko.grid(row=r+1, column=s)
            radek_tlacitek.append(t_tlacitko)
        # Tlačítka si můžeme ukládat do seznamu, abychom s nimi mohli později pracovat
        odhalené.append(radek_tlacitek)
    

###grafika  
## Vytvoření lobby okna
lobby_okno = tk.Tk()
lobby_okno.title("lobby_okno")
lobby_okno.geometry("600x500")
#logo lable
logo_label = tk.Label(lobby_okno, text="Miny", font=("Arial", 25))
logo_label.grid(pady=(10, 5), padx=250)
#logo
logo = tk.Label(lobby_okno, text="💣", bg="red", font=("Arial", 40))
logo.grid(pady=(5, 10))   
#play buton
play_tlacitko = tk.Button(lobby_okno, text="Play 🔺", font=("Arial", 25), bg="green", command=play)
play_tlacitko.grid(pady=(10, 25))
#settings buton
settings_tlacitko = tk.Button(lobby_okno, text="⚙nastavení", font=("Arial", 10), bg="grey", command=lambda: prepni_na(settings_okno))
settings_tlacitko.grid(pady=(150, 25))

##vytvorení settings okna
settings_okno = tk.Toplevel(lobby_okno)
settings_okno.title("settings_okno")
settings_okno.geometry("300x300")
#settings bvak buton
back_tlacitko = tk.Button(settings_okno, text="⬅️", font=("Arial", 10), bg="grey", command=settings_back)
back_tlacitko.grid(pady=(10, 25), padx=138)
#popis nastavovaciho pole x
x_x_label = tk.Label(settings_okno, text="velikost pole", font=("Arial", 10))
x_x_label.grid(pady=(25, 1))
#nastavení x*x
nastavovaci_radek_x = tk.Text(settings_okno, height=1, font=("Arial", 10), width=13)
nastavovaci_radek_x.grid(pady=(1, 10))
#popis nastavovaciho pole m
m_label = tk.Label(settings_okno, text="počet min", font=("Arial", 10))
m_label.grid(pady=(10, 1))
#nastavení pocet min
nastavovaci_radek_m = tk.Text(settings_okno, height=1, font=("Arial", 10), width=12)
nastavovaci_radek_m.grid(pady=(1, 5))
settings_okno.withdraw()

## Vytvoření herní okna
herni_okno = tk.Toplevel(lobby_okno)
herni_okno.title("herni_okno")
herni_okno.geometry("200x200")
#lista nehore frame 
lista_nahore = tk.Frame(herni_okno)
lista_nahore.grid(row=0, column=0, columnspan=10, sticky="w")
#back buton
back_tlacitko = tk.Button(lista_nahore, text="⬅️", font=("Arial", 10), bg="grey", command=lambda: prepni_na(lobby_okno))
back_tlacitko.grid(row= 0, column=0, pady=(0, 5))
#settings buton
settings_tlacitko = tk.Button(lista_nahore, text="⚙nastavení", font=("Arial", 10), bg="grey", command=lambda: prepni_na(settings_okno))
settings_tlacitko.grid(row= 0, column=1, pady=(0, 5))
#lista dole frame
lista_akci = tk.Frame(herni_okno)
lista_akci.grid(row=SIRKA+1, column=0, columnspan=10, sticky="w", pady=(5, 0))
#settings buton
settings_tlacitko = tk.Button(lista_akci, text="neco", font=("Arial", 10), bg="grey")
settings_tlacitko.grid(row= 0, column=1, pady=(0, 5))
#ukoncení
herni_okno.withdraw()

# Seznam všech oken pro snadnou hromadnou práci
vsechna_okna = [lobby_okno, settings_okno, herni_okno]

# Spuštění programu
lobby_okno.mainloop()