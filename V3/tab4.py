from tkinter import *
#from main import root
#root = Tk()
def create_tab4(tab4):
    def Addition():
        num1 = inputnum1.get('1.0', 'end')
        num2 = inputnum2.get('1.0', 'end')
        Outputnum.delete("1.0", "end")
        try:
            n1 = float(num1)
            n2 = float(num2)
            nb = n1 + n2
            Outputnum.insert(END, f"{nb}\n")
        except ValueError:
            Outputnum.insert(END, "une erreur est survenue.")
    def soustraction():
        num1 = inputnum1.get("1.0", "end")
        num2 = inputnum2.get("1.0", "end")
        Outputnum.delete("1.0", "end")
        try:
            n1 = float(num1)
            n2 = float(num2)
            nb = n1 - n2
            Outputnum.insert(END, f"{nb}\n")
        except ValueError:
            Outputnum.insert(END, "une erreur est survenue.")
    def multiplication():
        num1 = inputnum1.get("1.0", "end")
        num2 = inputnum2.get("1.0", "end")
        Outputnum.delete("1.0", "end")
        try:
            n1 = float(num1)
            n2 = float(num2)
            nb = n1 * n2
            Outputnum.insert(END, f"{nb}\n")
        except ValueError:
            Outputnum.insert(END, "une erreur est survenue.")
    def division():
        
        num1 = inputnum1.get("1.0", "end")
        num2 = inputnum2.get("1.0", "end")
        Outputnum.delete("1.0", "end")
        try:
            n1 = float(num1)
            n2 = float(num2)
            nb = round(n1/n2, 2)
            Outputnum.insert(END, f"{nb}\n")
        except ValueError:
            Outputnum.insert(END, "une erreur est survenue.")
    def clear3():
        Outputnum.delete("1.0", "end")
        inputnum1.delete("1.0", "end")
        inputnum2.delete("1.0", "end")
    #----------------------------------------------------------------
    #page config 
    l3 = Label(tab4, width=30,text = "Indique les nombres pour l'équation", font="Arial").grid(row=0, column=0, columnspan=3, pady=12)

    num1text = Label(tab4, width=18,text = "Numéro 1").grid(row=2, column=0, columnspan=1)
    num2text = Label(tab4, width=18,text = "Numéro 2").grid(row=2, column=1, columnspan=2)
    inputnum1 = Text(tab4, height=2, width=18, bg= "light yellow")
    inputnum1.grid(row=3, column=0, columnspan=1)
    inputnum2 = Text(tab4, height=2, width=18, bg= "light yellow")
    inputnum2.grid(row=3, column=1, columnspan=2)
    addition = Button(tab4,  height = 2,
                    width = 20, 
                    text ="Addition",
                    command = lambda:Addition()).grid(row=4, column=0,columnspan=1)
    Soustraction = Button(tab4,  height = 2,
                    width = 20, 
                    text ="Soustraction",
                    command = lambda:soustraction()).grid(row=4, column=1,columnspan=2)
    Multiplication = Button(tab4,  height = 2,
                    width = 20, 
                    text ="Multiplication",
                    command = lambda:multiplication()).grid(row=5, column=0, columnspan=1)
    Division = Button(tab4,  height = 2,
                    width = 20, 
                    text ="Division",
                    command = lambda:division()).grid(row=5, column=1, columnspan=2)
    Outputnum = Text(tab4, height=2, width=36, bg= "light blue")
    Outputnum.grid(row=6, column=0, columnspan=4,)
    Clear3 = Button(tab4, height = 2,
                    width = 20, 
                    text ="Clear",
                    command = lambda:clear3())
    Clear3.grid(row=7, column=0, columnspan=1)

    