from tkinter import *
#from main import root
import emoji
#root = Tk()
def create_tab3(tab3):
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

    def clear2():
        Output2.delete("1.0", "end-1c")
        inputtxt2.delete("1.0", "end-1c")
        l2 = Label(tab3, text = "Quelle est la masse ?").grid(row=1, column=1, columnspan=2)
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

    