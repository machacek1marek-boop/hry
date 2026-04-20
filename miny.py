# Import knihoven
import tkinter as tk
import random
from tkinter import messagebox
import time

##globalní promenne
#NASTAVENÍ:
SIRKA = 10              # Počet sloupců
VYSKA = 10              # Počet řádků
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
def play():
    print("pole")
    lobby_okno.withdraw()
    herni_okno.deiconify()
    
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
logo_label.grid(pady=(10, 20), padx=250)
#logo
logo = tk.Label(lobby_okno, text="💣", bg="red", font=("Arial", 40))
logo.grid(pady=(10, 20))   
#play buton
play_tlacitko = tk.Button(lobby_okno, text="Play 🔺", font=("Arial", 18), bg="green", command=play)
play_tlacitko.grid(pady=(20, 40))

# Vytvoření herní okna
herni_okno = tk.Toplevel(lobby_okno)
herni_okno.title("Miny_lobby")
herni_okno.geometry("600x500")
herni_okno.withdraw()

# Spuštění programu
lobby_okno.mainloop()