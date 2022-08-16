import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # return값이 없으므로 None적기 (생성자는 return값이 없기때문에 None을 써줘야함)
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 640, 400)  # (300,200)좌표에 넓이 500, 높이 200짜리를 만드셈 -> 원하는 위치,크기 설정해주면됨
        self.setWindowTitle('QPushobutton 예제')
        self.show()

    def addControls(self) -> None:
        self.label = QLabel('메시지 :', self)
        self.label.setGeometry(10, 10, 600, 40)
        self.btn1 = QPushButton('클릭', self)
        self.btn1.setGeometry(510, 350, 120, 40)
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결
        # click - 클릭했을때의 일 / cliked - 클릭하고 나서 일을 실행

    # event = signal (파이썬에서 둘은 동일한거)
    def btn1_clicked(self):
        self.label.setText('메시지 : btn1 버튼 클릭!!!')
        QMessageBox.information(self, 'signal', 'btn1_clicked!!')  # 일반정보창
        # QMessageBox.warning(self, 'signal', 'btn1_clicked!!')  # 경고창
        # QMessageBox.critical(self, 'signal', 'btn1_clicked!!')  # 에러창
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()