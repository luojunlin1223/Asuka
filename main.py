
import sys
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from Function import *

list=['189','61']
string=[''
        ,''
        ,''
        ,''
        ,'']


class Window(QWidget):
    def update_AutoN(self,postSignal_AutoN):
        self.infromationtext_AutoN.setText(postSignal_AutoN)
    def update_BacktoDeath(self,postSignal_BacktoDeath):
        self.infromationtext_Back.setText(postSignal_BacktoDeath)
    def update_Rem(self,postSignal_Rem):
        self.infromationtext_Rem.setText(postSignal_Rem)
    def threadFinished(self):
        self.infromationtext_Rem.setText("干扰程序结束")
        self.infromationtext_Back.setText("回点中止")
        self.infromationtext_AutoN.setText("自动开启内挂中止")
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.BacktoDeath=BacktoDeath()
        self.BacktoDeath.finished.connect(self.threadFinished)
        self.BacktoDeath.postSignal_BacktoDeath.connect(self.update_BacktoDeath)

        self.AutoAttack=AutoAttack()

        self.AutoN = AutoN()
        self.AutoN.finished.connect(self.threadFinished)
        self.AutoN.postSignal_AutoN.connect(self.update_AutoN)

        self.Removeob=RemoveOb()
        self.Removeob.finished.connect(self.threadFinished)
        self.Removeob.postSignal_Rem.connect(self.update_Rem)
        self.shop_second=shop_second()


        self.dig=dig()
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
        song_btn.setText("自动回根据地")
        song_btn.resize(self.btn_w, self.btn_h)

        shop_second_btn = QPushButton(self)
        self.shop_second_btn = shop_second_btn
        shop_second_btn.setText("跑商回")
        shop_second_btn.resize(self.btn_w, self.btn_h)
        shop_second_btn.move(80, 300)

        dig_btn = QPushButton(self)
        self.dig_btn = dig_btn
        dig_btn.setText("dig")
        dig_btn.resize(self.btn_w, self.btn_h)
        dig_btn.move(160, 300)


        stop_btn = QPushButton(self)
        self.stop_btn = stop_btn
        stop_btn.setText("停止")
        stop_btn.resize(self.btn_w, self.btn_h)
        stop_btn.move(160,40)

        attack_btn = QPushButton(self)
        self.attack_btn = attack_btn
        attack_btn.setText("打怪")
        attack_btn.resize(self.btn_w, self.btn_h)
        attack_btn.move(0, 40)

        attack_btn_gap=QLineEdit(self)
        self.attack_btn_gap=attack_btn_gap
        attack_btn_gap.resize(self.btn_w,self.btn_h)
        attack_btn_gap.move(80,40)
        qi=QIntValidator(1, 999)
        attack_btn_gap.setValidator(qi)

        autoattack_btn = QPushButton(self)
        self.autoattack_btn = autoattack_btn
        autoattack_btn.setText("自动开启内挂")
        autoattack_btn.resize(self.btn_w, self.btn_h)
        autoattack_btn.move(80, 0)

        Removeob_btn = QPushButton(self)
        self.Removeob_btn = Removeob_btn
        Removeob_btn.setText("消除干扰or刷马")
        Removeob_btn.resize(self.btn_w, self.btn_h)
        Removeob_btn.move(160, 0)

        infromationtext_Rem=QLineEdit(self)
        self.infromationtext_Rem=infromationtext_Rem
        infromationtext_Rem.resize(240,40)
        infromationtext_Rem.move(0,160)

        infromationtext_Back=QLineEdit(self)
        self.infromationtext_Back=infromationtext_Back
        infromationtext_Back.resize(240,40)
        infromationtext_Back.move(0,80)

        infromationtext_AutoN = QLineEdit(self)
        self.infromationtext_AutoN = infromationtext_AutoN
        infromationtext_AutoN.resize(240, 40)
        infromationtext_AutoN.move(0, 120)

        title_hint=QLabel(self)
        self.titile_hint=title_hint
        title_hint.setText("功能说明:")
        title_hint.move(330,0)

        hint=QLabel(self)
        self.hint=hint
        hint.resize(300,220)
        hint.move(250,10)
        hint.setText("最上面3个功能是同时开\n\n状态分别显示在下面3个信息框中\n\n"
                     "停止会停下所有功能\n\n"
                     "想要我把你们拉走需要把3个功能全部打开\n\n"
                     "打怪小心使用 切换怪的速度很快（会反击人）\n\n"
                     "有任何问题微信告诉我\n\n"
                     "回点坐标：（189，61）\n\n"
                     "喊话默认关闭")

        song_btn.clicked.connect(self.song)
        stop_btn.clicked.connect(self.stop)
        attack_btn.clicked.connect(self.attack)
        autoattack_btn.clicked.connect(self.autoattack)
        Removeob_btn.clicked.connect(self.removeob)
        shop_second_btn.clicked.connect(self.Shop_second)
        dig_btn.clicked.connect(self.Dig)
    def Dig(self):
        if(self.dig.isRunning()):
            self.dig.terminate()
        self.dig.start()
    def Shop_second(self):
        self.shop_second.start()
    def removeob(self):
        self.Removeob.start()
        self.infromationtext_Rem.setText("抗干扰启动")
    def autoattack(self):
        self.AutoN.start()
        self.infromationtext_AutoN.setText("自动开启内挂启动")
    def attack(self):
        self.AutoAttack.start()
        gap=self.attack_btn_gap.text()
    def stop(self):
        self.BacktoDeath.terminate()
        self.AutoAttack.terminate()
        self.AutoN.terminate()
        self.Removeob.terminate()
        self.shop_first.terminate()
        self.shop_second.terminate()
        self.dig.terminate()
    def song(self):
        self.BacktoDeath.start()
        self.infromationtext_Back.setText("回点程序启动")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
