# BasicGUI_HomeWork.py

from tkinter import *
from tkinter import ttk  

#ttk is theme of Tk


GUI = Tk()
GUI.geometry('300x300+100+300')
GUI.title('โปรแกรมของฉัน')


# B1 = Button(GUI,text = 'คำนวณ')
# B1.pack(ipadx=10,ipady=10) 


F1 = Frame(GUI)
F1.place(x=15,y=45)

B2 = ttk.Button(F1,text = 'คำนวณ')
B2.pack(ipadx=50,ipady=10) 


GUI.mainloop()