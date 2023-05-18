import time
import pyautogui
import pywinauto
from pywinauto.application import Application

# =================================================================

# sử dụng thư viện pyautowin để thao tác với các cửa sổ window
# sử dụng thư viện pyautogui để thao tác với chuột và bàn phím 

# =================================================================

# khởi tạo đối tượng TruyKich
truyKich = pywinauto.Application()

# mở game bằng đường dẫn tuyệt đối
def gotoGame():
    truyKich.start("D:\\TruyKich\\WDlauncher.exe")

# điền tài khoản mật khẩu + nhấn enter
def accAndPass(id):
    if int(id) <= 58:
        password = 'takitorj'
    elif int(id) >= 59 and int(id) <= 78 :
        password = 'takitorj@a'
    elif int(id) >= 79 and int(id) <= 100 :
        password = 'takitorj@b'
    elif int(id) >= 101 and int(id) <= 128 :
        password = 'takitorj@c'
    elif int(id) >= 157 and int(id) <= 169 :
        password = 'takitorj@f'
    pyautogui.moveTo(600, 600)
    pyautogui.click()
    account = 'role20' + id
    pyautogui.typewrite(account)
    time.sleep(1)
    pyautogui.moveTo(600, 635)
    pyautogui.click()
    pyautogui.typewrite(password)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

# chọn server
def serverNorth():
    pyautogui.moveTo(850, 560)
    pyautogui.click()

# click tạo nhân vật
def createName():
    pyautogui.moveTo(1170, 400)
    pyautogui.click()

# tắt cửa sổ game
def closeTruyKich():
    truyKich2 = Application().connect(path="D:\\TruyKich\\WDlauncher.exe")
    truyKich2.kill()
    pyautogui.moveTo(1901, 15)
    time.sleep(1)
    pyautogui.click()


# =================================================================

# acc role2001 thì id sẽ là 1
id = 1

# skip_indexes là các id của acc đã bán
def check(id):
    skip_indexes = [3, 4, 7, 8, 10, 12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    if id in skip_indexes:
        return 1
    else:
        return 0
                    

time.sleep(3)

# vòng lặp while giúp chạy từ id = 1 đến id mà mình muốn, t có 31 acc nên sẽ chạy đến 31
# nếu id mà trùng với id trong số acc đã bán thì id tăng 1 và vòng lặp bỏ qua id hiện tại
# nếu id không trùng thì chạy đoạn code autologin và print ra id đế check
while (id <= 27):
    if check(id) == 1:
        pass
    else:
        gotoGame()
        time.sleep(10)
        id_str = str(id).zfill(2)
        accAndPass(id_str)
        time.sleep(1)
        serverNorth()
        time.sleep(6)
        createName()
        time.sleep(30)
        closeTruyKich()
        time.sleep(5)
        print(id)
    id+=1

