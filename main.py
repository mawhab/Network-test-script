import pyautogui
import time

white = (255,255,255)
x,y = 1020,1055 # x and y values for chrome position in toolbar

# opning chrome
pyautogui.click(x=x, y=y)

time.sleep(2)
# opneing a new tab
pyautogui.hotkey('ctrl', 't') 

# going to router web interface
pyautogui.write('192.168.1.1')
pyautogui.press('enter') 

x,y = 1222, 866 # x and y values for internet unavailable message

# moving mouse to required position
pyautogui.moveTo(x,y)

time.sleep(3)

# getting colors of required portion
rgb = pyautogui.screenshot().getpixel((x,y))

# checking if internet is good
while rgb != white:
    pyautogui.click(x=107, y=60) # refreshing page
    pyautogui.moveTo(x,y) # moving back to position
    time.sleep(3)
    rgb = pyautogui.screenshot().getpixel((x,y))

pyautogui.alert(text='Internet is up', title='internet', button='Ok')
