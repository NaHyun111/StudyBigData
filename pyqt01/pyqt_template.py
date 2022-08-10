import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # return값이 없으므로 None적기 (생성자는 return값이 없기때문에 None을 써줘야함)
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300, 200, 500, 200)  # (300,200)좌표에 넓이 500, 높이 200짜리를 만드셈 -> 원하는 위치,크기 설정해주면됨
        self.setWindowTitle('QTemplate!!!')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()