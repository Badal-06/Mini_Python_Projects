import pyautogui
import time
message=5
while message>0:
    time.sleep(2)
    pyautogui.typewrite("hello")
    time.sleep(2)
    pyautogui.press('enter')
    message-=1
