import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

PointsEqA = []
PointsEqB = []

FautesEqA = []
FautesEqB = []

#df_eqA = pd.DataFrame({'Points': PointsEqA, 'Fautes': FautesEqA})

#df_eqB = pd.DataFrame({'Points': PointsEqB, 'Fautes': FautesEqB})

#print("Feuille de match :")
#print("Équipe A :")
#print(df_eqA.describe())
#print("\nÉquipe B :")
#print(df_eqB.describe())


def generate_feuille_match():
    c = canvas.Canvas("feuille_de_match.pdf", pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(230, 750, "FEUILLE DE MATCH")


    cell_width = 38
    cell_height = 10

    x_left = 25
    y_top = 650
    x_right = 250
    y_bottom = 750

    data = {
        "EqA": {
            "Fautes": {
                "Joueur 1": [True, False, False, False, False],
                "Joueur 2": [False, False, False, False, False],
                "Joueur 3": [True, True, True, True, True],
                "Joueur 4": [False, False, False, False, False],
                "Joueur 5": [True, False, False, False, False],
                "Joueur 6": [False, False, False, False, False],
                "Joueur 7": [True, True, True, True, True],
                "Joueur 8": [False, False, False, False, False],
                "Joueur 9": [True, False, False, False, False],
                "Joueur 10": [False, False, False, False, False]
            },
            "Points": [(2, "Joueur 4"), (3, "Joueur 7"), (1, "Joueur 3"), (2, "Joueur 10")]
        },
        "EqB": {
            "Fautes": {
                "Joueur 1": [True, False, False, False, False],
                "Joueur 2": [False, False, False, False, False],
                "Joueur 3": [True, True, True, True, True],
                "Joueur 4": [False, False, False, False, False],
                "Joueur 5": [True, False, False, False, False],
                "Joueur 6": [False, False, False, False, False],
                "Joueur 7": [True, True, True, True, True],
                "Joueur 8": [False, False, False, False, False],
                "Joueur 9": [True, False, False, False, False],
                "Joueur 10": [False, False, False, False, False]
            },
            "Points": [(2, "Joueur 1"), (3, "Joueur 4"), (2, "Joueur 9")]
        }
    }

    faults_table(c, data["EqA"]["Fautes"], x_left, y_top - 50, cell_width, cell_height, "Équipe A")
    faults_table(c, data["EqB"]["Fautes"], x_left, y_top - 250, cell_width, cell_height, "Équipe B")

    points_table(c, data["EqA"]["Points"] + data["EqB"]["Points"], x_right, y_top, cell_width, cell_height)


    c.showPage()

    c.save()

def faults_table(c, data, x, y, cell_width, cell_height, equipe):
    c.setFont("Helvetica", 8)

    c.rect(x, y, 6 * cell_width, cell_height)

    for i in range(7):
        c.line(x + i * cell_width, y, x + i * cell_width, y - 11 * cell_height)

    for i in range(12):
        c.line(x, y - i * cell_height, x + 6 * cell_width, y - i * cell_height)

    text_width = c.stringWidth("Fautes " + equipe, "Helvetica", 8)
    x_position = x + (cell_width)/2
    y_position = y + cell_height/2 - 3
    c.drawString(x_position, y_position, "Fautes " + equipe)

    for i in range(1, 6):
        text_width = c.stringWidth(str(i), "Helvetica", 8)
        x_position = x + i * cell_width + (cell_width - text_width) / 2
        y_position = y - cell_height + cell_height/2 - 3
        c.drawString(x_position, y_position, str(i))
    
    y -= cell_height
    
    for i, (key, value) in enumerate(data.items()):
        c.drawString(x, y - (i + 1) * cell_height + cell_height/2 - 4, key)
        
        for j, item in enumerate(value):
            if isinstance(item, bool):
                text_width = c.stringWidth("X" if item else "", "Helvetica", 8)
                x_position = x + (j + 1) * cell_width + (cell_width - text_width) / 2
                y_position = y - (i + 1) * cell_height + cell_height/2 - 4
                c.drawString(x_position, y_position, "X" if item else "")
            else:
                text_width = c.stringWidth(str(item), "Helvetica", 8)
                x_position = x + (j + 1) * cell_width + (cell_width - text_width) / 2
                y_position = y - (i + 1) * cell_height + cell_height/2 - 4
                c.drawString(x_position, y_position, str(item))




def points_table(c, data, x, y, cell_width, cell_height):
    c.setFont("Helvetica", 8)
    num_columns = 4
    num_rows = 70

    x += 35
    y += 70

    for offset in range(2):
        
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x + offset * 152 + 20, y + 5, "Équipe A")
        c.drawString(x + offset * 152 + 2 * cell_width + 20, y + 5, "Équipe B")
        c.setFont("Helvetica", 8)
        
        for col in range(1, num_columns - 1):
            for row in range(num_rows):
                value = (offset * 70) + (col - 1) * num_rows + row + 1
                if col == 2:
                    if offset == 0:
                        if row < 70:
                            text_width = c.stringWidth(str(row + 1), "Helvetica", 8)
                            x_position = x + (col + offset * 4) * cell_width + (cell_width - text_width) / 2
                            y_position = y - (row + 1) * cell_height + cell_height/2 - 4
                            c.drawString(x_position, y_position, str(row + 1))
                    else:
                        if row < 70:
                            text_width = c.stringWidth(str(row + 71), "Helvetica", 8)
                            x_position = x + (col + offset * 4) * cell_width + (cell_width - text_width) / 2
                            y_position = y - (row + 1) * cell_height + cell_height/2 - 4
                            c.drawString(x_position, y_position, str(row + 71))
                else:
                    text_width = c.stringWidth(str(value), "Helvetica", 8)
                    x_position = x + (col + offset * 4) * cell_width + (cell_width - text_width) / 2
                    y_position = y - (row + 1) * cell_height + cell_height/2 - 4
                    c.drawString(x_position, y_position, str(value))

        for col in range(num_columns):
            for row in range(num_rows):
                c.rect(x + (col + offset * 4) * cell_width, y - (row + 1) * cell_height, cell_width, cell_height)

 
if __name__ == "__main__":
    generate_feuille_match()
