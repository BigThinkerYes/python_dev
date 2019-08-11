import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using List boxes")
        self.setGeometry(250,150,500,500)
        self.UI()


    def UI(self):
        self.combo=QComboBox(self)
        self.combo.move(150,100)
        button=QPushButton("Save",self)
        button.move(150,130)
        button.clicked.connect(self.getValue)
        self.combo.addItem("Python")
        self.combo.addItems(["C","C#","PHP"])
        list1=["num1","num2","num3"]

        for name in list1:
            self.combo.addItem(name)

        self.show()

    def getValue(self):
        value=self.combo.currentText()
        print(value)


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()