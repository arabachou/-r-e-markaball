from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def menu_deroulant():
    fenetre_menu = Tk()

    options = ["joueur 1", "joueur 2", "joueur 3", "joueur 4", "joueur 5",
               "joueur 6", "joueur 7", "joueur 8", "joueur 9", "joueur 10"]
    
    choix = ttk.Combobox(fenetre_menu, values=options)
    choix.grid(pady=10)

    fenetre_menu.mainloop()

def ajout_2pts():
    joueur_selec = choix.get()
    