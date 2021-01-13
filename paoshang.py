from Tool import find, click
import aircv as ac
import pyautogui as auto
def updateshop():
    x, y = find(imsch=ac.imread('backimage/shop2.bmp'), target='shop2')
    click(x, y)
    auto.moveTo(1,1)