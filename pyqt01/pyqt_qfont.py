import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None:  # return값이 없으므로 None적기 (생성자는 return값이 없기때문에 None을 써줘야함)
        super().__init__()
        self.initUI()

    # 화면정의를 위해 만든 사용자 함수
    def initUI(self) -> None:
        self.setGeometry(300, 200, 600, 400)  # (300,200)좌표에 넓이 600, 높이 400짜리를 만드셈 -> 원하는 위치,크기 설정해주면됨
        self.setWindowTitle('QTemplate!!!')
        self.text = 'What a wonderful world~'
        self.show()

    def paintEvent(self, event) -> None:  # paintEvent는 사용자가 지정한게 아닌 여기 있는 함수
        paint = QPainter()
        paint.begin(self)
        # 무언가를 그리는 함수 추가
        self.drawText(event, paint)
        paint.end()

    # 텍스트 그리기 위한 사용자함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('NanumGothic', 20))
        paint.drawText(105, 100, 'HELL WORLD~')
        paint.setPen(QColor(0,250,10))
        paint.setFont(QFont('Impact', 15))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()