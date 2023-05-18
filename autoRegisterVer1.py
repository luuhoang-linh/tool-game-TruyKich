import time
import pyautogui
import pywinauto
from pywinauto.application import Application

time.sleep(5)

id = 1
soAcc = 50
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
    pyautogui.click()
    id_str = str(id).zfill(2)
    account = 'role' + id_str 
    pyautogui.typewrite(account)
    time.sleep(3)

    # mk
    pyautogui.moveTo(745, 470)
    time.sleep(1)
    pyautogui.click()
    pyautogui.typewrite('takitorj1')
    time.sleep(1)

    # nhap lai mk
    pyautogui.moveTo(750, 560)
    time.sleep(1)
    pyautogui.click()
    pyautogui.typewrite('takitorj1')
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
