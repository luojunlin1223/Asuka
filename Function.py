import colorsys
import time
from enum import auto

import pyperclip
from PIL.Image import Image
from PyQt5.QtCore import QThread, pyqtSignal

import Similary
from BaiduImageRead import ImageRead
from Tool import gooutbang, nav, nav_npc, findandclick, jinbang, Exist, find, click
import aircv as ac

from dingding import push_to_dingding


class shop_second(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(2)
        gooutbang()
        nav('34','50')
        nav('32', '162')
        nav('38', '284')
        nav('32', '176')
        nav('159', '287')
        nav_npc('shopzhengxi')
        findandclick('shopmy')
        time.sleep(3)
        jinbang()
        ''''
        gooutbang()
        nav('34', '50')
        time.sleep(60 + 15)
        nav('32', '162')
        time.sleep(57)
        shaqichuansong()
        nav('38', '384')
        time.sleep(60 + 51)
        nav('32', '176')
        time.sleep(60 + 11)
        nav('159', '287')
        time.sleep(59)
        auto.hotkey('altleft', '`')
        findandclick('shopzhengxi')
        findandclick('move_btn')
        time.sleep(60 + 5)
        findandclick('shopmy')
        time.sleep(3)
        jinbang()
        '''

class shop_first(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(2)
        gooutbang()
        nav('287', '32') #大理
        nav('288', '151')#无量山
        nav('287', '77')#镜湖
        nav('285', '44')
        nav('182', '287')
        nav_npc('shopzhengdong')
        findandclick('shopyour')
        time.sleep(3)
        jinbang()
        '''
        gooutbang()
        nav('287','32')
        time.sleep(60+15)
        nav('288', '151')
        time.sleep(57)
        nav('287','77')
        time.sleep(60+10)
        shaqichuansong()
        nav('285','44')
        time.sleep(60+52)
        nav('182','287')
        time.sleep(55)
        auto.hotkey('altleft','`')
        findandclick('shopzhengdong')
        findandclick('move_btn')
        time.sleep(60+13)
        findandclick('shopyour')
        time.sleep(3)
        jinbang()
        '''
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
        findandclick('mount')
        time.sleep(5)
        auto.press('esc')
        nav_npc('datunpc')
        findandclick('datu')
        if(Exist(imsch=ac.imread('backimage/jixu.bmp'),target='jixu')):
            findandclick('jixu')
            auto.mouseDown()
            auto.mouseUp()
            nav_npc('datunpc')
            findandclick('datu')
        auto.press('esc')
        findchengeling()
        screenshot()
        where,x,y=ImageRead('datusrc.png')
        auto.press('esc')
        if(where=='辽西'):
            auto.hotkey('altleft','m')
            findandclick('liaoxi')
            findandclick('liaoxitarget')
            if(Exist(imsch=ac.imread('backimage/ok_btn.bmp'),target='ok_btn')):
                findandclick('ok_btn')
                auto.press('esc')
            time.sleep(2*60+10)
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
        push_to_dingding('快去打图')
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
        while True:
            auto.press('F2')
#            auto.hotkey('altleft', 'l')
            time.sleep(1)
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
            auto.hotkey('altleft', '3')
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