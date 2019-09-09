import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt,QTimer
import random
from pygame import mixer
from mutagen.mp3 import MP3


musicList=[]
mixer.init()
muted=False
count = 0

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450,35,480,700)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
    ################### progress bar ######################
    def widgets(self):
        ################### progress bar ######################
        self.progressBar=QProgressBar()

        ################### buttons ######################
        self.addButton = QToolButton()
        self.addButton.setIcon(QIcon("icons/add.png"))
        self.addButton.setIconSize(QSize(48,48))
        self.addButton.setToolTip("Add a Song")
        self.addButton.clicked.connect(self.addSound)

        self.shuffleButton = QToolButton()
        self.shuffleButton.setIcon(QIcon("icons/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48, 48))
        self.shuffleButton.setToolTip("Shuffle the list")
        self.shuffleButton.clicked.connect(self.shufflePlayList)

        self.previousButton = QToolButton()
        self.previousButton.setIcon(QIcon("icons/previous.png"))
        self.previousButton.setIconSize(QSize(48, 48))
        self.previousButton.setToolTip("Play Previous")

        self.playButton = QToolButton()
        self.playButton.setIcon(QIcon("icons/play.png"))
        self.playButton.setIconSize(QSize(48, 48))
        self.playButton.setToolTip("Play")
        self.playButton.clicked.connect(self.playSounds)

        self.nextButton = QToolButton()
        self.nextButton.setIcon(QIcon("icons/next.png"))
        self.nextButton.setIconSize(QSize(48, 48))
        self.nextButton.setToolTip("Play Next")

        self.muteButton = QToolButton()
        self.muteButton.setIcon(QIcon("icons/mute.png"))
        self.muteButton.setIconSize(QSize(48, 48))
        self.muteButton.setToolTip("Mute")
        self.muteButton.clicked.connect(self.muteSound)

        ################### volume slider ########################
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setToolTip("Volume")
        #controls
        self.volumeSlider.setValue(70)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        mixer.music.set_volume(0.7)
        self.volumeSlider.valueChanged.connect(self.setVolume)

        ##################### Play List #########################
        self.playList = QListWidget()
        self.playList.doubleClicked.connect(self.playSounds)

        ################### Timer #######################
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateProgressBar)

    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topMainLayout=QVBoxLayout()
        self.topGroupBox=QGroupBox("Music Player",self)
        self.topGroupBox.setStyleSheet("background-color:#607D8B")
        self.topLayout=QHBoxLayout()
        self.middleLayout=QHBoxLayout()
        self.bottomLayout=QVBoxLayout()

        #   widgets top layout
        ################### progress bar ######################
        self.topLayout.addWidget(self.progressBar)

        #   middle layout
        ################### buttons ######################
        self.middleLayout.addStretch()
        self.middleLayout.addWidget(self.addButton)
        self.middleLayout.addWidget(self.shuffleButton)
        self.middleLayout.addWidget(self.playButton)
        self.middleLayout.addWidget(self.previousButton)
        self.middleLayout.addWidget(self.nextButton)
        self.middleLayout.addWidget(self.volumeSlider)
        self.middleLayout.addWidget(self.muteButton)
        self.middleLayout.addStretch()

        ## bottom layout widget
        self.bottomLayout.addWidget(self.playList)
        #

        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)

        self.topGroupBox.setLayout(self.topMainLayout)

        self.mainLayout.addWidget(self.topGroupBox)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

    ##### button functions
    def addSound(self):
        directory=QFileDialog.getOpenFileName(self,"Add Sound","","Sound Files (*.mp3 *.ogg *.wav)")
        print(directory)
        filename=os.path.basename(directory[0])
        print(filename)
        self.playList.addItem(filename)
        musicList.append(directory[0])

    def shufflePlayList(self):
        random.shuffle(musicList)
        print(musicList)
        self.playList.clear()

        for song in musicList:
            filename=os.path.basename(song)
            self.playList.addItem(filename)

    def playSounds(self):
        index=self.playList.currentRow()
        # print(index)
        # print(musicList[index])

        try:
            mixer.music.load(str(musicList[index]))
            mixer.music.play()
            self.timer.start() # used to update progress bar

            sound=MP3(str(musicList[index]))
            songLength=sound.info.length
            songLength=round(songLength)
            print(songLength)

        except:
            pass

    def setVolume(self):
        self.volume=self.volumeSlider.value()
        # print(self.volume)
        mixer.music.set_volume(self.volume/100)

    def muteSound(self):
        global muted

        if muted == False:
            mixer.music.set_volume(0.0)
            muted = True
            self.muteButton.setIcon(QIcon("icons/unmuted.png"))
            self.muteButton.setToolTip("UnMute")
            self.volumeSlider.setValue(0)
        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.muteButton.setToolTip("Mute")
            self.muteButton.setIcon(QIcon("icons/mute.png"))
            self.volumeSlider.setValue(70)

    def updateProgressBar(self):
        global count
        count +=1
        self.progressBar.setValue(count)


def main():
    App=QApplication(sys.argv)
    window=Player()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()