import sys
from PyQt5.QtWidgets import *
#dynamic center buttons with addStretch()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        formLayout=QFormLayout()

        name_txt = QLabel("Name: ")
        name_input = QLineEdit()
        pass_txt = QLabel("Password :")
        pass_input = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addStretch()  # shrink buttons down

        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        #   hbox make name box into two fields
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())

        formLayout.addRow(name_txt,hbox1)
        formLayout.addRow(pass_txt,pass_input)
        formLayout.addRow(QLabel("Country :"),QComboBox())
        formLayout.addRow(hbox)

        self.setLayout(formLayout)
        self.show()

def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()