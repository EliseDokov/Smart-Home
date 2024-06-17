#import sys
#from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
#from PyQt5.QtCore import QTimer, QTime, Qt
#
#
#class LiveClock(QWidget):
#    def __init__(self):
#        super().__init__()
#
#        self.initUI()
#
#        # Set up a timer to update the clock every second
#        timer = QTimer(self)
#        timer.timeout.connect(self.updateTime)
#        # Update every second
#        timer.start(1000)
#        # Initial time display
#        self.updateTime()
#
#    def initUI(self):
#        self.setWindowTitle('Live Clock')
#
#        # Create a layout and a label to show the time
#        layout = QVBoxLayout()
#        self.timeLabel = QLabel(self)
#        self.timeLabel.setAlignment(Qt.AlignCenter)
#        layout.addWidget(self.timeLabel)
#
#        self.setLayout(layout)
#        self.resize(200, 100)
#
#    def updateTime(self):
#        # Get the current time in 24-hour format
#        currentTime = QTime.currentTime().toString('HH:mm:ss')
#        self.timeLabel.setText(currentTime)
#
#
#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    clock = LiveClock()
#    clock.show()
#    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QLabel,
                             QVBoxLayout, QWidget, QMainWindow)
from PyQt5.QtCore import QTimer, QTime, Qt


class LiveClock(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Set up a timer to update the clock every second
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)  # Update every second

        self.updateTime()  # Initial time display

    def initUI(self):
        # Create a layout and a label to show the time
        layout = QVBoxLayout()
        self.timeLabel = QLabel(self)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timeLabel)
        self.setLayout(layout)
        self.resize(200, 100)

    def updateTime(self):
        # Get the current time in 24-hour format
        currentTime = QTime.currentTime().toString('HH:mm:ss')
        self.timeLabel.setText(currentTime)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Application with Live Clock')

        # Create the central widget and layout
        centralWidget = QWidget()
        layout = QVBoxLayout()

        # Add your existing widgets to the layout
        # For example, add a placeholder label
        label = QLabel('Main Application Content', self)
        layout.addWidget(label)

        # Create an instance of LiveClock and add it to the layout
        clock = LiveClock()
        layout.addWidget(clock)

        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.resize(400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
