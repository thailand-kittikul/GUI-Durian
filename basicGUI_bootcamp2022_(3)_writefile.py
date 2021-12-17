# writefile.py
from datetime import datetime


def writetext(quantity, total):
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) # บวกเป็นปี พ.ศ.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'วัน-เวลา: {} ดัมเบล: {} เซ็ท  เป็นเงิน {} บาท'.format(stamp,quantity,total))


# writetext(90,9000)
# writetext(90,9100)
# writetext(90,9200)
# writetext(90,9300)