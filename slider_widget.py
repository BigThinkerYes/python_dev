import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("slider Layout")
        self.setGeometry(350,150,600,500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)

        self.slider.valueChanged.connect(self.getValue)

        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2 = QLabel("Hello Python")

        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)
        self.setLayout(vbox)

        self.show()

    #   make connect print to terminal
    def getValue(self):
        val = self.slider.value()
        print(val)
        #   make value change inside the program
        self.text1.setText(str(val))

        #   scale the font text size
        fontSize = self.slider.value()
        font=QFont("Times",fontSize)
        self.text2.setFont(font)

def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()