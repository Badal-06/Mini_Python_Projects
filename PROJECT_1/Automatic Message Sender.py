import pyautogui
import time

# Enter how many time you want to send message
message_time=int(input("Enter time , You want to send message:  "))

# Enter Your Message
Message=input("Enter Your Message :")

while message_time>0:
    time.sleep(2)
    pyautogui.typewrite(Message)
    time.sleep(2)
    pyautogui.press('enter')
    message_time-=1
