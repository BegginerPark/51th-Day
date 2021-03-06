import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

form_class = uic.loadUiType("bull.ui")[0]

tickers = ["BTC", "ETH", "BCH", "ETC"]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        for i, ticker in enumerate(tickers):
            ticker_item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, ticker_item)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()