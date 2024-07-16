from tkinter import *
from tkinter import ttk
from tab1 import create_tab1
from tab2 import create_tab2
from tab3 import create_tab3
from tab4 import create_tab4
from tab5 import create_tab5
import emoji

root = Tk()
root.geometry("300x410")
root.title(" Calculatrice ")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Intro')
tabControl.add(tab2, text='Degrée')
tabControl.add(tab3, text='Masse')
tabControl.add(tab4, text='Calculatrice')
tabControl.add(tab5, text="Volume")
tabControl.pack(expand=1, fill="both")

create_tab1(tab1)
create_tab2(tab2)
create_tab3(tab3)
create_tab4(tab4)
create_tab5(tab5)

#-----------------------------------------------
# Close tab
exit_button1 = Button(tab2, height = 2,
                    width = 20,  text="Exit", command=root.destroy).grid(row=7, column=2)
exit_button2 = Button(tab3, height = 2,
                    width = 20,  text="Exit", command=root.destroy).grid(row=5, column=2)
exit_button3 = Button(tab4, height = 2,
                    width = 20,  text="Exit", command=root.destroy).grid(row=7, column=1, columnspan=2)

root.bind("<Escape>", lambda event: root.destroy()) # Touche sur le clavier pour fermer l'application

root.mainloop()
