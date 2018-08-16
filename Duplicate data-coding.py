#coding=utf-8
import os
file_handle=open('TR.txt',mode='w')
count=0
while True: 
	st='#'+'mytd'+str(count)+'{'
	file_handle.write(st)
	file_handle.write('\n')
	file_handle.write('height:10px; \n')
	file_handle.write('width:10px; \n')
	file_handle.write('background:#ccc; \n')
	file_handle.write('padding:0px; \n')
	file_handle.write('margin:0px; \n')
	file_handle.write('} \n')
	count+=1
	if count == 220:
		break
file_handle.close()
print('写入数据成功')
os.system("pause")