from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from feuille_match import *
from stats import *

def menu_deroulant(type, equipe):
    global choix
    global fenetre_menu
    fenetre_menu = Tk()

    options = ["joueur1", "joueur2", "joueur3", "joueur4", "joueur5",
               "joueur6", "joueur7", "joueur8", "joueur9", "joueur10"]
   
    choix = ttk.Combobox(fenetre_menu, values=options)
    choix.grid(pady=10)

    choix.bind("<<ComboboxSelected>>", lambda event: new_event(type, equipe))

    fenetre_menu.mainloop()

def new_event(type, equipe) :

    joueur_selec = choix.get()

    if equipe == "A" :

        dictionnaire_stats[equipe][joueur_selec].append(type)

        if type == "2pts" :
            PointsEqA.append((2, joueur_selec))
        elif type == "3pts" :
            PointsEqA.append((3, joueur_selec))
        elif type == "LF" :
            PointsEqA.append((1, joueur_selec))
        elif type == "faute" :
            FautesEqA.append(joueur_selec)

    elif equipe == "B" :

        dictionnaire_stats[equipe][joueur_selec].append(type)

        if type == "2pts" :
            PointsEqB.append((2, joueur_selec))
        elif type == "3pts" :
            PointsEqB.append((3, joueur_selec))
        elif type == "LF" :
            PointsEqB.append((1, joueur_selec))
        elif type == "faute" :
            FautesEqB.append(joueur_selec)

    fenetre_menu.destroy()

    print(dictionnaire_stats)
    print(PointsEqA)
    print(PointsEqB)