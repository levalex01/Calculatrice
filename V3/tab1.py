from tkinter import *
def create_tab1(tab1):
    space = Label(tab1)
    intro = Label(tab1, text="Bienvenue sur la page d'acceuil.")
    info= Label(tab1, text="Dans cette application")
    info2 = Label(tab1, text ="vous aurez accès à une calculatrice complette.")
    space.pack()
    intro.pack()
    info.pack()
    info2.pack()