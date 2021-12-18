# BasicGUI.py

from tkinter import *
from tkinter import ttk  

from datetime import datetime

import csv

#ttk is theme of Tk


GUI = Tk()
GUI.geometry('300x300+700+200')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย โดย คุณริท')


# B1 = Button(GUI,text = 'คำนวณ')
# B1.pack(ipadx=10,ipady=10) 


F1 = Frame(GUI)
F1.place(x=15,y=30)

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event = None):
	expense = v_expense.get()
	unit_price = v_unitprice.get()
	quantity = v_quantity.get()
	amount = int(unit_price)*int(quantity)
	dt = datetime.now()

	# .get() คือ ดึงค่ามาจาก v_expense = StringVar()
	print('รายการ: {}  ราคาต่อหน่วย:  {}   จำนวน: {}  รวมทั้งหมด {}' .format(expense,unit_price,quantity,amount))
	
	# clear ข้อมูลเก่า	
	v_expense.set('')
	v_unitprice.set('')
	v_quantity.set('')


	#บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
	today = datetime.now().strftime('%a')  # Example    days['Mon'] = 'จันทร์'

	#############
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    # !! Added New
	dt = days[today]+'-'+dt    # !! Added New
	#############


	with open ('savedata.csv','a',encoding='utf-8',newline='') as f:
		# with คือ สั่งเปิดไฟล์แล้วปิดอัตโนมัติ
		# 'a' คือ การบันทึกข้อมูลเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
		# newline = ''  ทำให้ข้อมูลไม่มีบรรทัดว่าง
		fw = csv.writer(f) # สร้างฟังก์ชันสำหรับเขียนข้อมูล
		data = [expense,unit_price,quantity,amount,dt]
		fw.writerow(data)

	# ทำให้เเคอเซอร์กลับไปตำแหน่งช่องกรอก E1	
	E1.focus()

# ทำให้สามารถกด enter ได้ 
GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save(event = None) ด้วย


FONT1 = (None,18) # None เปลี่ยนเป็น 'Angsana New'

#----------------- text1 ------------------
L = ttk.Label(F1, text = 'รายการค่าใช้จ่าย', font = FONT1).pack()
v_expense = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1, textvariable = v_expense,font=FONT1)
E1.pack()
#------------------------------------------

#----------------- text2 ------------------
L = ttk.Label(F1, text = 'ราคาต่อหน่วย (บาท/ชิ้น) ', font = FONT1).pack()
v_unitprice = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1, textvariable = v_unitprice,font=FONT1)
E2.pack()
#------------------------------------------

#----------------- text3 ------------------
L = ttk.Label(F1, text = 'จำนวน (ชิ้น) ', font = FONT1).pack()
v_quantity = StringVar() # StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1, textvariable = v_quantity,font=FONT1)
E3.pack()
#------------------------------------------


B2 = ttk.Button(F1,text = 'Save',command=Save)
B2.pack(ipadx=50,ipady=10) 


GUI.mainloop()