import aircv as ac
import pyautogui as auto
import time

import Similary


def Exist(imsch,target):
    auto.screenshot("src.png")
    imsrc = ac.imread("src.png")
    position = ac.find_template(imsrc, imsch)
    if (position is None):
        return False
    else:
        area = position['rectangle']
        left = area[0][0]
        right = area[2][0]
        top = area[1][1]
        bottom = area[0][1]
        width = abs(left - right)
        height = abs(top - bottom)
        auto.screenshot("waittov/" + target + ".png", region=(left, bottom, width, height))
        if ((Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)) > 0.8):
            return True
        return False


def nav(xlo, ylo):
    if (not Exist(imsch=ac.imread("backimage/move_btn.bmp"),target="move_btn")):
        auto.hotkey('altleft', '`')
    else:
        auto.hotkey('altleft', '`')
        auto.hotkey('altleft', '`')
    x, y = find(imsch=ac.imread("backimage/location.bmp"), target="location")
    click(x, y)
    auto.write(xlo)
    x, y = find(imsch=ac.imread("backimage/location.bmp"), target="location")
    click(x, y)
    auto.write(ylo)
    time.sleep(1)
    x, y = find(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")
    click(x, y)


def find(imsch, target):
    auto.screenshot("src.png")
    imsrc = ac.imread("src.png")
    position = ac.find_template(imsrc, imsch)
    i = 0
    while (position is None):
        i += 1
        print("Can't find out "+target)
        auto.screenshot("src.png")
        imsrc = ac.imread("src.png")
        position = ac.find_template(imsrc, imsch)
        time.sleep(5)
    area = position['rectangle']
    left = area[0][0]
    right = area[2][0]
    top = area[1][1]
    bottom = area[0][1]
    width = abs(left - right)
    height = abs(top - bottom)
    auto.screenshot("waittov/" + target + ".png", region=(left, bottom, width, height))
    if ((Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)) > 0.8):
        print("match"+target)
        x, y = position['result']
        return x, y
    print("Not match"+target)
    time.sleep(1)
    find(imsch, target)


def click(x, y):
    auto.moveTo(x, y)
    auto.mouseDown()
    auto.mouseUp()


def findandclick(string):
    global imsch
    if (string == 'death'):
        imsch = ac.imread("backimage/death.bmp")
    if (string == 'navigation_btn'):
        imsch = ac.imread("backimage/navigation_btn.bmp")
    if (string == 'loulan'):
        imsch = ac.imread("backimage/loulan.bmp")
    if (string == 'mount'):
        imsch = ac.imread("backimage/mount.bmp")
    if (string == 'zhufengjiu'):
        imsch = ac.imread("backimage/zhufengjiu.bmp")
    if (string == 'move_btn'):
        imsch = ac.imread("backimage/move_btn.bmp")
    if(string =='ok_btn'):
        imsch=ac.imread("backimage/ok_btn.bmp")
    x, y = find(imsch, string)
    click(x, y)