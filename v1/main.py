from tkinter import *
from tkinter import ttk
import emoji

root = Tk()
root.geometry("300x410")
root.title(" Calculatrice ")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Intro')
tabControl.add(tab2, text='Degrée')
tabControl.add(tab3, text='Masse')
tabControl.pack(expand=1, fill="both")

#----------------------------------------
# Clear les espaces de texte
def clear1():
    Output1.delete("1.0", "end-1c")
    inputtxt1.delete("1.0", "end-1c")

def clear2():
    Output2.delete("1.0", "end-1c")
    inputtxt2.delete("1.0", "end-1c")
#---------------------------------------
def Kg_to_Lb2():
    INPUT = inputtxt2.get("1.0", "end-1c")
    try:
        kg = float(INPUT)
        lb = round(kg * 2.205, 2)
        Output2.insert(END, f"Le poids est de {lb} LB\n")
    except ValueError:
        Output2.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def Lb_to_Kg2():
    INPUT = inputtxt2.get("1.0", "end-1c")
    try:
        lb = float(INPUT)
        kg = round(lb / 2.205, 2)
        Output2.insert(END, f"Le poids est de {kg} Kg\n")
    except ValueError:
        Output2.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))
#---------------------------------------
# Défénition de variable pour la 
# conversion entre C to F & F to C & C to K & K to C & F to K & K to F

def C_to_F1():
    INPUT = inputtxt1.get("1.0", "end-1c")
    Output1.delete("1.0", "end-1c")
    try:
        C = float(INPUT)
        F = round((C * 9/5) + 32, 2)
        Output1.insert(END, f"Le degrée de température est de {F} ° Fahrenheit\n")
    except ValueError:
        Output1.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def F_to_C1():
    INPUT = inputtxt1.get("1.0", "end-1c")
    Output1.delete("1.0", "end-1c")
    try:
        F = float(INPUT)
        C = round((F - 32) * 5/9, 2)
        Output1.insert(END, f"Le degrée de température est de {C} ° Celsuis\n")
    except ValueError:
        Output1.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))
def C_to_K1():
    INPUT = inputtxt1.get("1.0", "end-1c")
    Output1.delete("1.0", "end-1c")
    try:
        C = float(INPUT)
        K = round(C + 273.15, 2)
        Output1.insert(END, f"Le degrée de température est de {K} ° Kelvin\n")
    except ValueError:
        Output1.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def K_to_C1():
    INPUT = inputtxt1.get("1.0", "end-1c")
    Output1.delete("1.0", "end-1c")
    try:
        K = float(INPUT)
        C = round(K - 273.15, 2)
        Output1.insert(END, f"Le degrée de température est de {C} ° Celsius\n")
    except ValueError:
        Output1.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))
def F_to_K1():
    INPUT = inputtxt1.get("1.0", "end-1c")
    Output1.delete("1.0", "end-1c")
    try:
        F = float(INPUT)
        K = float(round((F - 32) * 5/9 + 273.15, 2))
        Output1.insert(END, f"Le degrée de température est de {K} ° Kelvin\n")
    except ValueError:
        Output1.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def K_to_F1():
    INPUT = inputtxt1.get("1.0", "end-1c")
    Output1.delete("1.0", "end-1c")
    try:
        K = float(INPUT)
        F = float(round((K - 273.15) * 9/5 + 32, 2))
        Output1.insert(END, f"Le degrée de température est de {F} ° Celsius\n")
    except ValueError:
        Output1.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))


#--------------------------------------
#Deffinition variable exit
def exit1():
    root.destroy()
def exit2():
    root.destroy()
#-------------------------------------

#--------------------------------------------------------------------------
#tab1

space = Label(tab1)
intro = Label(tab1, text="Bienvenue sur la page d'acceuil.")
info= Label(tab1, text="Dans cette application")
info2 = Label(tab1, text ="vous aurez accès à une calculatrice complette.")
space.pack()
intro.pack()
info.pack()
info2.pack()
#-----------------------------------------------------------------------
# tab2
l1 = Label(tab2, text = "Quelle est le degrée de température",).grid(row=0, column=1, columnspan=2)

inputtxt1 = Text(tab2, height=2,
                width = 30,
                bg = "light yellow",)

inputtxt1.grid(row=2, column=1, columnspan=2)

 
c_to_f1 = Button(tab2,  height = 2,
                 width = 20, 
                 text ="Celsius à fahrenheit",
                 command = lambda:C_to_F1()).grid(row=3, column=1)
f_to_c1 = Button(tab2, height = 2,
                 width = 20, 
                 text ="Fahrenheit à Celsius",
                 command = lambda:F_to_C1()).grid(row=3, column=2)
c_to_k1 = Button(tab2, height = 2,
                 width = 20, 
                 text ="Celsius à Kelvin",
                 command = lambda:C_to_K1()).grid(row=4, column=1)
k_to_c1 = Button(tab2, height = 2,
                 width = 20, 
                 text ="Kelvin à Celsius",
                 command = lambda:K_to_C1()).grid(row=4, column=2)
k_to_f1 = Button(tab2, height = 2,
                 width = 20, 
                 text ="Kelvin à fahrenheit",
                 command = lambda:K_to_F1()).grid(row=5, column=1)
f_to_k1 = Button(tab2, height = 2,
                 width = 20, 
                 text ="Fahrenheit à Kelvin",
                 command = lambda:F_to_K1()).grid(row=5, column=2)

Output1 = Text(tab2,height=10,
                width = 30, 
              bg = "light cyan")
Output1.grid(row=6, column=1, columnspan=2)

Clear1 = Button(tab2, height = 2,
                 width = 20, 
                 text ="Clear",
                 command = lambda:clear1()).grid(row=7, column=1)

exit_button1 = Button(tab2, height = 2,
                 width = 20,  text="Exit", command=root.destroy).grid(row=7, column=2)
#----------------------------------------------------------------------------------------
# tab3
l2 = Label(tab3, text = "Quelle est la masse ?").grid(row=1, column=1, columnspan=2)

inputtxt2 = Text(tab3, height=2,
                width = 30,
                bg = "light yellow",)
inputtxt2.grid(row=2, column=1, columnspan=2)

 
Kg_to_lb2 = Button(tab3, height = 2,
                 width = 20, 
                 text ="Kg à Lb",
                 command = lambda:Kg_to_Lb2()).grid(row=3, column=1)

lb_to_kg2 = Button(tab3, height = 2,
                 width = 20, 
                 text ="Lb à Kg",
                 command = lambda:Lb_to_Kg2()).grid(row=3, column=2)

Output2 = Text(tab3, height = 10, 
              width = 30, 
              bg = "light cyan")
Output2.grid(row=4, column=1,columnspan=2)
Clear2 = Button(tab3, height = 2,
                 width = 20, 
                 text ="Clear",
                 command = lambda:clear2())
Clear2.grid(row=5, column=1)

exit_button2 = Button(tab3, height = 2,
                 width = 20,  text="Exit", command=root.destroy).grid(row=5, column=2)
#------------------------------------------------------------------------------------------

# Commande global

root.bind("<Escape>", lambda event:exit()) # Touche sur le clavier pour faire l'application


mainloop()
