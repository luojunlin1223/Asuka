import colorsys
import time
import pyautogui as auto

import pyperclip
from PIL.Image import Image
from PyQt5.QtCore import QThread, pyqtSignal, QWaitCondition

import Similary
from BaiduImageRead import ImageRead, get_file_content, client
from Tool import gooutbang, nav, nav_npc, findandclick, jinbang, Exist, find, click, arrive, adjust_click, find_re
import aircv as ac

from dingding import push_to_dingding
from paoshang import updateshop
status =0   # 0:初始态  1:在我帮已经打开商人列表  3:到达对方帮会不打开商人列表 5:已经返回我帮不打开商人列表
    # 2：去对方帮路上      #4 ：回来路上
where = 999  # 999在我帮  #0 在洱海 #1 在大理 #2 在剑阁 #3 在敦煌 #4在洛阳 #5在雁南 #6在对面帮派
class shop_second(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __del__(self):
        self.wait()

    def run(self):
        global status
        def sell(good):
            findandclick('cailiao')
            auto.moveTo(1,1)
            if(good == 'liangshi'):
                while (Exist(imsch=ac.imread('backimage/liangshi2.bmp'), target='liangshi2')):
                    x, y = find(imsch=ac.imread('backimage/liangshi2.bmp'), target='liangshi2')
                    auto.moveTo(x, y)
                    x1, y1, area = find_re(imsch=ac.imread('backimage/maichujiazhi.bmp'), target='maichujiazhi')
                    auto.screenshot('pricesrc.png', region=(area[2][0], area[2][1], 150, abs(area[3][1] - area[2][1])))
                    image = get_file_content('pricesrc.png')
                    result = client.basicGeneral(image)
                    price = result['words_result'][0]['words']
                    if '94' in price:
                        while (Exist(imsch=ac.imread('backimage/liangshi2.bmp'), target='liangshi2')):
                            x, y = find(imsch=ac.imread('backimage/liangshi2.bmp'), target='liangshi2')
                            auto.moveTo(x, y)
                            auto.mouseDown(button='right')
                            auto.mouseUp(button='right')
                        while (Exist(imsch=ac.imread('backimage/liangshi2.bmp'), target='liangshi2')):
                            x, y = find(imsch=ac.imread('backimage/liangshi2.bmp'), target='liangshi2')
                            auto.moveTo(x, y)
                            auto.mouseDown(button='right')
                            auto.mouseUp(button='right')
                        break
                    else:
                        updateshop()
                        time.sleep(10)
            if(good=='chenchu'):
                while (Exist(imsch=ac.imread('backimage/chenchu2.bmp'), target='chenchu2')):
                    x, y = find(imsch=ac.imread('backimage/chenchu2.bmp'), target='chenchu2')
                    auto.moveTo(x, y)
                    x1, y1, area = find_re(imsch=ac.imread('backimage/maichujiazhi.bmp'), target='maichujiazhi')
                    auto.screenshot('pricesrc.png', region=(area[2][0], area[2][1], 150, abs(area[3][1] - area[2][1])))
                    image = get_file_content('pricesrc.png')
                    result = client.basicGeneral(image)
                    price = result['words_result'][0]['words']
                    if '83' in price:
                        while (Exist(imsch=ac.imread('backimage/chenchu2.bmp'), target='chenchu2')):
                            x, y = find(imsch=ac.imread('backimage/chenchu2.bmp'), target='chenchu2')
                            auto.moveTo(x, y)
                            auto.mouseDown(button='right')
                            auto.mouseUp(button='right')
                        while (Exist(imsch=ac.imread('backimage/chenchu2.bmp'), target='chenchu2')):
                            x, y = find(imsch=ac.imread('backimage/chenchu2.bmp'), target='chenchu2')
                            auto.moveTo(x, y)
                            auto.mouseDown(button='right')
                            auto.mouseUp(button='right')
                        break
                    else:
                        updateshop()
                        time.sleep(10)
        def buy(good,price1):
            auto.screenshot("shopsrc.png")
            result = ac.find_template(im_source=ac.imread('shopsrc.png'), im_search=good)
            if (result is None):
                print("没找到目标商品")
                buy(good,price1)
            else:
                rectangle = result['rectangle']
                x1 = rectangle[3][0]
                x = result['result'][0]
                y = result['result'][1]
                y1 = rectangle[3][1]
                height = abs(y - y1)
                shopresult = ac.find_template(im_source=ac.imread('shopsrc.png'),
                                              im_search=ac.imread('backimage/shop.bmp'))
                while shopresult is None:
                    auto.screenshot("shopsrc.png")
                    shopresult = ac.find_template(im_source=ac.imread('shopsrc.png'),
                                                  im_search=ac.imread('backimage/shop.bmp'))
                x2 = shopresult['result'][0]
                width = abs(x1 - x2)
                auto.screenshot('shopsrc.png', region=(x1, y, width, height+10))
                image = get_file_content('shopsrc.png')
                print(result['confidence'])
                result = client.basicGeneral(image)
                price = result['words_result'][0]['words']
                print(result['words_result'][0]['words'])
                auto.moveTo(1,1)
                if price1 == '49':
                    if price1 in price:
                        for i in range(0, 20):
                            findandclick('liangshi')
                            updateshop()
                            time.sleep(1)
                    else:
                        time.sleep(10)
                        updateshop()
                        buy(good, price1)
                if price1=='72':
                    if price1 in price:
                        for i in range(0, 20):
                            findandclick('chenchu')
                            updateshop()
                            time.sleep(1)
                    else:
                        time.sleep(10)
                        updateshop()
                        buy(good, price1)
        def goback():
            global where
            print('where:' + str(where))
            list=[('264','286'),('33','130'),('231','286'),('36','286'),('159','287')]
            if where==6:
                gooutbang()
                arrive()
                where-=1
            while where!=0:
                nav(list[abs(where-5)][0],list[abs(where-5)][1])
                arrive()
                where -= 1
            if where==0:
                nav_npc('zhengnan')
                findandclick('wobang')
                time.sleep(3)
                where=999
            if where==999:
                jinbang()
                time.sleep(35)
        def goto():
            global where
            print('where:'+ str(where))
            list = [('287', '32'), ('31','151'), ('105', '40'), ('284', '146'), ('286', '129')]
            if where==999:
                gooutbang()
                arrive()
                where =0
            while where!=len(list):
                nav(list[where][0], list[where][1])
                arrive()
                where += 1
            if where == 5:
                nav_npc('zhengbei')
                findandclick('dibang')
                time.sleep(3)
                where+=1
            if where == 6:
                jinbang()
                time.sleep(35)
        def prepare_my():
            updateshop()
            auto.hotkey('altleft','a')
            auto.hotkey('altleft','a')
            findandclick('cailiao')
            buy(ac.imread('backimage/liangshi.bmp'), '49')
        def prepare_your():
            adjust_click(location=('148', '56'), clicklocation=('734', '378'))
            updateshop()
            sell('liangshi')
            buy(ac.imread('backimage/chenchu.bmp'), '72')
        def end_shop():
            adjust_click(location=('148', '56'), clicklocation=('734', '378'))
            updateshop()
            sell('chenchu')
            findandclick('huanpiao')
            time.sleep(1)
            findandclick('lingpiao')
        time.sleep(2)
        print('status:'+str(status))
        if(status==0):
            adjust_click(location=('148', '56'), clicklocation=('734', '378'))
            findandclick('lingpiao')
            status += 1
        while True:
            if(status==1):
                prepare_my()
                status+=1
            if(status == 2):
                goto()
                status += 1
            if(status==3):
                prepare_your()
                status += 1
            if (status == 4):
                goback()
                status += 1
            if (status == 5):
                end_shop()
                status=1












class dig(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        def nav(xlo,ylo):
            if (not Exist(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")):
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
            x, y = find(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")
            click(x, y)
            auto.press('esc')
        def findchengeling():
            auto.hotkey('altleft', 'a')
            findandclick('renwu_in_beibao')
            x, y = find(imsch=ac.imread('backimage/chengeling.bmp'), target='chengeling')
            auto.mouseDown(button='right', x=x, y=y)
            auto.mouseUp(button='right', x=x, y=y)
        def screenshot():
            x,y=find(imsch=ac.imread('backimage/zaijian.bmp'),target='zaijian')
            x1,y1=find(imsch=ac.imread('backimage/datu_zuoshang.bmp'),target='datu_zuoshang')
            auto.screenshot('datusrc.png',region=(x1, y1, abs(x-x1), abs(y-y1)))
        def nav_npc(npc):
            if (not Exist(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")):
                auto.hotkey('altleft', '`')
            else:
                auto.hotkey('altleft', '`')
                auto.hotkey('altleft', '`')
            if(npc=='datunpc'):
                x, y = find(imsch=ac.imread('backimage/downarrow.bmp'), target='downarrow')
                while(x<500):
                    x, y = find(imsch=ac.imread('backimage/downarrow.bmp'), target='downarrow')
                for i in range(0, 45):
                    auto.mouseDown(x,y)
                    auto.mouseUp(x,y)
            findandclick(npc)
            findandclick('move_btn')
            auto.press('esc')
            while True:
                if (Exist(imsch=ac.imread("backimage/zaijian.bmp"), target='zaijian')):
                    break
            print("已经找到npc")
        time.sleep(2)
        if(Exist(imsch=ac.imread('backimage/ismount.bmp'),target='ismount')):
            findandclick('mount')
            auto.press('esc')
            findchengeling()
            auto.hotkey('altleft', 'l')
            auto.hotkey('altleft','a')
            auto.hotkey('altleft', 'a')
            time.sleep(20)
            auto.hotkey('altleft', 'l')
        else:
            auto.hotkey('altleft', 'l')
            auto.hotkey('altleft', 'a')
            auto.hotkey('altleft', 'a')
            time.sleep(20)
            auto.hotkey('altleft', 'l')
        if(Exist(imsch=ac.imread('backimage/back_to_home.bmp'),target='back_to_home')):
            findandclick('back_to_home')
            i=0
            while True:
                i+=1
                print(i)
                if (Exist(imsch=ac.imread("backimage/qiehuanchangjing.bmp"), target='qiehuanchangjing')):
                    time.sleep(5)
                    break
                if(i%50==0):
                    findandclick('back_to_home')
            findandclick('mount')
            time.sleep(5)
            auto.press('esc')
            nav_npc('datunpc')
            findandclick('datu')
            if (Exist(imsch=ac.imread('backimage/jixu.bmp'), target='jixu')):
                findandclick('jixu')
                time.sleep(1)
                auto.mouseDown()
                auto.mouseUp()
                nav_npc('datunpc')
                findandclick('datu')
            auto.press('esc')
            findchengeling()
            screenshot()
            where, x, y = ImageRead('datusrc.png')
            auto.press('esc')
            if (where == '辽西'):
                auto.hotkey('altleft', 'm')
                findandclick('liaoxi')
                findandclick('liaoxitarget')
                if (Exist(imsch=ac.imread('backimage/ok_btn.bmp'), target='ok_btn')):
                    findandclick('ok_btn')
                    auto.press('esc')
                time.sleep(2 * 60 + 10)
            else:
                if (where == '南海'):
                    nav_npc('fufeichuansong')
                    findandclick('nanhai')
                if (where == '南诏'):
                    nav_npc('fufeichuansong')
                    findandclick('nanzhao')
                findandclick('nav_ok_btn')
                time.sleep(3)
            nav(x, y)
            time.sleep(30)
            push_to_dingding('快去打图')
        else:
            push_to_dingding('打图没有传送符了')

class RemoveOb(QThread):
    postSignal_Rem = pyqtSignal(str)


    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        def Exist_ob(imsch, target):
            auto.screenshot("obsrc.png")
            imsrc = ac.imread("obsrc.png")
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
                if ((
                Similary.similary_calculate("waittov/" + target + ".png", "backimage/" + target + ".bmp", 1)) > 0.8):
                    return True
                return False
        def detect():
            while True:
                if (Exist_ob(imsch=ac.imread("backimage/shaqientrance.bmp"), target="shaqientrance")):
                    self.postSignal_Rem.emit("发现干扰！")
                    findandclick('ok_btn')
                time.sleep(3)
                self.postSignal_Rem.emit("没有发现干扰！")
        #detect()
        def nav(xlo, ylo):
            if (not Exist(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")):
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
            x, y = find(imsch=ac.imread("backimage/move_btn.bmp"), target="move_btn")
            click(x, y)
            auto.press('esc')
        def back():
            nav('56', '183')
            auto.hotkey('altleft', 'v')
        time.sleep(2)
        while True:
            auto.moveTo(699, 277)
            auto.mouseDown()
            auto.mouseUp()
            time.sleep(1)
            auto.moveTo(96, 252)
            auto.mouseDown()
            auto.mouseUp()
            time.sleep(1)
            auto.moveTo(94, 330)
            auto.mouseDown()
            auto.mouseUp()
            time.sleep(5 * 60 + 1)
            list = [(656, 324), (657, 234), (735, 229), (734, 316)]
            for i in range(0, 4):
                back()
                time.sleep(5)
                auto.moveTo(list[i][0], list[i][1])
                auto.mouseDown()
                auto.mouseUp()
                time.sleep(7)
                auto.moveTo(1036, 416)
                auto.mouseDown()
                auto.mouseUp()






class AutoN(QThread):
    postSignal_AutoN = pyqtSignal(str)


    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        def get_dominant_color(image):
            max_score = 0.0001
            dominant_color = None
            for count, (r, g, b) in image.getcolors(image.size[0] * image.size[1]):
                # 转为HSV标准
                saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
                y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
                y = (y - 16.0) / (235 - 16)

                # 忽略高亮色
                if y > 0.9:
                    continue
                score = (saturation + 0.1) * count
                if score > max_score:
                    max_score = score
                    dominant_color = (r, g, b)
                return dominant_color
        def attackneverdie():
            while True:
                time.sleep(2)
                auto.screenshot("neiguasrc.png")
                imsch = ac.imread("backimage/neigua.bmp")
                imsrc = ac.imread("neiguasrc.png")
                position = ac.find_template(imsrc, imsch)
                if(position is None):
                    self.postSignal_AutoN.emit("找不到自动打怪按钮")
                    break
                area = position['rectangle']
                left = area[0][0]
                right = area[2][0]
                top = area[1][1]
                bottom = area[0][1]
                width = abs(left - right)
                height = abs(top - bottom)
                auto.screenshot("neiguasrc.png", region=(left, bottom, width, height))
                image = Image.open("neiguasrc.png")
                image = image.convert('RGB')
                while (get_dominant_color(image)[0] < 200):
                    time.sleep(1)
                    self.postSignal_AutoN.emit("正在正常打怪.......")
                    auto.screenshot("neiguasrc.png")
                    imsch = ac.imread("backimage/neigua.bmp")
                    imsrc = ac.imread("neiguasrc.png")
                    position = ac.find_template(imsrc, imsch)
                    if (position is None):
                        self.postSignal_AutoN.emit("找不到自动打怪按钮")
                        break
                    area = position['rectangle']
                    left = area[0][0]
                    right = area[2][0]
                    top = area[1][1]
                    bottom = area[0][1]
                    width = abs(left - right)
                    height = abs(top - bottom)
                    auto.screenshot("neiguasrc.png", region=(left, bottom, width, height))
                    image = Image.open("neiguasrc.png")
                auto.hotkey('altleft', 'l')
                self.postSignal_AutoN.emit("自动开启内挂")
        attackneverdie()
class BacktoDeath(QThread):
    postSignal_BacktoDeath = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        def hanhua(string):
            pyperclip.copy(string)  # 先复制
            auto.hotkey('ctrl', 'v')
            auto.press('enter')# 再粘贴
        def song():
            time.sleep(2)
            self.postSignal_BacktoDeath.emit("正在检测死亡中.......")
            findandclick('death')
            self.postSignal_BacktoDeath.emit("检测到死亡")
            time.sleep(3)
            findandclick('navigation_btn')
            nav('10','23')
            time.sleep(10)
            auto.hotkey('altleft', '`')
            findandclick('zhufengjiu')
            findandclick('move_btn')
            time.sleep(5)
            findandclick('loulan')
            time.sleep(5)
            findandclick('mount')
            time.sleep(4)
            nav('298','142')
            time.sleep(7)
            nav(list[0],list[1])
            self.postSignal_BacktoDeath.emit("正在前往("+list[0]+","+list[1]+")....")
            time.sleep(62)
            findandclick('mount')
            time.sleep(1)
            auto.press('esc')
            time.sleep(1)
            auto.hotkey('altleft','l')
            song()
        song()
class AutoAttack(QThread):
    gap=3
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(2)
        while True:
            auto.hotkey('ctrlleft', 'tab')
            auto.hotkey('altleft', '1')
            auto.hotkey('altleft', '2')

            time.sleep(1)
        ''''
        i=0
        while True:
            i+=1
            print(i)
            auto.hotkey('ctrlleft', 'tab')
            auto.hotkey('altleft', '1')
            auto.hotkey('altleft', '2')
            if(i%self.gap==0):
                auto.screenshot("src.png")
                position = ac.find_template(im_search=ac.imread("follow/target.bmp"), im_source=ac.imread("src.png"))
                if position is None:
                    print("无法跟随")
                else:
                    x, y = position['result']
                    click(x, y)
                    time.sleep(1)
                    '''