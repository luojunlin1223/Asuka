import colorsys
import sys
import time

import aircv as ac
import pyautogui as auto
import pyperclip
from PIL import Image
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QWidget, QTextEdit, QLineEdit, QApplication
import Similary
from Tool import findandclick, nav

list=['189','61']
string=[''
        ,''
        ,''
        ,''
        ,'']
class RemoveOb(QThread):
    postSignal = pyqtSignal(str)


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
            if (Exist_ob(imsch=ac.imread("backimage/shaqientrance.bmp"), target="shaqientrance")):
                self.postSignal.emit("发现干扰！")
                findandclick('ok_btn')
            time.sleep(3)
            self.postSignal.emit("没有发现干扰！")
            detect()
        detect()


class AutoN(QThread):
    postSignal = pyqtSignal(str)


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
            time.sleep(2)
            auto.screenshot("neiguasrc.png")
            imsch = ac.imread("backimage/neigua.bmp")
            imsrc = ac.imread("neiguasrc.png")
            position = ac.find_template(imsrc, imsch)
            area = position['rectangle']
            left = area[0][0]
            right = area[2][0]
            top = area[1][1]
            bottom = area[0][1]
            width = abs(left - right)
            height = abs(top - bottom)
            im = auto.screenshot("neiguasrc.png", region=(left, bottom, width, height))
            image = Image.open("neiguasrc.png")
            image = image.convert('RGB')
            while (get_dominant_color(image)[0] < 200):
                time.sleep(1)
                self.postSignal.emit("正在正常打怪.......")
                auto.screenshot("neiguasrc.png")
                imsch = ac.imread("backimage/neigua.bmp")
                imsrc = ac.imread("neiguasrc.png")
                position = ac.find_template(imsrc, imsch)
                area = position['rectangle']
                left = area[0][0]
                right = area[2][0]
                top = area[1][1]
                bottom = area[0][1]
                width = abs(left - right)
                height = abs(top - bottom)
                im = auto.screenshot("neiguasrc.png", region=(left, bottom, width, height))
                image = Image.open("neiguasrc.png")
            auto.hotkey('altleft', 'l')
            self.postSignal.emit("自动开启内挂")
            attackneverdie()
        attackneverdie()



class BacktoDeath(QThread):
    postSignal = pyqtSignal(str)
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
            findandclick('death')
            self.postSignal("检测到死亡")
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
            self.postSignal.emit("正在前往("+list[0]+","+list[1]+")....")
            time.sleep(62)
            findandclick('mount')
            time.sleep(1)
            auto.press('esc')
            time.sleep(1)
            auto.hotkey('altleft','l')
            song()
        song()
class AutoAttack(QThread):
    postSignal = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(2)
        while True:
            auto.hotkey('ctrlleft','tab')
            auto.hotkey('altleft','1')
            auto.hotkey('altleft', '2')



class Window(QWidget):
    def getprocess(self,postSignal):
        self.infromationtext.setText(postSignal)
    def threadFinished(self):
        self.infromationtext.setText("程序结束")
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.BacktoDeath=BacktoDeath()
        self.BacktoDeath.finished.connect(self.threadFinished)
        self.BacktoDeath.postSignal.connect(self.getprocess)

        self.AutoAttack=AutoAttack()
        self.AutoAttack.finished.connect(self.threadFinished)
        self.AutoAttack.postSignal.connect(self.getprocess)

        self.AutoN = AutoN()
        self.AutoN.finished.connect(self.threadFinished)
        self.AutoN.postSignal.connect(self.getprocess)

        self.Removeob=RemoveOb()
        self.Removeob.finished.connect(self.threadFinished)
        self.Removeob.postSignal.connect(self.getprocess)
        #2.2设置控件
        self.setWindowTitle("回点测试版本")
        self.resize(500,500)
        self.btn_w=80
        self.btn_h=40
        self.top_margin=0
        self.setup_ui()

    def setup_ui(self):
        song_btn = QPushButton(self)
        self.song_btn = song_btn
        song_btn.setText("送刀")
        song_btn.resize(self.btn_w, self.btn_h)

        stop_btn = QPushButton(self)
        self.stop_btn = stop_btn
        stop_btn.setText("停止")
        stop_btn.resize(self.btn_w, self.btn_h)
        stop_btn.move(150,0)

        attack_btn = QPushButton(self)
        self.attack_btn = attack_btn
        attack_btn.setText("打怪")
        attack_btn.resize(self.btn_w, self.btn_h)
        attack_btn.move(120, 50)

        autoattack_btn = QPushButton(self)
        self.autoattack_btn = autoattack_btn
        autoattack_btn.setText("自动开启内挂")
        autoattack_btn.resize(self.btn_w, self.btn_h)
        autoattack_btn.move(80, 0)

        Removeob_btn = QPushButton(self)
        self.Removeob_btn = Removeob_btn
        Removeob_btn.setText("消除干扰")
        Removeob_btn.resize(self.btn_w, self.btn_h)
        Removeob_btn.move(250, 0)

        locationedit1=QTextEdit(self)
        self.locationedit1=locationedit1
        locationedit1.move(0,50)
        locationedit1.resize(50,30)

        locationedit2 = QTextEdit(self)
        self.locationedit2 = locationedit2
        locationedit2.move(40, 50)
        locationedit2.resize(50, 30)

        infromationtext=QLineEdit(self)
        self.infromationtext=infromationtext
        infromationtext.move(40,150)

        song_btn.clicked.connect(self.song)
        stop_btn.clicked.connect(self.stop)
        attack_btn.clicked.connect(self.attack)
        autoattack_btn.clicked.connect(self.autoattack)
        Removeob_btn.clicked.connect(self.removeob)
    def removeob(self):
        self.Removeob.start()
    def autoattack(self):
        self.AutoN.start()
    def attack(self):
        self.AutoAttack.start()
    def stop(self):
        self.BacktoDeath.terminate()
        self.AutoAttack.terminate()
        self.AutoN.terminate()
        self.Removeob.terminate()
    def song(self):
        self.BacktoDeath.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
