# GUIBasic.py

from tkinter import * # จากแพ็กชื่อ tkinterให้ดึงฟังก์ชันมาทั้งหมด

GUI = Tk() # สร้างGUIขึ้นแล้วดึงฟังก์ชันของTk()ทีตัวใหญ่ เคตัวเล็ก 
GUI.geometry('500x500')

L = Label(GUI,text='Hello World!',font=(None,50))
L.pack()

L = Label(GUI,text='Hello World!',font=(None,50))
L.pack()

L = Label(GUI,text='Hello World!',font=(None,50))
L.pack()


# Label คือข้อความของโปรแกรม (L ตัวใหญ่)

GUI.mainloop()
