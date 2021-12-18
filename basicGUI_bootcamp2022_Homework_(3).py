# BasicGUI_HomeWork.py

from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import csv
#################################

def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) # บวกเป็นปี พ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	
	return stamp		


def writetext(quantity, total):
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) # บวกเป็นปี พ.ศ.
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'วัน-เวลา: {} ดัมเบล: {} เซ็ท  เป็นเงิน {} บาท'.format(stamp,quantity,total))

def writecsv(data):
	# data = ['Time',10,500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('csv Success !')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	result = readcsv()
	sumlist_quan =[]
	sumlist_total =[]
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return (sumquan, sumtotal)


#################################

GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมสำหรับแม่ค้า v.0.0.1')

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

def Calculate(event=None):
	quantity = v_quantity.get()
	price = 800
	amount = float(quantity) * price
	print('ราคาต่อหน่วย {} บาท/ชุด ราคารวม {} บาท'.format(price,amount))
	cal = float(quantity) * price
	
	stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


	data = [timestamp(thai=False),quantity,cal]
	writecsv(data)


	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text ='ดัมเบลจำนวน {} ชุด  ราคาทั้งหมด {:,.2f} บาท' .format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('') # clear
	E1.focus()


B1 = ttk.Button(GUI,text = 'คำนวณ',command=Calculate)
B1.pack(ipadx=30, ipady=20,pady=20)  #pady ระยะจากขอบปุ่มไปยังตัวที่อยู่ด้านบน

E1.bind('<Return>',Calculate)

def SummaryData(event):

	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text ='จำนวนที่ขายได้: {} ลูก\nยอดขาย:{:,.2f}บาท' .format(sm[0],sm[1])
	messagebox.showinfo(title,text)


GUI.bind('<F1>',SummaryData)
GUI.bind('<F2>',SummaryData)

E1.focus() # ให้เคอเซอร์ไปยังตำแหน่งของ E1
GUI.mainloop()