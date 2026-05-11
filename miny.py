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
print("definovano")

##definice command
def play():
    global SIRKA, VYSKA, POCET_MIN
    
    # 1. Načtení textu z políček
    hodnota_x = nastavovaci_radek_x.get("1.0", "end-1c")
    hodnota_m = nastavovaci_radek_m.get("1.0", "end-1c")
    
    # 2. Kontrola, jestli nejsou políčka prázdná
    if hodnota_x == "":
        SIRKA = 10
        VYSKA = 10
        print("sirka chybí, nastavuji 10")
    if hodnota_m == "":
        POCET_MIN = 10
        print("pocet m chybí, nastavuji 10")
    else:
        # 3. Převod na čísla (teď už bezpečně)
        SIRKA = int(hodnota_x)
        VYSKA = SIRKA
        POCET_MIN = int(hodnota_m)
        
        # 4. Správný výpis (pomocí f-stringu)
        print(f"SIRKA: {SIRKA}")
        print(f"VYSKA: {VYSKA}")
        print(f"p_min: {POCET_MIN}")

    print("herní pole")
    lobby_okno.withdraw()
    herni_okno.deiconify()
    herni_okno.geometry(str(31* SIRKA) + "x" + str(26* VYSKA))
    
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
            t_tlacitko.grid(row=r, column=s)
            radek_tlacitek.append(t_tlacitko)
        # Tlačítka si můžeme ukládat do seznamu, abychom s nimi mohli později pracovat
        odhalené.append(radek_tlacitek)

##grafika  
# Vytvoření lobby okna
lobby_okno = tk.Tk()
lobby_okno.title("Miny_lobby")
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
#popis nastavovaciho pole x
x_x_label = tk.Label(lobby_okno, text="nast. vel. pole", font=("Arial", 10))
x_x_label.grid(pady=(25, 1))
#nastavení x*x
nastavovaci_radek_x = tk.Text(lobby_okno, height=1, font=("Arial", 10), width=13)
nastavovaci_radek_x.grid(pady=(1, 10))
#popis nastavovaciho pole m
m_label = tk.Label(lobby_okno, text="nast. počt min", font=("Arial", 10))
m_label.grid(pady=(10, 1))
#nastavení pocet min
nastavovaci_radek_m = tk.Text(lobby_okno, height=1, font=("Arial", 10), width=12)
nastavovaci_radek_m.grid(pady=(1, 5))

# Vytvoření herní okna
herni_okno = tk.Toplevel(lobby_okno)
herni_okno.title("Miny_hra")
herni_okno.geometry(str(31* SIRKA) + "x" + str(26* VYSKA))
herni_okno.withdraw()


# Spuštění programu
lobby_okno.mainloop()
