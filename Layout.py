from PySide2.QtGui import QFont
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from Button import Button
from Timer import Timer
from Actions import Actions

class Layout(Button, Timer, Actions):
    def __init__(self, game_window):
        """
        Constructor
        :param game_window: Window for the game
        """
        Button.__init__(self)
        Timer.__init__(self)
        Actions.__init__(self)
        # Create game window
        self.game_window = game_window
        self.game_window.resize(470, 530)
        self.game_window.setMaximumSize(470, 530)
        self.game_window.setMinimumSize(470, 530)
        self.game_window.setWindowTitle("Minefield")
        self.game_window.setWindowIcon(self.icon_bomb)
        # Create central widget
        self.centralwidget = QWidget()
        self.game_window.setCentralWidget(self.centralwidget)
        # First line
        self.pushButtonA1 = QPushButton(self.centralwidget)
        self.pushButtonA1.setGeometry(QRect(10, 10, 30, 30))
        self.pushButtonA2 = QPushButton(self.centralwidget)
        self.pushButtonA2.setGeometry(QRect(40, 10, 30, 30))
        self.pushButtonA3 = QPushButton(self.centralwidget)
        self.pushButtonA3.setGeometry(QRect(70, 10, 30, 30))
        self.pushButtonA4 = QPushButton(self.centralwidget)
        self.pushButtonA4.setGeometry(QRect(100, 10, 30, 30))
        self.pushButtonA5 = QPushButton(self.centralwidget)
        self.pushButtonA5.setGeometry(QRect(130, 10, 30, 30))
        self.pushButtonA6 = QPushButton(self.centralwidget)
        self.pushButtonA6.setGeometry(QRect(160, 10, 30, 30))
        self.pushButtonA7 = QPushButton(self.centralwidget)
        self.pushButtonA7.setGeometry(QRect(190, 10, 30, 30))
        self.pushButtonA8 = QPushButton(self.centralwidget)
        self.pushButtonA8.setGeometry(QRect(220, 10, 30, 30))
        self.pushButtonA9 = QPushButton(self.centralwidget)
        self.pushButtonA9.setGeometry(QRect(250, 10, 30, 30))
        self.pushButtonA10 = QPushButton(self.centralwidget)
        self.pushButtonA10.setGeometry(QRect(280, 10, 30, 30))
        self.pushButtonA11 = QPushButton(self.centralwidget)
        self.pushButtonA11.setGeometry(QRect(310, 10, 30, 30))
        self.pushButtonA12 = QPushButton(self.centralwidget)
        self.pushButtonA12.setGeometry(QRect(340, 10, 30, 30))
        self.pushButtonA13 = QPushButton(self.centralwidget)
        self.pushButtonA13.setGeometry(QRect(370, 10, 30, 30))
        self.pushButtonA14 = QPushButton(self.centralwidget)
        self.pushButtonA14.setGeometry(QRect(400, 10, 30, 30))
        self.pushButtonA15 = QPushButton(self.centralwidget)
        self.pushButtonA15.setGeometry(QRect(430, 10, 30, 30))
        # Second line
        self.pushButtonB1 = QPushButton(self.centralwidget)
        self.pushButtonB1.setGeometry(QRect(10, 40, 30, 30))
        self.pushButtonB2 = QPushButton(self.centralwidget)
        self.pushButtonB2.setGeometry(QRect(40, 40, 30, 30))
        self.pushButtonB3 = QPushButton(self.centralwidget)
        self.pushButtonB3.setGeometry(QRect(70, 40, 30, 30))
        self.pushButtonB4 = QPushButton(self.centralwidget)
        self.pushButtonB4.setGeometry(QRect(100, 40, 30, 30))
        self.pushButtonB5 = QPushButton(self.centralwidget)
        self.pushButtonB5.setGeometry(QRect(130, 40, 30, 30))
        self.pushButtonB6 = QPushButton(self.centralwidget)
        self.pushButtonB6.setGeometry(QRect(160, 40, 30, 30))
        self.pushButtonB7 = QPushButton(self.centralwidget)
        self.pushButtonB7.setGeometry(QRect(190, 40, 30, 30))
        self.pushButtonB8 = QPushButton(self.centralwidget)
        self.pushButtonB8.setGeometry(QRect(220, 40, 30, 30))
        self.pushButtonB9 = QPushButton(self.centralwidget)
        self.pushButtonB9.setGeometry(QRect(250, 40, 30, 30))
        self.pushButtonB10 = QPushButton(self.centralwidget)
        self.pushButtonB10.setGeometry(QRect(280, 40, 30, 30))
        self.pushButtonB11 = QPushButton(self.centralwidget)
        self.pushButtonB11.setGeometry(QRect(310, 40, 30, 30))
        self.pushButtonB12 = QPushButton(self.centralwidget)
        self.pushButtonB12.setGeometry(QRect(340, 40, 30, 30))
        self.pushButtonB13 = QPushButton(self.centralwidget)
        self.pushButtonB13.setGeometry(QRect(370, 40, 30, 30))
        self.pushButtonB14 = QPushButton(self.centralwidget)
        self.pushButtonB14.setGeometry(QRect(400, 40, 30, 30))
        self.pushButtonB15 = QPushButton(self.centralwidget)
        self.pushButtonB15.setGeometry(QRect(430, 40, 30, 30))
        # Third line
        self.pushButtonC1 = QPushButton(self.centralwidget)
        self.pushButtonC1.setGeometry(QRect(10, 70, 30, 30))
        self.pushButtonC2 = QPushButton(self.centralwidget)
        self.pushButtonC2.setGeometry(QRect(40, 70, 30, 30))
        self.pushButtonC3 = QPushButton(self.centralwidget)
        self.pushButtonC3.setGeometry(QRect(70, 70, 30, 30))
        self.pushButtonC4 = QPushButton(self.centralwidget)
        self.pushButtonC4.setGeometry(QRect(100, 70, 30, 30))
        self.pushButtonC5 = QPushButton(self.centralwidget)
        self.pushButtonC5.setGeometry(QRect(130, 70, 30, 30))
        self.pushButtonC6 = QPushButton(self.centralwidget)
        self.pushButtonC6.setGeometry(QRect(160, 70, 30, 30))
        self.pushButtonC7 = QPushButton(self.centralwidget)
        self.pushButtonC7.setGeometry(QRect(190, 70, 30, 30))
        self.pushButtonC8 = QPushButton(self.centralwidget)
        self.pushButtonC8.setGeometry(QRect(220, 70, 30, 30))
        self.pushButtonC9 = QPushButton(self.centralwidget)
        self.pushButtonC9.setGeometry(QRect(250, 70, 30, 30))
        self.pushButtonC10 = QPushButton(self.centralwidget)
        self.pushButtonC10.setGeometry(QRect(280, 70, 30, 30))
        self.pushButtonC11 = QPushButton(self.centralwidget)
        self.pushButtonC11.setGeometry(QRect(310, 70, 30, 30))
        self.pushButtonC12 = QPushButton(self.centralwidget)
        self.pushButtonC12.setGeometry(QRect(340, 70, 30, 30))
        self.pushButtonC13 = QPushButton(self.centralwidget)
        self.pushButtonC13.setGeometry(QRect(370, 70, 30, 30))
        self.pushButtonC14 = QPushButton(self.centralwidget)
        self.pushButtonC14.setGeometry(QRect(400, 70, 30, 30))
        self.pushButtonC15 = QPushButton(self.centralwidget)
        self.pushButtonC15.setGeometry(QRect(430, 70, 30, 30))
        # Fourth line
        self.pushButtonD1 = QPushButton(self.centralwidget)
        self.pushButtonD1.setGeometry(QRect(10, 100, 30, 30))
        self.pushButtonD2 = QPushButton(self.centralwidget)
        self.pushButtonD2.setGeometry(QRect(40, 100, 30, 30))
        self.pushButtonD3 = QPushButton(self.centralwidget)
        self.pushButtonD3.setGeometry(QRect(70, 100, 30, 30))
        self.pushButtonD4 = QPushButton(self.centralwidget)
        self.pushButtonD4.setGeometry(QRect(100, 100, 30, 30))
        self.pushButtonD5 = QPushButton(self.centralwidget)
        self.pushButtonD5.setGeometry(QRect(130, 100, 30, 30))
        self.pushButtonD6 = QPushButton(self.centralwidget)
        self.pushButtonD6.setGeometry(QRect(160, 100, 30, 30))
        self.pushButtonD7 = QPushButton(self.centralwidget)
        self.pushButtonD7.setGeometry(QRect(190, 100, 30, 30))
        self.pushButtonD8 = QPushButton(self.centralwidget)
        self.pushButtonD8.setGeometry(QRect(220, 100, 30, 30))
        self.pushButtonD9 = QPushButton(self.centralwidget)
        self.pushButtonD9.setGeometry(QRect(250, 100, 30, 30))
        self.pushButtonD10 = QPushButton(self.centralwidget)
        self.pushButtonD10.setGeometry(QRect(280, 100, 30, 30))
        self.pushButtonD11 = QPushButton(self.centralwidget)
        self.pushButtonD11.setGeometry(QRect(310, 100, 30, 30))
        self.pushButtonD12 = QPushButton(self.centralwidget)
        self.pushButtonD12.setGeometry(QRect(340, 100, 30, 30))
        self.pushButtonD13 = QPushButton(self.centralwidget)
        self.pushButtonD13.setGeometry(QRect(370, 100, 30, 30))
        self.pushButtonD14 = QPushButton(self.centralwidget)
        self.pushButtonD14.setGeometry(QRect(400, 100, 30, 30))
        self.pushButtonD15 = QPushButton(self.centralwidget)
        self.pushButtonD15.setGeometry(QRect(430, 100, 30, 30))
        # Fiveth line
        self.pushButtonE1 = QPushButton(self.centralwidget)
        self.pushButtonE1.setGeometry(QRect(10, 130, 30, 30))
        self.pushButtonE2 = QPushButton(self.centralwidget)
        self.pushButtonE2.setGeometry(QRect(40, 130, 30, 30))
        self.pushButtonE3 = QPushButton(self.centralwidget)
        self.pushButtonE3.setGeometry(QRect(70, 130, 30, 30))
        self.pushButtonE4 = QPushButton(self.centralwidget)
        self.pushButtonE4.setGeometry(QRect(100, 130, 30, 30))
        self.pushButtonE5 = QPushButton(self.centralwidget)
        self.pushButtonE5.setGeometry(QRect(130, 130, 30, 30))
        self.pushButtonE6 = QPushButton(self.centralwidget)
        self.pushButtonE6.setGeometry(QRect(160, 130, 30, 30))
        self.pushButtonE7 = QPushButton(self.centralwidget)
        self.pushButtonE7.setGeometry(QRect(190, 130, 30, 30))
        self.pushButtonE8 = QPushButton(self.centralwidget)
        self.pushButtonE8.setGeometry(QRect(220, 130, 30, 30))
        self.pushButtonE9 = QPushButton(self.centralwidget)
        self.pushButtonE9.setGeometry(QRect(250, 130, 30, 30))
        self.pushButtonE10 = QPushButton(self.centralwidget)
        self.pushButtonE10.setGeometry(QRect(280, 130, 30, 30))
        self.pushButtonE11 = QPushButton(self.centralwidget)
        self.pushButtonE11.setGeometry(QRect(310, 130, 30, 30))
        self.pushButtonE12 = QPushButton(self.centralwidget)
        self.pushButtonE12.setGeometry(QRect(340, 130, 30, 30))
        self.pushButtonE13 = QPushButton(self.centralwidget)
        self.pushButtonE13.setGeometry(QRect(370, 130, 30, 30))
        self.pushButtonE14 = QPushButton(self.centralwidget)
        self.pushButtonE14.setGeometry(QRect(400, 130, 30, 30))
        self.pushButtonE15 = QPushButton(self.centralwidget)
        self.pushButtonE15.setGeometry(QRect(430, 130, 30, 30))
        # Sixth line
        self.pushButtonF1 = QPushButton(self.centralwidget)
        self.pushButtonF1.setGeometry(QRect(10, 160, 30, 30))
        self.pushButtonF2 = QPushButton(self.centralwidget)
        self.pushButtonF2.setGeometry(QRect(40, 160, 30, 30))
        self.pushButtonF3 = QPushButton(self.centralwidget)
        self.pushButtonF3.setGeometry(QRect(70, 160, 30, 30))
        self.pushButtonF4 = QPushButton(self.centralwidget)
        self.pushButtonF4.setGeometry(QRect(100, 160, 30, 30))
        self.pushButtonF5 = QPushButton(self.centralwidget)
        self.pushButtonF5.setGeometry(QRect(130, 160, 30, 30))
        self.pushButtonF6 = QPushButton(self.centralwidget)
        self.pushButtonF6.setGeometry(QRect(160, 160, 30, 30))
        self.pushButtonF7 = QPushButton(self.centralwidget)
        self.pushButtonF7.setGeometry(QRect(190, 160, 30, 30))
        self.pushButtonF8 = QPushButton(self.centralwidget)
        self.pushButtonF8.setGeometry(QRect(220, 160, 30, 30))
        self.pushButtonF9 = QPushButton(self.centralwidget)
        self.pushButtonF9.setGeometry(QRect(250, 160, 30, 30))
        self.pushButtonF10 = QPushButton(self.centralwidget)
        self.pushButtonF10.setGeometry(QRect(280, 160, 30, 30))
        self.pushButtonF11 = QPushButton(self.centralwidget)
        self.pushButtonF11.setGeometry(QRect(310, 160, 30, 30))
        self.pushButtonF12 = QPushButton(self.centralwidget)
        self.pushButtonF12.setGeometry(QRect(340, 160, 30, 30))
        self.pushButtonF13 = QPushButton(self.centralwidget)
        self.pushButtonF13.setGeometry(QRect(370, 160, 30, 30))
        self.pushButtonF14 = QPushButton(self.centralwidget)
        self.pushButtonF14.setGeometry(QRect(400, 160, 30, 30))
        self.pushButtonF15 = QPushButton(self.centralwidget)
        self.pushButtonF15.setGeometry(QRect(430, 160, 30, 30))
        # Seventh line
        self.pushButtonG1 = QPushButton(self.centralwidget)
        self.pushButtonG1.setGeometry(QRect(10, 190, 30, 30))
        self.pushButtonG2 = QPushButton(self.centralwidget)
        self.pushButtonG2.setGeometry(QRect(40, 190, 30, 30))
        self.pushButtonG3 = QPushButton(self.centralwidget)
        self.pushButtonG3.setGeometry(QRect(70, 190, 30, 30))
        self.pushButtonG4 = QPushButton(self.centralwidget)
        self.pushButtonG4.setGeometry(QRect(100, 190, 30, 30))
        self.pushButtonG5 = QPushButton(self.centralwidget)
        self.pushButtonG5.setGeometry(QRect(130, 190, 30, 30))
        self.pushButtonG6 = QPushButton(self.centralwidget)
        self.pushButtonG6.setGeometry(QRect(160, 190, 30, 30))
        self.pushButtonG7 = QPushButton(self.centralwidget)
        self.pushButtonG7.setGeometry(QRect(190, 190, 30, 30))
        self.pushButtonG8 = QPushButton(self.centralwidget)
        self.pushButtonG8.setGeometry(QRect(220, 190, 30, 30))
        self.pushButtonG9 = QPushButton(self.centralwidget)
        self.pushButtonG9.setGeometry(QRect(250, 190, 30, 30))
        self.pushButtonG10 = QPushButton(self.centralwidget)
        self.pushButtonG10.setGeometry(QRect(280, 190, 30, 30))
        self.pushButtonG11 = QPushButton(self.centralwidget)
        self.pushButtonG11.setGeometry(QRect(310, 190, 30, 30))
        self.pushButtonG12 = QPushButton(self.centralwidget)
        self.pushButtonG12.setGeometry(QRect(340, 190, 30, 30))
        self.pushButtonG13 = QPushButton(self.centralwidget)
        self.pushButtonG13.setGeometry(QRect(370, 190, 30, 30))
        self.pushButtonG14 = QPushButton(self.centralwidget)
        self.pushButtonG14.setGeometry(QRect(400, 190, 30, 30))
        self.pushButtonG15 = QPushButton(self.centralwidget)
        self.pushButtonG15.setGeometry(QRect(430, 190, 30, 30))
        # Eighth line
        self.pushButtonH1 = QPushButton(self.centralwidget)
        self.pushButtonH1.setGeometry(QRect(10, 220, 30, 30))
        self.pushButtonH2 = QPushButton(self.centralwidget)
        self.pushButtonH2.setGeometry(QRect(40, 220, 30, 30))
        self.pushButtonH3 = QPushButton(self.centralwidget)
        self.pushButtonH3.setGeometry(QRect(70, 220, 30, 30))
        self.pushButtonH4 = QPushButton(self.centralwidget)
        self.pushButtonH4.setGeometry(QRect(100, 220, 30, 30))
        self.pushButtonH5 = QPushButton(self.centralwidget)
        self.pushButtonH5.setGeometry(QRect(130, 220, 30, 30))
        self.pushButtonH6 = QPushButton(self.centralwidget)
        self.pushButtonH6.setGeometry(QRect(160, 220, 30, 30))
        self.pushButtonH7 = QPushButton(self.centralwidget)
        self.pushButtonH7.setGeometry(QRect(190, 220, 30, 30))
        self.pushButtonH8 = QPushButton(self.centralwidget)
        self.pushButtonH8.setGeometry(QRect(220, 220, 30, 30))
        self.pushButtonH9 = QPushButton(self.centralwidget)
        self.pushButtonH9.setGeometry(QRect(250, 220, 30, 30))
        self.pushButtonH10 = QPushButton(self.centralwidget)
        self.pushButtonH10.setGeometry(QRect(280, 220, 30, 30))
        self.pushButtonH11 = QPushButton(self.centralwidget)
        self.pushButtonH11.setGeometry(QRect(310, 220, 30, 30))
        self.pushButtonH12 = QPushButton(self.centralwidget)
        self.pushButtonH12.setGeometry(QRect(340, 220, 30, 30))
        self.pushButtonH13 = QPushButton(self.centralwidget)
        self.pushButtonH13.setGeometry(QRect(370, 220, 30, 30))
        self.pushButtonH14 = QPushButton(self.centralwidget)
        self.pushButtonH14.setGeometry(QRect(400, 220, 30, 30))
        self.pushButtonH15 = QPushButton(self.centralwidget)
        self.pushButtonH15.setGeometry(QRect(430, 220, 30, 30))
        # Nineth line
        self.pushButtonI1 = QPushButton(self.centralwidget)
        self.pushButtonI1.setGeometry(QRect(10, 250, 30, 30))
        self.pushButtonI2 = QPushButton(self.centralwidget)
        self.pushButtonI2.setGeometry(QRect(40, 250, 30, 30))
        self.pushButtonI3 = QPushButton(self.centralwidget)
        self.pushButtonI3.setGeometry(QRect(70, 250, 30, 30))
        self.pushButtonI4 = QPushButton(self.centralwidget)
        self.pushButtonI4.setGeometry(QRect(100, 250, 30, 30))
        self.pushButtonI5 = QPushButton(self.centralwidget)
        self.pushButtonI5.setGeometry(QRect(130, 250, 30, 30))
        self.pushButtonI6 = QPushButton(self.centralwidget)
        self.pushButtonI6.setGeometry(QRect(160, 250, 30, 30))
        self.pushButtonI7 = QPushButton(self.centralwidget)
        self.pushButtonI7.setGeometry(QRect(190, 250, 30, 30))
        self.pushButtonI8 = QPushButton(self.centralwidget)
        self.pushButtonI8.setGeometry(QRect(220, 250, 30, 30))
        self.pushButtonI9 = QPushButton(self.centralwidget)
        self.pushButtonI9.setGeometry(QRect(250, 250, 30, 30))
        self.pushButtonI10 = QPushButton(self.centralwidget)
        self.pushButtonI10.setGeometry(QRect(280, 250, 30, 30))
        self.pushButtonI11 = QPushButton(self.centralwidget)
        self.pushButtonI11.setGeometry(QRect(310, 250, 30, 30))
        self.pushButtonI12 = QPushButton(self.centralwidget)
        self.pushButtonI12.setGeometry(QRect(340, 250, 30, 30))
        self.pushButtonI13 = QPushButton(self.centralwidget)
        self.pushButtonI13.setGeometry(QRect(370, 250, 30, 30))
        self.pushButtonI14 = QPushButton(self.centralwidget)
        self.pushButtonI14.setGeometry(QRect(400, 250, 30, 30))
        self.pushButtonI15 = QPushButton(self.centralwidget)
        self.pushButtonI15.setGeometry(QRect(430, 250, 30, 30))
        # Tenth line
        self.pushButtonJ1 = QPushButton(self.centralwidget)
        self.pushButtonJ1.setGeometry(QRect(10, 280, 30, 30))
        self.pushButtonJ2 = QPushButton(self.centralwidget)
        self.pushButtonJ2.setGeometry(QRect(40, 280, 30, 30))
        self.pushButtonJ3 = QPushButton(self.centralwidget)
        self.pushButtonJ3.setGeometry(QRect(70, 280, 30, 30))
        self.pushButtonJ4 = QPushButton(self.centralwidget)
        self.pushButtonJ4.setGeometry(QRect(100, 280, 30, 30))
        self.pushButtonJ5 = QPushButton(self.centralwidget)
        self.pushButtonJ5.setGeometry(QRect(130, 280, 30, 30))
        self.pushButtonJ6 = QPushButton(self.centralwidget)
        self.pushButtonJ6.setGeometry(QRect(160, 280, 30, 30))
        self.pushButtonJ7 = QPushButton(self.centralwidget)
        self.pushButtonJ7.setGeometry(QRect(190, 280, 30, 30))
        self.pushButtonJ8 = QPushButton(self.centralwidget)
        self.pushButtonJ8.setGeometry(QRect(220, 280, 30, 30))
        self.pushButtonJ9 = QPushButton(self.centralwidget)
        self.pushButtonJ9.setGeometry(QRect(250, 280, 30, 30))
        self.pushButtonJ10 = QPushButton(self.centralwidget)
        self.pushButtonJ10.setGeometry(QRect(280, 280, 30, 30))
        self.pushButtonJ11 = QPushButton(self.centralwidget)
        self.pushButtonJ11.setGeometry(QRect(310, 280, 30, 30))
        self.pushButtonJ12 = QPushButton(self.centralwidget)
        self.pushButtonJ12.setGeometry(QRect(340, 280, 30, 30))
        self.pushButtonJ13 = QPushButton(self.centralwidget)
        self.pushButtonJ13.setGeometry(QRect(370, 280, 30, 30))
        self.pushButtonJ14 = QPushButton(self.centralwidget)
        self.pushButtonJ14.setGeometry(QRect(400, 280, 30, 30))
        self.pushButtonJ15 = QPushButton(self.centralwidget)
        self.pushButtonJ15.setGeometry(QRect(430, 280, 30, 30))
        # Eleventh line
        self.pushButtonK1 = QPushButton(self.centralwidget)
        self.pushButtonK1.setGeometry(QRect(10, 310, 30, 30))
        self.pushButtonK2 = QPushButton(self.centralwidget)
        self.pushButtonK2.setGeometry(QRect(40, 310, 30, 30))
        self.pushButtonK3 = QPushButton(self.centralwidget)
        self.pushButtonK3.setGeometry(QRect(70, 310, 30, 30))
        self.pushButtonK4 = QPushButton(self.centralwidget)
        self.pushButtonK4.setGeometry(QRect(100, 310, 30, 30))
        self.pushButtonK5 = QPushButton(self.centralwidget)
        self.pushButtonK5.setGeometry(QRect(130, 310, 30, 30))
        self.pushButtonK6 = QPushButton(self.centralwidget)
        self.pushButtonK6.setGeometry(QRect(160, 310, 30, 30))
        self.pushButtonK7 = QPushButton(self.centralwidget)
        self.pushButtonK7.setGeometry(QRect(190, 310, 30, 30))
        self.pushButtonK8 = QPushButton(self.centralwidget)
        self.pushButtonK8.setGeometry(QRect(220, 310, 30, 30))
        self.pushButtonK9 = QPushButton(self.centralwidget)
        self.pushButtonK9.setGeometry(QRect(250, 310, 30, 30))
        self.pushButtonK10 = QPushButton(self.centralwidget)
        self.pushButtonK10.setGeometry(QRect(280, 310, 30, 30))
        self.pushButtonK11 = QPushButton(self.centralwidget)
        self.pushButtonK11.setGeometry(QRect(310, 310, 30, 30))
        self.pushButtonK12 = QPushButton(self.centralwidget)
        self.pushButtonK12.setGeometry(QRect(340, 310, 30, 30))
        self.pushButtonK13 = QPushButton(self.centralwidget)
        self.pushButtonK13.setGeometry(QRect(370, 310, 30, 30))
        self.pushButtonK14 = QPushButton(self.centralwidget)
        self.pushButtonK14.setGeometry(QRect(400, 310, 30, 30))
        self.pushButtonK15 = QPushButton(self.centralwidget)
        self.pushButtonK15.setGeometry(QRect(430, 310, 30, 30))
        # Twelveth line
        self.pushButtonL1 = QPushButton(self.centralwidget)
        self.pushButtonL1.setGeometry(QRect(10, 340, 30, 30))
        self.pushButtonL2 = QPushButton(self.centralwidget)
        self.pushButtonL2.setGeometry(QRect(40, 340, 30, 30))
        self.pushButtonL3 = QPushButton(self.centralwidget)
        self.pushButtonL3.setGeometry(QRect(70, 340, 30, 30))
        self.pushButtonL4 = QPushButton(self.centralwidget)
        self.pushButtonL4.setGeometry(QRect(100, 340, 30, 30))
        self.pushButtonL5 = QPushButton(self.centralwidget)
        self.pushButtonL5.setGeometry(QRect(130, 340, 30, 30))
        self.pushButtonL6 = QPushButton(self.centralwidget)
        self.pushButtonL6.setGeometry(QRect(160, 340, 30, 30))
        self.pushButtonL7 = QPushButton(self.centralwidget)
        self.pushButtonL7.setGeometry(QRect(190, 340, 30, 30))
        self.pushButtonL8 = QPushButton(self.centralwidget)
        self.pushButtonL8.setGeometry(QRect(220, 340, 30, 30))
        self.pushButtonL9 = QPushButton(self.centralwidget)
        self.pushButtonL9.setGeometry(QRect(250, 340, 30, 30))
        self.pushButtonL10 = QPushButton(self.centralwidget)
        self.pushButtonL10.setGeometry(QRect(280, 340, 30, 30))
        self.pushButtonL11 = QPushButton(self.centralwidget)
        self.pushButtonL11.setGeometry(QRect(310, 340, 30, 30))
        self.pushButtonL12 = QPushButton(self.centralwidget)
        self.pushButtonL12.setGeometry(QRect(340, 340, 30, 30))
        self.pushButtonL13 = QPushButton(self.centralwidget)
        self.pushButtonL13.setGeometry(QRect(370, 340, 30, 30))
        self.pushButtonL14 = QPushButton(self.centralwidget)
        self.pushButtonL14.setGeometry(QRect(400, 340, 30, 30))
        self.pushButtonL15 = QPushButton(self.centralwidget)
        self.pushButtonL15.setGeometry(QRect(430, 340, 30, 30))
        # Thirteenth line
        self.pushButtonM1 = QPushButton(self.centralwidget)
        self.pushButtonM1.setGeometry(QRect(10, 370, 30, 30))
        self.pushButtonM2 = QPushButton(self.centralwidget)
        self.pushButtonM2.setGeometry(QRect(40, 370, 30, 30))
        self.pushButtonM3 = QPushButton(self.centralwidget)
        self.pushButtonM3.setGeometry(QRect(70, 370, 30, 30))
        self.pushButtonM4 = QPushButton(self.centralwidget)
        self.pushButtonM4.setGeometry(QRect(100, 370, 30, 30))
        self.pushButtonM5 = QPushButton(self.centralwidget)
        self.pushButtonM5.setGeometry(QRect(130, 370, 30, 30))
        self.pushButtonM6 = QPushButton(self.centralwidget)
        self.pushButtonM6.setGeometry(QRect(160, 370, 30, 30))
        self.pushButtonM7 = QPushButton(self.centralwidget)
        self.pushButtonM7.setGeometry(QRect(190, 370, 30, 30))
        self.pushButtonM8 = QPushButton(self.centralwidget)
        self.pushButtonM8.setGeometry(QRect(220, 370, 30, 30))
        self.pushButtonM9 = QPushButton(self.centralwidget)
        self.pushButtonM9.setGeometry(QRect(250, 370, 30, 30))
        self.pushButtonM10 = QPushButton(self.centralwidget)
        self.pushButtonM10.setGeometry(QRect(280, 370, 30, 30))
        self.pushButtonM11 = QPushButton(self.centralwidget)
        self.pushButtonM11.setGeometry(QRect(310, 370, 30, 30))
        self.pushButtonM12 = QPushButton(self.centralwidget)
        self.pushButtonM12.setGeometry(QRect(340, 370, 30, 30))
        self.pushButtonM13 = QPushButton(self.centralwidget)
        self.pushButtonM13.setGeometry(QRect(370, 370, 30, 30))
        self.pushButtonM14 = QPushButton(self.centralwidget)
        self.pushButtonM14.setGeometry(QRect(400, 370, 30, 30))
        self.pushButtonM15 = QPushButton(self.centralwidget)
        self.pushButtonM15.setGeometry(QRect(430, 370, 30, 30))
        # Fourteenth line
        self.pushButtonN1 = QPushButton(self.centralwidget)
        self.pushButtonN1.setGeometry(QRect(10, 400, 30, 30))
        self.pushButtonN2 = QPushButton(self.centralwidget)
        self.pushButtonN2.setGeometry(QRect(40, 400, 30, 30))
        self.pushButtonN3 = QPushButton(self.centralwidget)
        self.pushButtonN3.setGeometry(QRect(70, 400, 30, 30))
        self.pushButtonN4 = QPushButton(self.centralwidget)
        self.pushButtonN4.setGeometry(QRect(100, 400, 30, 30))
        self.pushButtonN5 = QPushButton(self.centralwidget)
        self.pushButtonN5.setGeometry(QRect(130, 400, 30, 30))
        self.pushButtonN6 = QPushButton(self.centralwidget)
        self.pushButtonN6.setGeometry(QRect(160, 400, 30, 30))
        self.pushButtonN7 = QPushButton(self.centralwidget)
        self.pushButtonN7.setGeometry(QRect(190, 400, 30, 30))
        self.pushButtonN8 = QPushButton(self.centralwidget)
        self.pushButtonN8.setGeometry(QRect(220, 400, 30, 30))
        self.pushButtonN9 = QPushButton(self.centralwidget)
        self.pushButtonN9.setGeometry(QRect(250, 400, 30, 30))
        self.pushButtonN10 = QPushButton(self.centralwidget)
        self.pushButtonN10.setGeometry(QRect(280, 400, 30, 30))
        self.pushButtonN11 = QPushButton(self.centralwidget)
        self.pushButtonN11.setGeometry(QRect(310, 400, 30, 30))
        self.pushButtonN12 = QPushButton(self.centralwidget)
        self.pushButtonN12.setGeometry(QRect(340, 400, 30, 30))
        self.pushButtonN13 = QPushButton(self.centralwidget)
        self.pushButtonN13.setGeometry(QRect(370, 400, 30, 30))
        self.pushButtonN14 = QPushButton(self.centralwidget)
        self.pushButtonN14.setGeometry(QRect(400, 400, 30, 30))
        self.pushButtonN15 = QPushButton(self.centralwidget)
        self.pushButtonN15.setGeometry(QRect(430, 400, 30, 30))
        # Fiveteenth line
        self.pushButtonO1 = QPushButton(self.centralwidget)
        self.pushButtonO1.setGeometry(QRect(10, 430, 30, 30))
        self.pushButtonO2 = QPushButton(self.centralwidget)
        self.pushButtonO2.setGeometry(QRect(40, 430, 30, 30))
        self.pushButtonO3 = QPushButton(self.centralwidget)
        self.pushButtonO3.setGeometry(QRect(70, 430, 30, 30))
        self.pushButtonO4 = QPushButton(self.centralwidget)
        self.pushButtonO4.setGeometry(QRect(100, 430, 30, 30))
        self.pushButtonO5 = QPushButton(self.centralwidget)
        self.pushButtonO5.setGeometry(QRect(130, 430, 30, 30))
        self.pushButtonO6 = QPushButton(self.centralwidget)
        self.pushButtonO6.setGeometry(QRect(160, 430, 30, 30))
        self.pushButtonO7 = QPushButton(self.centralwidget)
        self.pushButtonO7.setGeometry(QRect(190, 430, 30, 30))
        self.pushButtonO8 = QPushButton(self.centralwidget)
        self.pushButtonO8.setGeometry(QRect(220, 430, 30, 30))
        self.pushButtonO9 = QPushButton(self.centralwidget)
        self.pushButtonO9.setGeometry(QRect(250, 430, 30, 30))
        self.pushButtonO10 = QPushButton(self.centralwidget)
        self.pushButtonO10.setGeometry(QRect(280, 430, 30, 30))
        self.pushButtonO11 = QPushButton(self.centralwidget)
        self.pushButtonO11.setGeometry(QRect(310, 430, 30, 30))
        self.pushButtonO12 = QPushButton(self.centralwidget)
        self.pushButtonO12.setGeometry(QRect(340, 430, 30, 30))
        self.pushButtonO13 = QPushButton(self.centralwidget)
        self.pushButtonO13.setGeometry(QRect(370, 430, 30, 30))
        self.pushButtonO14 = QPushButton(self.centralwidget)
        self.pushButtonO14.setGeometry(QRect(400, 430, 30, 30))
        self.pushButtonO15 = QPushButton(self.centralwidget)
        self.pushButtonO15.setGeometry(QRect(430, 430, 30, 30))
        # Button flag
        self.pushButtonFlag = QPushButton(self.centralwidget)
        self.pushButtonFlag.setGeometry(QRect(10, 470, 30, 30))
        self.pushButtonFlag.clicked.connect(self.toggle_flag_status)
        self.pushButtonFlag.setIcon(self.icon_flag_off)
        self.pushButtonFlag.setIconSize(QSize(28, 28))
        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_event)
        self.timer_label = QLineEdit(self.centralwidget)
        self.timer_label.setGeometry(QRect(190, 470, 90, 30))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont().setWeight(25))
        self.timer_label.setReadOnly(True)
        # Create bombs label
        self.bombs_label = QLineEdit(self.centralwidget)
        self.bombs_label.setGeometry(QRect(400, 470, 60, 30))
        self.bombs_label.setAlignment(Qt.AlignCenter)
        self.bombs_label.setFont(QFont().setWeight(25))
        self.bombs_label.setReadOnly(True)
        # Create actions
        self.action_records = QAction('Records', self)
        self.action_records.setShortcut('Ctrl+F')
        self.action_records.triggered.connect(lambda: self.show_records(self))
        self.action_erase_records = QAction('Erase records', self)
        self.action_erase_records.setShortcut('Ctrl+D')
        self.action_erase_records.triggered.connect(lambda : self.erase_records(self))
        # Create menu bar
        self.menu = QMenu('Menu', self)
        self.menu.addAction(self.action_records)
        self.menu.addAction(self.action_erase_records)
        self.menubar = self.menuBar()
        self.menubar.addMenu(self.menu)
