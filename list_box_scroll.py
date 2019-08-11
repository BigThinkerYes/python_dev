import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("radio buttons")
        self.setGeometry(50,50,500,500)
        self.UI()


    def UI(self):
        self.spinBox=QSpinBox(self)
        self.spinBox.move(150,100)
        self.spinBox.setFont(font)
        # self.spinBox.setMinimum(25)
        # self.spinBox.setMaximum(110)
        self.spinBox.setRange(25,110)

        # using the money sign
        # self.pinBox.setPrefix("$ ")

        # using measurements
        self.spinBox.setSuffix(" cm")

        # increase by 5 on each click
        self.spinBox.setSingleStep(5)

        # print value use connect
        # self.spinBox.valueChanged.connect(self.getValue)

        # use button to print to screen
        button=QPushButton("Send",self)
        button.move(150, 140)
        button.clicked.connect(self.getValue)

        self.show()

    # used to print the value
    def getValue(self):
        value=self.spinBox.value()
        print(value)

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()