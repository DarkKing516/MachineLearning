import pyautogui
import webbrowser as web
from time import sleep

web.open("https://web.whatsapp.com/send?phone=+573002568694")
sleep(10)

with open("ext.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        sleep(1)
        pyautogui.press("enter")

# for i in range(10):
#     pyautogui.typewrite("a")
#     pyautogui.press("enter")

# a = 0
# for i in range(10):
#     a += 1
#     b = str(a)
#     pyautogui.typewrite(b)
#     pyautogui.press("enter")
#     # print(b)