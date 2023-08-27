import sys
from PyQt5.QtWidgets import (QApplication, QWidget, # 애플리케이션 핸들러와 빈 GUI 위젯
                             QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon


class Calculator(QWidget): # QWidget 클래스를 상속방아서 클래스를 정의
    
    def __init__(self):
        super().__init__() # 부모 클래스 QWidget을 초기화
        self.initUI() # 나머지 초기화는 initUI 함수에 정의
        
    def initUI(self):
        self.btn1=QPushButton('Message',self)
        self.btn1.clicked.connect(self.activateMessage)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator') # 윈도에 표시되는 타이틀
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256) # 윈도 사이즈
        self.show() # 윈도 화면이 표시되도록 호출
        
    def activateMessage(self):
        QMessageBox.information(self,"information","Button clicked!")
        
        
if __name__ == '__main__': # pyqt는 애플리케이션 당 1개의 QApplication이 필요함
    app=QApplication(sys.argv) # QApplication 인스턴스 생성
    view=Calculator() # Calculator 윈도 인스턴스 생성
    sys.exit(app.exec_()) # 애플리케이션이 이벤트 처리를 하도록 루프 구동