import tkinter as tk
from tkinter import *
from tkinter import ttk
def create_tab5(tab5):
    def on_select():
        selected_value = selected_option.get()
        execute_action(selected_value)
    def execute_action(selected_value):
        #------------------------------------------------------------
        # mL to L
        if selected_value == "mL to L":
            INPUT = inputvolume.get("1.0", "end")
            output.delete("1.0", "end")
            try:
                ml = float(INPUT)
                L = round(ml/1000, 4)
                output.insert(END, f"le volume est de {L} Litre\n")
            except ValueError:
                output.insert(END, f"une erreur est survenue\n")

        #-------------------------------------------------------------
        # L to mL
        elif selected_value == "L to mL":
            INPUT = inputvolume.get("1.0", "end")
            output.delete("1.0", "end")
            try:
                L = float(INPUT)
                mL = round(L*1000, 4)
                output.insert(END, f"le volume est de {mL} mL\n")
            except ValueError:
                output.insert(END, f"une erreur est survenue\n")

        #------------------------------------------------------------
        # mL to Oz
        elif selected_value == "mL to Oz":
            INPUT = inputvolume.get("1.0", "end")
            output.delete("1.0", "end")
            try:
                ml = float(INPUT)
                oz = round(ml/29.574, 4)
                output.insert(END, f"le volume est de {oz} Once (oz)\n")
            except ValueError:
                output.insert(END, f"une erreur est survenue\n")
        #-----------------------------------------------------------
        # Oz to mL
        elif selected_value == "Oz to mL":
            INPUT = inputvolume.get("1.0", "end")
            output.delete("1.0", "end")
            try:
                oz = float(INPUT)
                ml = round(oz*29.574)
                output.insert(END, f"le volume est de {ml} Once (oz)\n")
            except ValueError:
                output.insert(END, f"une erreur est survenue\n")
        #----------------------------------------------------------
        # mL to CM³
        elif selected_value == "mL to Cm³":
            INPUT = inputvolume.get("1.0", "end")
            output.delete("1.0", "end")
            try:
                ml = float(INPUT)
                cm = round(ml)
                output.insert(END, f"le volume est de {cm} Cm³\n")
            except ValueError:
                output.insert(END, f"une erreur est survenue\n")
        #--------------------------------------------------------
        # cm to ml
        elif selected_value == "Cm³ to mL":
            INPUT = inputvolume.get("1.0", "end")
            output.delete("1.0", "end")
            try:
                cm = float(INPUT)
                ml = round(cm)
                output.insert(END, f"le volume est de {ml} mL\n")
            except ValueError:
                output.insert(END, f"une erreur est survenue\n")
        else:
            output.insert(END, "Aucune action définie pour cette option")

    
    selected_option = tk.StringVar()
    
    options = ["Non selectionner","mL to L", "L to mL", "mL to Oz","Oz to mL", "mL to Cm³", "Cm³ to mL" ]
    selected_option.set(options[0])
    
    l1 = Label(tab5,text="Indique le volume à transformer.", font="Arial").grid(row=0, column=1, columnspan=2)
    dropdown = ttk.OptionMenu(tab5, selected_option, *options)
    dropdown.grid(row=2,column=1,columnspan=2)


    # Ajout d'un bouton pour exécuter l'action en fonction de la valeur sélectionnée
    execute_button = ttk.Button(tab5, text="Exécuter", command=on_select)
    execute_button.grid(row=3,column=1, columnspan=2)
    inputvolume = Text(tab5, height=2,
                            width = 30,
                            bg = "light yellow",)
    inputvolume.grid(row=1, column=1, columnspan=2)
    output = Text(tab5,height=10,
                        width = 30, 
                    bg = "light cyan")
    output.grid(row=4, column=1, columnspan=2)
    def clear2():
        inputvolume.delete("1.0", "end-1c")
        output.delete("1.0", "end-1c")
    Clear2 = Button(tab5, height = 2,
                    width = 20, 
                    text ="Clear",
                    command = lambda:clear2())
    Clear2.grid(row=5, column=1)