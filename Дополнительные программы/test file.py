import sys
import sys

from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QSpinBox, QDoubleSpinBox
from PyQt5.QtGui import QFont

admin_root = False


def admin(a, b):
    if admin_root:
        print(a, b)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 500, 500, 300)

        font = QFont()
        font.setPointSize(14)
        self.font = font

        self.labell = QLabel(self)

        self.clik = QPushButton("Рассчитать", self)
        self.clik.move(400, 5)
        self.clik.resize(100, 30)
        self.clik.clicked.connect(self.work_programm)

        self.printt = QLineEdit(self)
        self.printt.move(115, 5)
        self.printt.resize(280, 30)
        self.printt.setFont(font)

        self.text1 = QLabel("Имя файла", self)
        self.text1.move(10, 5)
        self.text1.setFont(font)

        self.spin_print2 = QSpinBox(self)
        self.spin_print2.move(245, 40)
        self.spin_print2.resize(250, 30)
        self.spin_print2.setFont(font)
        self.spin_print2.setValue(50)

        self.spin_print2_line = QLineEdit("0", self)
        self.spin_print2_line.move(245, 40)
        self.spin_print2_line.resize(230, 30)
        self.spin_print2_line.setFont(font)

        self.text2 = QLabel("Максимальное значение:", self)
        self.text2.move(10, 40)
        self.text2.setFont(font)

        self.spin_print3 = QSpinBox(self)
        self.spin_print3.move(245, 80)
        self.spin_print3.resize(250, 30)
        self.spin_print3.setFont(font)
        self.spin_print3.setValue(50)

        self.spin_print3_line = QLineEdit("0", self)
        self.spin_print3_line.move(245, 80)
        self.spin_print3_line.resize(230, 30)
        self.spin_print3_line.setFont(font)

        self.text3 = QLabel("Минимальное значение:", self)
        self.text3.move(10, 80)
        self.text3.setFont(font)

        self.spin_print4 = QDoubleSpinBox(self)
        self.spin_print4.move(245, 120)
        self.spin_print4.resize(250, 30)
        self.spin_print4.setFont(font)
        self.spin_print4.setValue(50)

        self.spin_print4_line = QLineEdit("0.00", self)
        self.spin_print4_line.move(245, 120)
        self.spin_print4_line.resize(230, 30)
        self.spin_print4_line.setFont(font)

        self.text4 = QLabel("Средние значение:", self)
        self.text4.move(10, 120)
        self.text4.setFont(font)

    def work_programm(self):
        self.labell.hide()
        try:
            file_save = open(self.printt.text(), encoding="utf-8", mode="rt").read()  # здесь надо изменить имя файла
        except FileNotFoundError:
            self.labell.hide()
            self.labell = QLabel(f"файл '{self.printt.text()}' не найден", self)
            self.labell.move(10, 270)
            self.labell.setFont(self.font)
            self.labell.show()
            return

        maxx = -10000000000000000000000000000000000
        minn = 100000000000000000000000000000000000
        sum_cr = 0
        count_cr = 0
        for i in file_save.split():
            try:
                i = int(i)
            except TypeError:
                self.labell.hide()
                self.labell = QLabel(f"В файле '{self.printt.text()}' содержатся не корректные данные", self)
                self.labell.move(10, 270)
                self.labell.setFont(self.font)
                self.labell.show()
                return

            admin(i, type(i))
            if i > maxx:
                admin("max", i)
                maxx = i
            if i < minn:
                admin("min", i)
                minn = i
            sum_cr += i
            count_cr += 1
        admin("max", maxx)
        admin("min", minn)
        self.spin_print2_line.setText(str(maxx))
        self.spin_print3_line.setText(str(minn))
        self.spin_print4_line.setText(str(sum_cr / count_cr))

        # list_file_save = file_save.split("\n")
        # self.printt.setText(choice(list_file_save))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())

