from tkinter import *
def create_tab5(tab5):
    l1 = Label(tab5,text="Indique le volume à transformer.", font="Arial").grid(row=0, column=1, columnspan=2)
    #-------------------------------------------------------
    # inputvolume
    inputvolume = Text(tab5, height=2,
                        width = 30,
                        bg = "light yellow",)
    inputvolume.grid(row=2, column=1, columnspan=2)
    #-------------------------------------------------------
    #ml to l
    def ml_to_L():
        INPUT = inputvolume.get("1.0", "end")
        output.delete("1.0", "end")
        try:
            ml = float(INPUT)
            L = round(ml/1000, 4)
            output.insert(END, f"le volume est de {L} Litre\n")
        except ValueError:
            output.insert(END, f"une erreur est survenue\n")
    Ml_to_l = Button(tab5,  height = 2,
                    width = 20, 
                    text ="mL à L",
                    command = lambda:ml_to_L()).grid(row=3, column=1)
    #------------------------------------------------------------------
    # L to mL
    def l_to_ml():
        INPUT = inputvolume.get("1.0", "end")
        output.delete("1.0", "end")
        try:
            L = float(INPUT)
            mL = round(L*1000, 4)
            output.insert(END, f"le volume est de {mL} Litre\n")
        except ValueError:
            output.insert(END, f"une erreur est survenue\n")
    L_to_mL = Button(tab5,  height = 2,
                    width = 20, 
                    text ="L to mL",
                    command = lambda:l_to_ml()).grid(row=3, column=2)
    #----------------------------------------------------------
    # ml to oz
    def ml_to_oz():
        INPUT = inputvolume.get("1.0", "end")
        output.delete("1.0", "end")
        try:
            ml = float(INPUT)
            oz = round(ml/29.574, 4)
            output.insert(END, f"le volume est de {oz} Once (oz)\n")
        except ValueError:
            output.insert(END, f"une erreur est survenue\n")
    ml_to_Oz = Button(tab5,  height = 2,
                    width = 20, 
                    text ="mL to oz",
                    command = lambda:ml_to_oz()).grid(row=4, column=1)
    #----------------------------------------------------------
    # oz to ml
    def oz_to_ml():
        INPUT = inputvolume.get("1.0", "end")
        output.delete("1.0", "end")
        try:
            oz = float(INPUT)
            ml = round(oz*29.574)
            output.insert(END, f"le volume est de {ml} Once (oz)\n")
        except ValueError:
            output.insert(END, f"une erreur est survenue\n")
    Oz_to_ml = Button(tab5,  height = 2,
                    width = 20, 
                    text ="oz to mL",
                    command = lambda:oz_to_ml()).grid(row=4, column=2)
    #----------------------------------------------------------
    # ml to cm³
    def ml_to_cm():
        INPUT = inputvolume.get("1.0", "end")
        output.delete("1.0", "end")
        try:
            ml = float(INPUT)
            cm = round(ml)
            output.insert(END, f"le volume est de {cm} Cm³\n")
        except ValueError:
            output.insert(END, f"une erreur est survenue\n")
    mL_to_cm = Button(tab5,  height = 2,
                    width = 20, 
                    text ="mL to cm³",
                    command = lambda:ml_to_cm()).grid(row=5, column=1)
    #----------------------------------------------------------
    # m
    def cm_to_ml():
        INPUT = inputvolume.get("1.0", "end")
        output.delete("1.0", "end")
        try:
            cm = float(INPUT)
            ml = round(cm)
            output.insert(END, f"le volume est de {ml} mL\n")
        except ValueError:
            output.insert(END, f"une erreur est survenue\n")
    cM_to_ml = Button(tab5,  height = 2,
                    width = 20, 
                    text ="Cm³ to mL",
                    command = lambda:cm_to_ml()).grid(row=5, column=2)
    #----------------------------------------------------------
    # output
    output = Text(tab5,height=10,
                    width = 30, 
                bg = "light cyan")
    output.grid(row=8, column=1, columnspan=2)
    