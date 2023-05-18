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
    pyautogui.moveTo(600, 600)
    pyautogui.click()
    account = 'role20' + id
    pyautogui.typewrite(account)
    time.sleep(1)
    pyautogui.moveTo(600, 635)
    pyautogui.click()
    pyautogui.typewrite('takitorj@b')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

# chọn server
def serverNorth():
    pyautogui.moveTo(850, 560)
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
id = 79

# skip_indexes là các id của acc đã bán
skip_indexes = [3, 4, 7, 8, 10, 20, 22, 30, 32]

time.sleep(3)

# vòng lặp while giúp chạy từ id = 1 đến id mà mình muốn, t có 31 acc nên sẽ chạy đến 31
# nếu id mà trùng với id trong số acc đã bán thì id tăng 1 và vòng lặp bỏ qua id hiện tại
# nếu id không trùng thì chạy đoạn code autologin và print ra id đế check
while (id <101):
    if id in skip_indexes:
        pass
    else:
        gotoGame()
        time.sleep(5)
        id_str = str(id).zfill(2)
        accAndPass(id_str)
        time.sleep(1)
        serverNorth()
        time.sleep(20)
        closeTruyKich()
        time.sleep(5)
        print(id)
    id+=1

