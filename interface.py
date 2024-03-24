from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from fonctions import *
from feuille_match import *
from stats import *

root = Tk()

canvas = Canvas(root, width=1015, height=648)
canvas.grid(row=0, column = 0)

fond = Image.open("images/fond_terrain.png")
fond = fond.resize((1015, 648))
fond_adapt = ImageTk.PhotoImage(fond)

canvas.create_image(0, 0, anchor=NW, image=fond_adapt)

style_label = ttk.Style()
style_label.configure('Custom.TLabel',
                      background='orange',
                      foreground='black',
                      padding=(30, 30),
                      font=('Arial', 22),
                      anchor='center'
)

style_label.configure('Custom2.TLabel',
                      background='blue',
                      foreground='white',
                      padding=(30, 30),
                      font=('Arial', 22),
                      anchor='center'
)

style_bouton = ttk.Style()
style_bouton.configure('Custom3.TLabel',
                       background='orange',
                       foreground='black',
                       padding=(13, 13),
                       font=('Arial', 14),
                       anchor='center'
)

style_bouton.configure('Custom4.TLabel',
                       background='blue',
                       foreground='white',
                       padding=(13, 13),
                       font=('Arial', 14),
)

style_bouton2 = ttk.Style()
style_bouton2.configure('Custom5.TLabel',
                        background='black',
                        foreground='white',
                        padding=(5, 5),
                        font=('Arial', 12),
)

ttk.Label(canvas, text="Équipe A", style='Custom.TLabel').grid(column=2, row=1, pady=40)
ttk.Button(canvas, text="2pts", style='Custom3.TLabel', command=lambda: menu_deroulant("2pts", "A")).grid(column=1, row=2, padx=10, pady=20)
ttk.Button(canvas, text="3pts", style='Custom3.TLabel', command=lambda: menu_deroulant("3pts", "A")).grid(column=2, row=2, padx=10, pady=20)
ttk.Button(canvas, text="LF", style='Custom3.TLabel', command=lambda: menu_deroulant("LF", "A")).grid(column=3, row=2, padx=10, pady=20)
ttk.Button(canvas, text="Rebond", style='Custom3.TLabel', command=lambda: menu_deroulant("rebond", "A")).grid(column=1, row=3, padx=10, pady=20)
ttk.Button(canvas, text="Contre", style='Custom3.TLabel', command=lambda: menu_deroulant("contre", "A")).grid(column=2, row=3, padx=10, pady=20)
ttk.Button(canvas, text="Faute", style='Custom3.TLabel', command=lambda: menu_deroulant("faute", "A")).grid(column=3, row=3, padx=10, pady=20)
ttk.Button(canvas, text="Passe décisive", style='Custom3.TLabel', command=lambda: menu_deroulant("passe décisive", "A")).grid(column=1, row=4, padx=10, pady=20)
ttk.Button(canvas, text="Perte de balle", style='Custom3.TLabel', command=lambda: menu_deroulant("perte de balle", "A")).grid(column=2, row=4, padx=10, pady=20)
ttk.Button(canvas, text="Interception", style='Custom3.TLabel', command=lambda: menu_deroulant("interception", "A")).grid(column=3, row=4, padx=10, pady=20)
ttk.Button(canvas, text="Changement", style='Custom3.TLabel', command=lambda: menu_deroulant("changement", "A")).grid(column=2, row=5, padx=10, pady=20)

ttk.Label(canvas, text="Équipe B", style='Custom2.TLabel').grid(column=6, row=1, pady=40)
ttk.Button(canvas, text="2pts", style='Custom4.TLabel', command=lambda: menu_deroulant("2pts", "B")).grid(column=5, row=2, padx=10, pady=20)
ttk.Button(canvas, text="3pts", style='Custom4.TLabel', command=lambda: menu_deroulant("3pts", "B")).grid(column=6, row=2, padx=10, pady=20)
ttk.Button(canvas, text="LF", style='Custom4.TLabel', command=lambda: menu_deroulant("LF", "B")).grid(column=7, row=2, padx=10, pady=20)
ttk.Button(canvas, text="Rebond", style='Custom4.TLabel', command=lambda: menu_deroulant("rebond", "B")).grid(column=5, row=3, padx=10, pady=20)
ttk.Button(canvas, text="Contre", style='Custom4.TLabel', command=lambda: menu_deroulant("contre", "B")).grid(column=6, row=3, padx=10, pady=20)
ttk.Button(canvas, text="Faute", style='Custom4.TLabel', command=lambda: menu_deroulant("faute", "B")).grid(column=7, row=3, padx=10, pady=20)
ttk.Button(canvas, text="Passe décisive", style='Custom4.TLabel', command=lambda: menu_deroulant("passe décisive", "B")).grid(column=5, row=4, padx=10, pady=20)
ttk.Button(canvas, text="Perte de balle", style='Custom4.TLabel', command=lambda: menu_deroulant("perte de balle", "B")).grid(column=6, row=4, padx=10, pady=20)
ttk.Button(canvas, text="Interception", style='Custom4.TLabel', command=lambda: menu_deroulant("interception", "B")).grid(column=7, row=4, padx=10, pady=20)
ttk.Button(canvas, text="Changement", style='Custom4.TLabel', command=lambda: menu_deroulant("changement", "B")).grid(column=6, row=5, padx=10, pady=20)

ttk.Button(canvas, text="Accueil", style='Custom5.TLabel').grid(column=1, row=6, padx=5, pady=32)
ttk.Button(canvas, text="Feuille", style='Custom5.TLabel').grid(column=7, row=6, padx=5, pady=32)

root.mainloop()