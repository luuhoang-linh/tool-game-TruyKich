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
    if int(id) <= 68:
        password = 'takitorj1'
    elif int(id) > 58 and int(id) <= 78 :
        password = 'takitorj@a'
    elif int(id) > 78 and int(id) <= 100 :
        password = 'takitorj@b'
    elif int(id) > 100 and int(id) <= 156 :
        password = 'takitorj@c'
    elif int(id) > 156 and int(id) <= 200 :
        password = 'takitorj@f'
    pyautogui.moveTo(600, 600)
    pyautogui.click()
    account = 'role' + str(id)
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
id = 65

# skip_indexes là các id của acc đã bán

time.sleep(3)

# vòng lặp while giúp chạy từ id = 1 đến id mà mình muốn, t có 31 acc nên sẽ chạy đến 31
# nếu id mà trùng với id trong số acc đã bán thì id tăng 1 và vòng lặp bỏ qua id hiện tại
# nếu id không trùng thì chạy đoạn code autologin và print ra id đế check
while (id <= 68):
    gotoGame()
    time.sleep(5)
    accAndPass(id)
    time.sleep(1)
    serverNorth()
    time.sleep(6)
    createName()
    time.sleep(20)
    closeTruyKich()
    time.sleep(5)
    print(id)
    id+=1

