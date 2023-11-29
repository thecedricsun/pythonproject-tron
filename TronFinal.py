from importlib import resources
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from pickle import *
import pygame
from PIL import ImageTk, Image
import random
import numpy as np
import copy
import time

#################################################################################
#
#   Données de partie
#   0 == vide
#   1 == mur
#   2 ==

Data = [   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,8,0,0,0,0,0,0,8,0,0,0,0,0,0,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,8,1,8,0,0,0,0,8,9,8,0,0,0,0,8,1,8,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
           [1,0,0,1,9,0,0,0,0,0,0,0,0,0,0,0,9,1,0,0,1,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,8,0,0,1,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,8,8,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,1,0,0,1,8,8,8,8,8,8,8,8,8,8,8,8,8,1,0,0,1],
           [1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,1,0,0,1,8,8,8,8,8,8,8,8,8,8,8,8,8,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,1,0,0,1,8,8,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,8,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,1,0,0,1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,1,8,8,1,1,8,8,1,8,8,1,1,8,8,1,0,0,1,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,1,8,8,1,1,8,8,1,8,8,1,1,8,8,1,0,0,1,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,9,0,1,1,1,1,1,1,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,9,0,0,0,0,0,8,1,8,0,0,0,0,8,9,8,0,1,0,0,0,0,0,0,9,1,0,0,0,1,9,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1],
           [1,0,0,1,8,8,1,1,8,8,1,8,8,1,1,8,8,1,0,0,1,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,9,0,1,1,1,1,1,1,0,0,1],
           [1,0,0,1,8,8,1,1,8,8,1,8,8,1,1,8,8,1,0,0,1,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,8,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,1,0,0,1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,1,0,0,1,8,8,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
           [1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,1,0,0,1,8,8,8,8,8,8,8,8,8,8,8,8,8,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,1,0,0,1,8,8,8,8,8,8,8,8,8,8,8,8,8,1,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,8,8,1,0,0,1],
           [1,0,0,1,9,0,0,0,0,0,0,0,0,0,0,0,9,1,0,0,1,0,0,8,1,8,0,0,0,0,8,1,8,0,0,0,0,8,0,0,1,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,0,0,1],
           [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,8,1,8,0,0,0,0,8,9,8,0,0,0,0,8,1,8,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
           [1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,8,0,0,0,0,0,0,8,0,0,0,0,0,0,8,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

GInit = np.array(Data, dtype=np.int32)
GInit = np.flip(GInit, 0).transpose()
game_state = "start"
song = "music/CocoMall.mp3"
player = False

# LARGEUR = 39
LARGEUR = 61
# HAUTEUR = 17
HAUTEUR = 35
# container pour passer efficacement toutes les données de la partie

class Game:
    def __init__(self, Grille, Motos, Score=0):
        self.Score   = Score
        self.Motos = Motos
        self.Grille  = Grille

    def copy(self):
        return copy.deepcopy(self)

Motos = []
randomspawn = [[19, 5], [59, 33], [1, 33], [21, 1], [6, 9], [21, 30], [29, 7], [30, 4], [15, 18], [42,30], [34, 17], [46, 17], [23, 13]]

choix = random.randrange(len(randomspawn))
spawn1 = randomspawn[choix]
randomspawn.remove(spawn1)

choix = random.randrange(len(randomspawn))
spawn2 = randomspawn[choix]
randomspawn.remove(spawn2)

choix = random.randrange(len(randomspawn))
spawn3 = randomspawn[choix]
randomspawn.remove(spawn3)

choix = random.randrange(len(randomspawn))
spawn4 = randomspawn[choix]
randomspawn.remove(spawn4)

Motos.append([spawn1[0], spawn1[1], "blue", 0, False,"",2])
Motos.append([spawn2[0], spawn2[1], "green", 0, False,"",3])
Motos.append([spawn3[0], spawn3[1], "orange", 0, False,"",4])
Motos.append([spawn4[0], spawn4[1], "red", 0, False, "", 5])

GameInit = Game(GInit, Motos)

pygame.mixer.init()

pygame.mixer.music.load(song)
pygame.mixer.music.play(loops = 52)

##############################################################
#
#   création de la fenetre principale  - NE PAS TOUCHER

L = 16  # largeur d'une case du jeu en pixel
largeurPix = LARGEUR * L
hauteurPix = HAUTEUR * L


Window = tk.Tk()
Window.geometry(str(largeurPix)+"x"+str(hauteurPix))   # taille de la fenetre
Window.title("TRONKART PRORIDER")


# création de la frame principale stockant toutes les pages

F = tk.Frame(Window)
F.pack(side="top", fill="both", expand=True)
F.grid_rowconfigure(0, weight=1)
F.grid_columnconfigure(0, weight=1)

# gestion des différentes pages

ListePages = {}
PageActive = 0


def CreerUnePage(id):
    Frame = tk.Frame(F)
    ListePages[id] = Frame
    Frame.grid(row=0, column=0, sticky="nsew")
    return Frame


def AfficherPage(id):
    global PageActive
    PageActive = id
    ListePages[id].tkraise()

Frame0 = CreerUnePage(0)

canvas = tk.Canvas(Frame0, width=largeurPix, height=hauteurPix, bg="black")
canvas.place(x=0, y=0)
canvas.pack()

#   Dessine la grille de jeu - ne pas toucher

# import des visuels du jeu
# map
TP = ImageTk.PhotoImage(Image.open("ressources/TP3.png"))
BRICK = ImageTk.PhotoImage(Image.open("ressources/BRICK.png"))
START = ImageTk.PhotoImage(Image.open("ressources/scenes/supermariotron.jpg"))
MENU = ImageTk.PhotoImage(Image.open("ressources/scenes/player.jpg"))
BEGIN = ImageTk.PhotoImage(Image.open("ressources/scenes/Beginning.jpeg"))
img = ImageTk.PhotoImage(Image.open("ressources/gameover.jpeg"))
COIN = ImageTk.PhotoImage(Image.open("ressources/sprite/coin.png"))

# head
blueHEAD = ImageTk.PhotoImage(Image.open("ressources/sprite/head/blue.png"))
greenHEAD = ImageTk.PhotoImage(Image.open("ressources/sprite/head/green.png"))
pinkHEAD = ImageTk.PhotoImage(Image.open("ressources/sprite/head/pink.png"))
orangeHEAD = ImageTk.PhotoImage(Image.open("ressources/sprite/head/orange.png"))
redHEAD = ImageTk.PhotoImage(Image.open("ressources/sprite/head/red.png"))

# body
blueBODY = ImageTk.PhotoImage(Image.open("ressources/sprite/body/blue.png"))
greenBODY = ImageTk.PhotoImage(Image.open("ressources/sprite/body/green.png"))
pinkBODY = ImageTk.PhotoImage(Image.open("ressources/sprite/body/pink.png"))
orangeBODY = ImageTk.PhotoImage(Image.open("ressources/sprite/body/orange.png"))
redBODY = ImageTk.PhotoImage(Image.open("ressources/sprite/body/red.png"))

def EndScreen(Game):
    canvas.create_rectangle(0,0,LARGEUR*L,HAUTEUR*L,fill="black")
    canvas.create_image(LARGEUR*L//2, HAUTEUR*L//2 -150,image=img,anchor=tk.CENTER)
    h = open ("lastscore","r")
    last = "Last game scores :"
    last += h.read()
    h.close()
    i = open ("MyScore", "r")
    best = "Last Game Score : "
    best += i.read()
    i.close()
    f = open ("lastscore","w")
    g = open ("MyScore", "w" )

    
    SNESFont=tkFont.Font(family="SNES",size="35")
    FontLittle = tkFont.Font(family="SNES",size="25")
    if player:
        canvas.create_text(LARGEUR*L//2, HAUTEUR*L//2 +50,fill="white",text="Your score : "+str(Game.Motos[4][3]),font=SNESFont)
        canvas.create_text(LARGEUR*L//2, HAUTEUR*L//2 +150,fill="white",text=best,font=FontLittle)
        g.write(str(Game.Motos[4][3]))
    else:
        endtext = "SCORES"
        canvas.create_text(LARGEUR*L//2, HAUTEUR*L//2 + 5 ,fill="white",text=endtext,font=SNESFont)
        nb = 40
        for M in Game.Motos:
            endtext = M[2] + ":" + str(M[3])
            canvas.create_text(LARGEUR*L//2, HAUTEUR*L//2 + 10 + nb,fill=M[2],text=endtext,font=SNESFont)
            nb += 40
            f.write(endtext + " ")
        canvas.create_text(LARGEUR*L//2, HAUTEUR*L//2 + 10 + nb,fill="white",text=last,font=FontLittle)
    f.close()
    g.close()

def AfficheStart():
    canvas.create_image(0, 0, image=START, anchor=tk.NW)

def AfficheMenu():
    canvas.create_image(0, 0, image=MENU, anchor=tk.NW)

GPS = np.flip(GInit, 0).transpose()

def Affiche(Game):
    global GPS
    canvas.delete("all")
    H = canvas.winfo_height()

    def DrawCase(x, y, coul):
        # draw image en fct de la couleur
        x*= L
        y*= L
        # canvas.create_rectangle(x, H-y, x+L, H-y-L, fill=coul)

        #body
        if coul == "#b5fffe": #blueBODY
            canvas.create_image(x, H-y-L, image=blueBODY, anchor=tk.NW)
        if coul == "#80ffaa": #greenBODY
            canvas.create_image(x, H-y-L, image=greenBODY, anchor=tk.NW)
        if coul == "#FFC585": #orangeBODY
            canvas.create_image(x, H-y-L, image=orangeBODY, anchor=tk.NW)
        if coul == "#d11346": #redBODY
            canvas.create_image(x, H-y-L, image=redBODY, anchor=tk.NW)
        if coul == "pinkbody": #pinkBODY
            canvas.create_image(x, H-y-L, image=pinkBODY, anchor=tk.NW)
        #body

        #head
        if coul == "blue": #blueHEAD
            canvas.create_image(x, H-y-L, image=blueHEAD, anchor=tk.NW)
        if coul == "green": #greenHEAD
            canvas.create_image(x, H-y-L, image=greenHEAD, anchor=tk.NW)
        if coul == "orange": #orangeHEAD
            canvas.create_image(x, H-y-L, image=orangeHEAD, anchor=tk.NW)
        if coul == "red": #redHEAD
            canvas.create_image(x, H-y-L, image=redHEAD, anchor=tk.NW)
        if coul == "pink": #pinkHEAD
            canvas.create_image(x, H-y-L, image=pinkHEAD, anchor=tk.NW)
        #head

    def DrawBrick(x, y):
        x *= L
        y *= L
        # canvas.create_rectangle(x, H-y, x+L, H-y-L, fill=coul)
        canvas.create_image(x, y, image=BRICK, anchor=tk.NW)

    def DrawCoin(x, y):
        x *= L
        y *= L
        # canvas.create_rectangle(x, H-y, x+L, H-y-L, fill=coul)
        canvas.create_image(x, H-y-L, image=COIN, anchor=tk.NW)

    def DrawTP(x, y):
        global TP, L

        H = canvas.winfo_height()
        x *= L
        y *= L
        canvas.create_image(x, H-y-L, image=TP, anchor=tk.NW)
    

    # dessin des murs

    for x in range (LARGEUR):
       for y in range (HAUTEUR):
            if Game.Grille[x,y] == 1  : 
                DrawBrick(x,y)
            if Game.Grille[x,y] == 2  : 
                DrawCase(x,y,"#b5fffe" )
            if Game.Grille[x,y] == 3  : 
                DrawCase(x,y,"#80ffaa" )
            if Game.Grille[x,y] == 4  : 
                DrawCase(x,y,"#FFC585" )
            if Game.Grille[x,y] == 5  : 
                DrawCase(x,y,"#d11346" )
            if Game.Grille[x,y] == 6  : 
                DrawCase(x,y,"pinkbody" )
            if Game.Grille[x,y] == 8  : 
                DrawCoin(x,y)
            if Game.Grille[x,y] == 9  : 
                DrawTP(x,y)

    # dessin de la moto HEAD
    for M in Game.Motos:
        DrawCase(M[0],M[1],M[2])

###########################################################
#
# gestion du joueur IA

# VOTRE CODE ICI

def Play(Game):
    global GPS
    Sortie = True

    for M in Game.Motos:
        if not M[4]:
            x,y = M[0], M[1]
            if Game.Grille[x, y] != 9:
                Game.Grille[x,y] = M[6]  # laisse la trace de la moto

            #déplacement random
            L = MotosPossibleMove(Game, M[0], M[1])
            if L:
                if M[2] != "pink":
                    if M[2] == "blue":
                        choix = BestMove(Game, L, 10000, M)
                        x += L[choix][0]
                        y += L[choix][1]
                    elif M[2] == "green":
                        choix = BestMove(Game, L, 5000, M)
                        x += L[choix][0]
                        y += L[choix][1]
                    elif M[2] == "orange":
                        choix = BestMove(Game, L, 1000, M)
                        x += L[choix][0]
                        y += L[choix][1]
                    else:
                        choix = BestMove(Game, L, 500, M)
                        x += L[choix][0]
                        y += L[choix][1]
                    
            if player:
                if M[2]=="pink":
                    if M[5]=="bas":y+=-1
                    if M[5]=="droite":x+=1
                    if M[5]=="haut":y+=1
                    if M[5]=="gauche":x+=-1
            
            v = Game.Grille[x,y]

            if v > 0 and v != 9 and v != 8:
                # collision détectée
                M[4] = True # partie terminée pour la moto en question
                
            else :
                M[0] = x  # valide le déplacement
                M[1] = y  # valide le déplacement
                M[3] += 1   # la partie continue
                if v == 8:
                    #ajouter des points en score
                    M[3] += 4

                    # enlever la piece de la Game.Grille
                    Game.Grille[x,y] = 0

                # test

                if testCaseTP(M[0], M[1], Game.Grille):
                    # case TP
                    # il faut mnt TP sur telle case en fct de telle case
                    if ciblageTP(x, y):
                        M[0] = ciblageTP(x, y)[0]

                        M[1] = ciblageTP(x, y)[1]

                if not L:
                    M[4] = True

        if not player:
            for M in Game.Motos:
                if not M[4]:
                    Sortie = False
        else:
            if not Game.Motos[4][4]:
                Sortie = False

    return Sortie


def leftKey(event):
    global CurrenGame
    if player:
        CurrentGame.Motos[4][5]="gauche"
Window.bind('<Left>',leftKey)

def rightKey(event):
    global CurrentGame
    if player:
        CurrentGame.Motos[4][5]="droite"
Window.bind('<Right>',rightKey)

def upKey(event):
    global CurrentGame
    if player:
        CurrentGame.Motos[4][5]="haut"
Window.bind('<Up>',upKey)

def downKey(event):
    global CurrentGame
    if player:
        CurrentGame.Motos[4][5]="bas"
Window.bind('<Down>',downKey)


def testCaseTP(x, y, Grille):
    # return True si (x, y) est sur une case TP
    if Grille[x][y] == 9:
        # case TP
        return True
    else:
        return False
    # else return False


def ciblageTP(x, y):
    # return nouveau (x, y) en fct d'anciens (x, y)

    # 1ere paire __ aller - retour (référence screenshot dans "ressources/referenceTP.png")
    if x == 4 and y == 30:
        return tuple((23, 17))
    if x == 23 and y == 17:
        return tuple((4, 30))

    # 2eme paire __ aller - retour
    if x == 16 and y == 30:
        return tuple((30, 31))
    if x == 30 and y == 31:
        return tuple((16, 30))

    # 3eme paire __ aller - retour
    if x == 37 and y == 17:
        return tuple((47, 17))
    if x == 47 and y == 17:
        return tuple((37, 17))

    # 4eme paire __ aller - retour
    if x == 30 and y == 3:
        return tuple((50, 13))
    if x == 50 and y == 13:
        return tuple((30, 3))

    # 5eme paire __ aller - retour
    if x == 50 and y == 21:
        return tuple((16, 4))
    if x == 16 and y == 4:
        return tuple((50, 21))

    # 6eme paire __ aller - retour
    if x == 53 and y == 17:
        return tuple((4,4))
    if x == 4 and y == 4:
        return tuple((53, 17))

def MotosPossibleMove(Game, motoX, motoY):
    L = []
    x,y = motoX, motoY
    if ( Game.Grille[x  ][y-1] == 0 ) or ( Game.Grille[x  ][y-1] == 9 ) or ( Game.Grille[x  ][y-1] == 8 ): 
        L.append((0,-1))
    if ( Game.Grille[x  ][y+1] == 0 ) or ( Game.Grille[x  ][y+1] == 9 ) or ( Game.Grille[x  ][y+1] == 8 ): 
        L.append((0,1))
    if ( Game.Grille[x+1][y  ] == 0 ) or ( Game.Grille[x+1][y  ] == 9 ) or ( Game.Grille[x+1][y  ] == 8 ): 
        L.append((1,0))
    if ( Game.Grille[x-1][y  ] == 0 ) or ( Game.Grille[x-1][y  ] == 9 ) or ( Game.Grille[x-1][y  ] == 8 ): 
        L.append((-1,0))
    return L

def Simulate(Game, nb, dirx, diry, moto):
    # on copie les datas de départ pour créer plusieurs parties en //
    G = np.tile(Game.Grille, (nb, 1, 1))
    X = np.tile(moto[0] + dirx, nb)
    Y = np.tile(moto[1] + diry, nb)
    S = np.tile(moto[3], nb)
    I = np.arange(nb)  # 0,1,2,3,4,5...
    boucle = True

    # VOTRE CODE ICI

    dx = np.array([0, -1, 0,  1,  0], dtype=np.int32)
    dy = np.array([0,  0, 1,  0, -1], dtype=np.int32)
    ds = np.array([0,  1,  1,  1,  1], dtype=np.int32)

    while(boucle):
        # marque le passage de la moto
        G[I, X, Y] = 1

        # Vgauche = (G[I, X-1, Y] == 0) * 1
        # Vhaut = (G[I, X, Y+1] == 0) * 1
        # Vdroite = (G[I, X+1, Y] == 0) * 1
        # Vbas = (G[I, X, Y-1] == 0) * 1

        if (G[I, X-1, Y] == 0).all():
            Vgauche = 1
        elif (G[I, X-1, Y] == 8).all():
            Vgauche = 1
        elif (G[I, X-1, Y] == 9).all():
            Vgauche = 1
        else :
            Vgauche = 0

        if (G[I, X, Y+1] == 0).all():
            Vhaut = 1
        elif (G[I, X, Y+1] == 8).all():
            Vhaut = 1
        elif (G[I, X, Y+1] == 9).all():
            Vhaut = 1
        else :
            Vhaut = 0

        if (G[I, X+1, Y] == 0).all():
            Vdroite = 1
        elif (G[I, X+1, Y] == 8).all():
            Vdroite = 1
        elif (G[I, X+1, Y] == 9).all():
            Vdroite = 1
        else :
            Vdroite = 0

        if (G[I, X, Y-1] == 0).all():
            Vbas = 1
        elif (G[I, X, Y-1] == 8).all():
            Vbas = 1
        elif (G[I, X, Y-1] == 9).all():
            Vbas = 1
        else :
            Vbas = 0

        LPossibles = np.zeros((nb, 4), dtype=np.int32)
        Tailles = np.zeros(nb, dtype=np.int32)

        LPossibles[I, Tailles] = Vgauche
        Tailles += Vgauche

        LPossibles[I, Tailles] = Vdroite*3
        Tailles += Vdroite

        LPossibles[I, Tailles] = Vhaut*2
        Tailles += Vhaut

        LPossibles[I, Tailles] = Vbas*4
        Tailles += Vbas

        Tailles[Tailles == 0] = 1

        R = np.random.randint(Tailles)
        Choix = LPossibles[I, R]

        SommeScore1 = np.sum(S)

        # DEPLACEMENT
        DX = dx[Choix]
        DY = dy[Choix]
        DS = ds[Choix]
        X += DX
        Y += DY
        S += DS

        SommeScore2 = np.sum(S)
        if SommeScore1 == SommeScore2:
            boucle = False
    return np.mean(S)


def BestMove(Game, L, nb, Moto):
    bestmove = 0
    maxtot = 0

    for i in range (len(L)):
        Game2 = Game.copy()
        Game2.Grille[Moto[0] ,Moto[1]] = Moto[6]
        if Simulate(Game2, nb, L[i][0], L[i][1], Moto ) > maxtot:
            maxtot = Simulate(Game2, nb, L[i][0], L[i][1], Moto )
            bestmove = i

    return bestmove


def StartGame(event):
    global game_state, song, player, CurrentGame
    if event.char == "b":
        if game_state == "start":
            game_state = "menu"
            song = "music/DuckTales.mp3"
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 52)
    elif game_state == "menu":
        if event.char == "y":
            player = True
            CurrentGame.Motos.append([24, 15, "pink", 0, False, "haut", 6])
            game_state = "game"
            song = "music/Rainbow.mp3"
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 52)
        elif event.char == "n":
            game_state = "game"
            song = "music/Rainbow.mp3"
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 52)


Window.bind("<KeyPress>",StartGame)

################################################################################
CurrentGame = GameInit.copy()
cpt = 0


def Partie():
    global game_state, cpt, CurrentGame
    Tstart = time.time()
    if game_state == "start":
        AfficheStart()
        Window.after(100, Partie)
    elif game_state == "menu":
        AfficheMenu()
        Window.after(100, Partie)
    else:
        PartieTermine = Play(CurrentGame)

        if not PartieTermine:
            Affiche(CurrentGame)
            #StartScreen()
            # rappelle la fonction Partie() dans 30ms
            # entre temps laisse l'OS réafficher l'interface
            Window.after(100, Partie)
        else:
            game_state = "end"
            song = "music/Howl.mp3"
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 52)
            EndScreen(CurrentGame)
        cpt += 1
        print(time.time()-Tstart)


#####################################################################################
#
#  Mise en place de l'interface - ne pas toucher

AfficherPage(0)
Window.after(100, Partie)
Window.mainloop()
