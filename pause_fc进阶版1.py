#coding=utf-8
import os
import pyperclip
s=pyperclip.paste()#将剪贴板缓冲区内容保存为字符串变量
print('原路径是：')
print(s)
x=list(s)#字符串转为list
def change(chr):
    if chr=='\\':
        chr='/'
    return chr   
m=list(map(change,x))     
s="".join(m)#
pyperclip.copy(s)#将修改后的内容复制进剪贴板缓冲区，用于粘贴操作
print('\n修改后的路径是：')
print("**********************************")
print('\n')
print(s)
print('\n')
print("**********************************")
print('内容已添加到粘贴板，可直接粘贴\*_*/')
print('\n'*2)
os.system("pause")