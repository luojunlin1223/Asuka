import aircv as ac
import pyautogui as auto
import time

import Similary


def Exist(imsch,target):
    auto.screenshot("Existsrc.png")
    imsrc = ac.imread("Existsrc.png")
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
        print(target+'的匹配度：'+str(Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)))
        if ((Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)) > 0.7):
            return True
        return False


def nav(xlo, ylo):
    if (not Exist(imsch=ac.imread("backimage/move_btn.bmp"),target="move_btn")):
        auto.hotkey('altleft','`')
    else:
        auto.hotkey('altleft','`')
        auto.hotkey('altleft','`')
    x, y = find(imsch=ac.imread("backimage/location.bmp"), target="location")
    click(x, y)
    auto.write(xlo)
    x, y = find(imsch=ac.imread("backimage/location.bmp"), target="location")
    click(x, y)
    auto.write(ylo)
    x, y = find(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")
    click(x, y)
    auto.press('esc')

def find_re(imsch,target):
    while True:
        auto.screenshot("src.png")
        imsrc = ac.imread("src.png")
        position = ac.find_template(imsrc, imsch)
        i = 0
        while (position is None):
            i += 1
            print("找不到： " + target)
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
        diff = Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)
        print(diff)
        if (diff > 0.7):
            print("找到：" + target)
            x, y = position['result']
            return x, y, area
        print("准确度不匹配：" + target)
        time.sleep(1)


def find(imsch, target):
    while True:
        auto.screenshot("src.png")
        imsrc = ac.imread("src.png")
        position = ac.find_template(imsrc, imsch)
        i = 0
        while (position is None):
            i += 1
            print("找不到： " + target)
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
        diff=Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)
        if ( diff> 0.7):
            print("找到：" + target)
            x, y = position['result']
            return x, y
        print("准确度不匹配：" + target)
        time.sleep(1)



def click(x, y):
    auto.moveTo(x, y)
    auto.mouseDown()
    auto.mouseUp()


def findandclick(string):
    global imsch
    if (string == 'huanpiao'):
        imsch = ac.imread("backimage/huanpiao.bmp")
    if (string == 'cailiao'):
        imsch = ac.imread("backimage/cailiao.bmp")
    if (string == 'dibang'):
        imsch = ac.imread("backimage/dibang.bmp")
    if (string == 'zhengbei'):
        imsch = ac.imread("backimage/zhengbei.bmp")
    if (string == 'lingpiao'):
        imsch = ac.imread("backimage/lingpiao.bmp")
    if (string == 'wobang'):
        imsch = ac.imread("backimage/wobang.bmp")
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
    if(string =='shopzhengdong'):
        imsch=ac.imread("backimage/shopzhengdong.bmp")
    if (string == 'shopyour'):
        imsch = ac.imread("backimage/shopyour.bmp")
    if(string == 'shopzhengxi'):
        imsch = ac.imread("backimage/shopzhengxi.bmp")
    if (string == 'shopmy'):
        imsch = ac.imread("backimage/shopmy.bmp")
    if (string == 'datunpc'):
        imsch = ac.imread("backimage/datunpc.bmp")
    if (string == 'downarrow'):
        imsch = ac.imread("backimage/downarrow.bmp")
    if (string == 'datu'):
        imsch = ac.imread("backimage/datu.bmp")
    if(string=='renwu_in_beibao'):
        imsch = ac.imread("backimage/renwu_in_beibao.bmp")
    if(string=='fufeichuansong'):
        imsch=ac.imread('backimage/fufeichuansong.bmp')
    if (string == 'nanhai'):
        imsch = ac.imread('backimage/nanhai.bmp')
    if (string == 'nav_ok_btn'):
        imsch = ac.imread('backimage/nav_ok_btn.bmp')
    if (string == 'nanzhao'):
        imsch = ac.imread('backimage/nanzhao.bmp')
    if (string == 'liaoxi'):
        imsch = ac.imread('backimage/liaoxi.bmp')
    if (string == 'liaoxitarget'):
        imsch = ac.imread('backimage/liaoxitarget.bmp')
    if (string == 'jixu'):
        imsch = ac.imread('backimage/jixu.bmp')
    if (string == 'back_to_home'):
        imsch = ac.imread('backimage/back_to_home.bmp')
    if (string == 'daocaoren'):
        imsch = ac.imread('backimage/daocaoren.bmp')
    if (string == 'zhongzhizaochan'):
        imsch = ac.imread('backimage/zhongzhizaochan.bmp')
    if (string == 'zhongzhi5'):
        imsch = ac.imread('backimage/zhongzhi5.bmp')
    if (string == 'qianbushiqu'):
        imsch = ac.imread('backimage/quanbushiqu.bmp')
    if (string == 'zhengnan'):
        imsch = ac.imread('backimage/zhengnan.bmp')
    if (string == 'liangshi'):
        imsch = ac.imread('backimage/liangshi.bmp')
    if (string == 'chenchu'):
        imsch = ac.imread('backimage/chenchu.bmp')
    x, y = find(imsch, string)
    click(x, y)


def gooutbang():
    nav('98', '159')


def jinbang():
    nav('148', '56')


def shaqichuansong():
    while True:
        if (Exist(imsch=ac.imread("backimage/ok_btn.bmp"), target='ok_btn')):
            findandclick('ok_btn')
            break
    print("已经到达(杀气判断)")
    time.sleep(5)


def arrive():
    start_time=time.time()
    while True:
        end_time=time.time()
        if (Exist(imsch=ac.imread("backimage/qiehuanchangjing.bmp"), target='qiehuanchangjing')):
            break
        if(abs(start_time-end_time)>60*2):
            break
    print("已经到达")
    time.sleep(5)


def nav_npc(npc):
    if (not Exist(imsch=ac.imread("backimage/move_btn.bmp"),target="move_btn")):
        auto.hotkey('altleft', '`')
    else:
        auto.hotkey('altleft', '`')
        auto.hotkey('altleft', '`')
    findandclick(npc)
    findandclick('move_btn')
    while True:
        if (Exist(imsch=ac.imread("backimage/zaijian.bmp"), target='zaijian')):
            break
    print("已经找到npc")


def adjust_click(location, clicklocation):
    nav(location[0], location[1])
    auto.hotkey('altleft', 'v')
    time.sleep(1)
    click(int(clicklocation[0]), int(clicklocation[1]))
    click(int(clicklocation[0]), int(clicklocation[1]))