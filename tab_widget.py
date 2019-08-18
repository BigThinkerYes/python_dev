import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget")
        self.setGeometry(350,150,600,600)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()

        #   tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        #   define tabs
        self.tabs.addTab(self.tab1,"First Tab")
        self.tabs.addTab(self.tab2,"Second Tab")
        self.tabs.addTab(self.tab3,"Last Tab")

        #   widgets
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addStretch()

        self.text = QLabel("Hello Python")
        self.btn1 = QPushButton("First Tab")

        self.btn1.clicked.connect(self.btnFunc)

        self.btn2 = QPushButton("Second Tab")

        vbox.addWidget(self.text)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addStretch() # center the button
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

        self.show()

    #   make the body change when button is clicked
    def btnFunc(self):
        self.text.setText("Button is activated")

def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()