# BasicGUI.py

from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมของฉัน')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image = file,text ='')
IMG.pack()

L1 = Label(GUI,text = 'โปรแกรมคำนวณทุเรียน',font = ('Angsana New',30,'bold'),fg ='green')
L1.pack() #.place(x,y) ,  .grid(row=0,column=0)

L2 = Label(GUI,text = 'กรุณากรอกจำนวนทุเรียน',font = ('Angsana New',20))
L2.pack() #.place(x,y) ,  .grid(row=0,column=0)

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก
E1 = ttk.Entry(GUI,textvariable = v_quantity, font =('impact',30))
E1.pack()

def Calculate():
	quantity = v_quantity.get()
	price = 100
	print('ราคารวม', float(quantity) * price)
	cal = float(quantity) * price
	messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย','ทุเรียนจำนวน {} กิโลกรัม  ราคาทั้งหมด {:,.2f} บาท' .format(quantity,cal))


B1 = ttk.Button(GUI,text = 'คำนวณ',command=Calculate)
B1.pack(ipadx=30, ipady=20,pady=20)  #pady ระยะจากขอบปุ่มไปยังตัวที่อยู่ด้านบน

GUI.mainloop()