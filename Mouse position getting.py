import  os
import  time
import pyautogui as pag
try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  #获取屏幕的尺寸
        print(screenWidth,screenHeight)
        x,y = pag.position()   #获取当前鼠标的位置
        posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
        print(posStr) ###		
        time.sleep(0.5)
        os.system('cls')   #清楚屏幕
except KeyboardInterrupt:
    print('end....')

	
	
'''
import pyautogui
import os

screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)while(1)
a=pyautogui.position()
print(a)
secs_between_keys = 0.1
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)
pyautogui.click(x=1013, y=521, clicks=1,  button='left')
#print(b)
#pyautogui.hotkey('ctrl', 'v') # 粘贴我是粘贴来的你好

try:
    while True:
        x, y = pyautogui.position()
        print(x,y)
    except KeyboardInterrupt:
        print(‘\nExit.’)
		
os.system("pause")
'''