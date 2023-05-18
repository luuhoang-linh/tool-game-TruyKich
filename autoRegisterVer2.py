import time
import pyautogui
import pywinauto
from pywinauto.application import Application

time.sleep(5)

id = 97
soAcc = 4
while (soAcc>=1):
    # ban ngay
    pyautogui.moveTo(1206, 361)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

    # dang ki
    pyautogui.moveTo(772, 253)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

    # tai khoan
    pyautogui.moveTo(745, 380)
    pyautogui.click()
    time.sleep(1)
    account = 'role' + str(id) 
    pyautogui.typewrite(account)
    pyautogui.moveTo(772, 253)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    # mk
    pyautogui.moveTo(745, 470)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('takitorjj')
    time.sleep(1)

    # nhap lai mk
    pyautogui.moveTo(750, 560)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite('takitorjj')
    time.sleep(1)

    # dang ki
    pyautogui.moveTo(750, 650)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    # thoat
    pyautogui.moveTo(1039, 951)
    time.sleep(1)
    pyautogui.click()
    time.sleep(10)

    print(id)
    id+=1
    soAcc-=1
