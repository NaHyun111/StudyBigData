import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # return값이 없으므로 None적기 (생성자는 return값이 없기때문에 None을 써줘야함)
        super().__init__()
        self.initUI()

    # 화면정의를 위해 만든 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 600, 400)  # (300,200)좌표에 넓이 600, 높이 400짜리를 만드셈 -> 원하는 위치,크기 설정해주면됨
        self.setWindowTitle('Qlabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/image/lion.png')) # 윈도우아이콘 지정
        label1 = QLabel('111', self)   
        label2 = QLabel('', self)
        label1.setStyleSheet(
            ('border-width: 3px;'
            'border-style: solid;'
            'border-color: blue;'
            'image: url(./pyqt01/image/image1.png)')
        )
        label2.setStyleSheet(
            ('border-width: 3px;'
            'border-style: dot-dot-dash;'
            'border-color: red;'
            'image: url(./pyqt01/image/image2.png)')
        )

        box = QHBoxLayout() # QHBoxLayout은 가로로 나오고 QVBoxLayout은 세로로 출력됨
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()