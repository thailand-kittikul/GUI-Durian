# BasicGUI_HomeWork.py

from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมของฉัน')

file = PhotoImage(file='ดัมเบล.png')
IMG = Label(GUI,image = file,text ='')
IMG.pack()

L1 = Label(GUI,text = 'โปรแกรมคำนวณราคาดัมเบล',font = ('Angsana New',40,'bold'),fg ='red')
L1.pack() #.place(x,y) ,  .grid(row=0,column=0)

L2 = Label(GUI,text = 'กรุณากรอกจำนวนดัมเบล (ชุด)',font = ('Angsana New',25))
L2.pack() #.place(x,y) ,  .grid(row=0,column=0)

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก
E1 = ttk.Entry(GUI,textvariable = v_quantity, font =('impact',30))
E1.pack()

def Calculate():
	quantity = v_quantity.get()
	price = 800
	amount = float(quantity) * price
	print('ราคาต่อหน่วย {} บาท/ชุด ราคารวม {} บาท'.format(price,amount))
	cal = float(quantity) * price
	
	# ฟังห์ชั่นบันทึกข้อมูลลง file.txt
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'ดัมเบล: {} เซ็ท  เป็นเงิน {} บาท'.format(quantity,amount))

	# pop up
	messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย','ดัมเบลจำนวน {} ชุด  ราคาทั้งหมด {:,.1f} บาท' .format(quantity,cal))


B1 = ttk.Button(GUI,text = 'คำนวณ',command=Calculate)
B1.pack(ipadx=30, ipady=20,pady=20)  #pady ระยะจากขอบปุ่มไปยังตัวที่อยู่ด้านบน


GUI.mainloop()