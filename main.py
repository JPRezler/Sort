# test de différents algorithmes de tri et visualisation graphique
# utilisation de classes, recursivité et multithread

import time
import random
from tkinter import *
from tkinter import ttk
from class_bloc import *
import logging

# configuration logging
logging.basicConfig(level=logging.DEBUG)

# creation de la fenetre principale
root = Tk()
root.title('tri')
root.geometry('1200x800')

#label
Label(root,text = 'Nombre de barres:').grid(column=0,row=0)

#entry pour le nombre de barre
nb_barre_string = StringVar()
nb_barres = ttk.Entry(root, textvariable=nb_barre_string)
nb_barres.grid(column=1,row=0)

# les frame de tri



#fonction liée au bouton
def chgt():
    frame_tri = []
    for nb_frame in range(6):
        frameUL = Frame(root, highlightbackground="red", highlightthickness=1, width=taille_frame, height=taille_frame,
                        bd=0)
        frameUL.grid_propagate(0)
        r = ((nb_frame) // 3)
        c = (nb_frame) % 3
        logging.debug(f"creation de la classe bloc colonne {c} et rang {r}")
        if nb_frame == 0:
            frame_tri.append(bloc_celian([c, r], col[nb_frame], frameUL, root))
        elif nb_frame == 1:
            frame_tri.append(bloc_jp([c, r], col[nb_frame], frameUL, root))
        elif nb_frame == 2:
            frame_tri.append(bloc_insertion([c, r], col[nb_frame], frameUL, root))
        elif nb_frame == 3:
            frame_tri.append(bloc_fusion([c, r], col[nb_frame], frameUL, root))
        elif nb_frame == 4:
            frame_tri.append(bloc_tuple([c, r], col[nb_frame], frameUL, root))
        else:
            frame_tri.append(bloc([c, r], col[nb_frame], frameUL, root))
    nb_barre = min(int(nb_barre_string.get()),170)
    a = list(range(nb_barre))

    for nb_frame in range(6):
        random.shuffle(a)
        frame_tri[nb_frame].new_rectangle(a)
        if frame_tri[nb_frame].first_call == True:
            frame_tri[nb_frame].tri_en_cours = True
            frame_tri[nb_frame].start()
            frame_tri[nb_frame].first_call = False
        else:
            frame_tri[nb_frame].tri_en_cours = True

def fermeture():# faire une fermeture des threads
    sys.exit()
    root.destroy()
    return

# button
button = Button(root, text = 'lancez!', command = chgt)
button.grid(column = 2,row = 0)

# main program
nb_barres.focus()
root.protocol("WM_DELETE_WINDOW", fermeture)
root.bind("<Return>", chgt)
root.mainloop()

