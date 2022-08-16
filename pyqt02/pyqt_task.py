import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # return값이 없으므로 None적기 (생성자는 return값이 없기때문에 None을 써줘야함)
        super().__init__()
        uic.loadUi('./pyqt02/ttask.ui', self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btn1_clicked)

    # def btn1_clicked(self):  -> 이렇게해야맞는건데,,,,
    #     self.txbLog.append('실행!!')
    #     self.pgbTask.setRange(0, 99)
    #     for i in range(0, 100):
    #         print(f'출력 : {i}')
    #         self.pgbTask.setValue(i)
    #         self.txbLog.append(f'출력 > {i}')

    def btn1_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0, 999999)
        for i in range(0, 1000000):  # 값이 너무 커서 응답없음이 됨
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()