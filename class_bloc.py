# objet des différents blocs graphiques suivant le type d algo de tri

from tkinter import *
# from tkinter import ttk
from threading import Thread
import time
from function_decorators import timer

col = ['black','brown','red','orange','yellow','green','blue','purple','grey','white']
taille_frame = 370

# class master, affichage frame, creation des rectangles, fonctions interversions, et tri général
class bloc(Thread):
    def __init__(self, emplacement, couleur, frame, main_window):
        Thread.__init__(self)
        self.terminated = False
        self.nb_b = 150 # nombre de barre
        self.emplacement = emplacement # numero de frame
        self.couleur = couleur #couleur des barres
        self.frame = frame #instance de la frame d'affichage
        self.liste_a_trier = list() #liste a trier
        self.numero_rectangle = list()  # numero_rectangle(i)+1 est le numéro du rectangle en position i
        self.liste_sort_numero_rec = list()  # couple nombre a trier et rectangle correspondant
                                            # numero_rectangle(i)+1 est le numéro du rectangle en position i
        self.main_window = main_window # fenetre principale
        self.canva = Canvas(self.frame)
        self.canva.config(width = taille_frame-10, height= taille_frame-10)
        self.frame.grid(column=self.emplacement[0], row=self.emplacement[1] + 1)
        self.tri_en_cours = True
        self.first_call = True

    def new_rectangle(self, liste):
        self.nb_b = len(liste)  # nombre de barre
        self.liste_a_trier = list(liste) #liste a trier
        self.numero_rectangle = list(range(self.nb_b))
        self.canva.delete("all")
        for i in range(self.nb_b):
            self.numero_rectangle[i]=self.canva.create_rectangle(2 * i+1, self.nb_b * 2 - self.liste_a_trier[i] * 2, 2 * i + 3, self.nb_b * 2 + 10,fill=self.couleur)
            self.numero_rectangle[i] -=1
            self.liste_sort_numero_rec.append((liste[i],self.numero_rectangle[i]))
        self.canva.pack_propagate(0)
        self.canva.grid(column=0,row=0)
        self.main_window.update()


    def inter(self, depart, arrivee): #interverti deux rectangles depart et arrivee (comptage a partir de 1)
        # time.sleep(0.01)
        distance = (arrivee - depart)*2 # 2 unite en x pour une case
        # print(f'depart avant chgt{self.canva.bbox(depart+1)}')
        self.canva.move(self.numero_rectangle[depart]+1, distance,0)
        # print(f'depart apres chgt{self.canva.bbox(depart+1)}')
        # print(f'arrivee avant chgt{self.canva.bbox(arrivee+1)}')
        self.canva.move(self.numero_rectangle[arrivee]+1,-distance,0)
        # print(f'arrivee apres chgt{self.canva.bbox(arrivee+1)}')
        self.main_window.update()
        #intervetir dans la liste
        intermediaire = self.liste_a_trier[arrivee]
        self.liste_a_trier[arrivee]=self.liste_a_trier[depart]
        self.liste_a_trier[depart]=intermediaire
        self.numero_rectangle[arrivee] , self.numero_rectangle[depart] = self.numero_rectangle[depart] , self.numero_rectangle[arrivee]
        # intermediaire = self.numero_rectangle[arrivee]
        # self.numero_rectangle[arrivee]=self.numero_rectangle[depart]
        # self.numero_rectangle[depart]=intermediaire
    def inter_tuple (self, depart, arrivee): #interverti deux rectangles depart et arrivee (comptage a partir de 1)
        distance = (arrivee - depart)*2 # 2 unite en x pour une case
        self.canva.move(self.liste_sort_numero_rec[depart][1]+1, distance,0)
        self.canva.move(self.liste_sort_numero_rec[arrivee][1]+1,-distance,0)
        self.main_window.update()
        #intervetir dans la liste
        self.liste_sort_numero_rec[arrivee] , self.liste_sort_numero_rec[depart] = self.liste_sort_numero_rec[depart] , self.liste_sort_numero_rec[arrivee]

    def inter_image_rec(self,depart,arrivee): #interverti les rectangles numéro départ et numéro arrivée
        # print(f"depart={depart} arrivee = {arrivee}")
        # print(f'depart avant chgt{self.canva.bbox(depart+1)}')
        # print(f'arrivee avant chgt{self.canva.bbox(arrivee+1)}')
        # time.sleep(0.01)
        distance = (self.canva.bbox(arrivee+1)[0]- self.canva.bbox(depart+1)[0])
        self.canva.move(depart + 1, distance, 0)
        self.canva.move(arrivee + 1, -distance, 0)
        self.main_window.update()

    @timer
    def tri(self):
        for j in range(self.nb_b-1):
            for i in range (self.nb_b-1-j):
                time.sleep(0.01)
                if self.liste_a_trier[i]<self.liste_a_trier[i+1]:
                    # print(f"les 2 elements a trier{self.liste_a_trier[i]} et {self.liste_a_trier[i+1]}")
                    self.inter(i,i+1)

    def run(self):
        self.terminated = False
       # while self.terminated == False:
        while self.tri_en_cours == True:
            self.tri()
            self.tri_en_cours = False
        time.sleep(1)

    def stop(self):
        self.terminated = True



# bloc tri JP
class bloc_jp (bloc):
    def __init__(self, emplacement, couleur, frame, main_window):
        bloc.__init__(self, emplacement, couleur, frame, main_window)

    def new_rectangle(self, liste):
        bloc.new_rectangle(self,liste)
        self.canva.create_text((taille_frame-20) // 2, taille_frame - 20, text="JP", fill='black')
        self.main_window.update()


# bloc tri Celian
class bloc_celian (bloc):
    def __init__(self, emplacement, couleur, frame, main_window):
        bloc.__init__(self, emplacement, couleur, frame, main_window)
    def new_rectangle(self, liste):
        bloc.new_rectangle(self,liste)
        self.canva.create_text((taille_frame-20) // 2, taille_frame - 20, text="Celian", fill='black')
        self.main_window.update()

    @timer
    def tri(self):
        indice_min = 0
        for i in range(self.nb_b - 1):
            for j in range (self.nb_b-1-i):
                indice_min=self.nb_b-1-i
                time.sleep(0.01)
                if self.liste_a_trier[indice_min] > self.liste_a_trier[self.nb_b-2-i-j]:
                    indice_min = self.nb_b-2-i-j
                self.inter(indice_min, self.nb_b-1-i)

# class JP_tuple
class bloc_tuple (bloc):
    def __init__(self, emplacement, couleur, frame, main_window):
        bloc.__init__(self, emplacement, couleur, frame, main_window)
    def new_rectangle(self, liste):
        bloc.new_rectangle(self,liste)
        self.canva.create_text((taille_frame-20) // 2, taille_frame - 20, text="Tuple", fill='black')
        self.main_window.update()

    @timer
    def tri(self):
        for j in range(self.nb_b-1):
            for i in range (self.nb_b-1-j):
                time.sleep(0.01)
                if self.liste_sort_numero_rec[i][0]<self.liste_sort_numero_rec[i+1][0]:
                    # print(f"les 2 elements a trier{self.liste_a_trier[i]} et {self.liste_a_trier[i+1]}")
                    self.inter_tuple(i,i+1)
# bloc tri insertion
class bloc_insertion (bloc):
    def __init__(self, emplacement, couleur, frame, main_window):
        bloc.__init__(self, emplacement, couleur, frame, main_window)
    def new_rectangle(self, liste):
        bloc.new_rectangle(self,liste)
        self.canva.create_text((taille_frame-20) // 2, taille_frame - 20, text="insertion", fill='black')
        self.main_window.update()

    @timer
    def tri(self):
        indice_min = 0
        for i in range(self.nb_b):
            for j in range (i):
                time.sleep(0.01)
                if self.liste_a_trier[j] < self.liste_a_trier[i]:
                    for k in range(i-j):
                        self.inter(i,j+k)
                    break


# bloc tri fusion
class bloc_fusion (bloc):
    def __init__(self, emplacement, couleur, frame, main_window):
        bloc.__init__(self, emplacement, couleur, frame, main_window)
    def new_rectangle(self, liste):
        bloc.new_rectangle(self,liste)
        self.canva.create_text((taille_frame-20) // 2, taille_frame - 20, text="Fusion", fill='black')
        self.main_window.update()

    def tri_fusion(self, liste,liste_rect):
        if len(liste)>1:
            midlist = len(liste)//2
            left_side = list(liste[:(midlist)]) #jusqu a indice midlist - 1
            left_side_rec = list(liste_rect[:(midlist)])
            right_side = list(liste[(midlist):]) # a partir de lindice midlist
            right_side_rec = list(liste_rect[(midlist):])
            self.tri_fusion(left_side,left_side_rec)
            self.tri_fusion(right_side,right_side_rec)
            liste_rect[:(midlist)] = list(left_side_rec)
            liste_rect[(midlist):] = list(right_side_rec)

            global_index =0
            left_index = 0
            right_index = 0
            for i in range(midlist):
                # print(f"taille left side {len(left_side)} et midlist {midlist}")
                # print(f"taille right side {len(right_side)} et right_index {right_index}")
                while right_index<len(right_side) and left_side[i]<right_side[right_index]:
                    time.sleep(0.01)
                    liste[global_index]=right_side[right_index]
                    # affichage rectangle
                    # print(f"depart {liste_rect[global_index]} et arrivee {left_side[i]}")
                    self.inter_image_rec(right_side_rec[right_index], liste_rect[global_index]) # insertion du rect a la place de
                    liste_rect[global_index] = right_side_rec[right_index]# celui de gauche
                    j = midlist+right_index
                    liste_rect[j]=left_side_rec[i]
                    while j > global_index+1: # maintenant remettre la global list a sa place juste a droite du nouvel inseré
                        self.inter_image_rec(liste_rect[j],liste_rect[j-1])
                        intermediaire = liste_rect[j]
                        liste_rect[j] = liste_rect[j-1]
                        liste_rect[j-1] = intermediaire
                        j -=1
                        #fin affichage
                    global_index += 1
                    right_index += 1
                liste[global_index] = left_side[left_index]
                liste_rect[global_index] = left_side_rec[left_index]
                global_index+=1
                left_index +=1
            while right_index<len(right_side):
                liste[global_index] = right_side[right_index]
                liste_rect[global_index] = right_side_rec[right_index]
                right_index +=1
                global_index +=1
        else:
            return

    @timer
    def tri(self):
        self.tri_fusion(self.liste_a_trier,self.numero_rectangle)
        return
