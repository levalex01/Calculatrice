from tkinter import *
#from main import root
import emoji
#root = Tk()
def create_tab2(tab2):
    def clear1():
        Output1.delete("1.0", "end-1c")
        inputtxt1.delete("1.0", "end-1c")

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

    