

from PySide6.QtCore import Qt
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget
from Forms.main_ui import Ui_Form
from PySide6.QtSerialPort import *
import sys


class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.port = QSerialPort()
        # self.port.setOpenMode(QIODevice.OpenModeFlag.ReadWrite)
        self.port.setBaudRate(19200)
        ports =  QSerialPortInfo.availablePorts()
        self.ui.portsCombo.clear()
        for i in ports:
            self.ui.portsCombo.addItem(i.portName())
            print(i.portName())
        self.ui.speedSld.setMaximum(15)
        self.ui.holdSld.setMaximum(15)
        self.ui.connectBtn.clicked.connect(self.connect)
        self.ui.speedSld.valueChanged.connect(self.speedChange)
        self.ui.holdSld.valueChanged.connect(self.holdChange)
        self.ui.speedLine.setText(str(self.ui.speedSld.value()))
        self.ui.holdLine.setText(str(self.ui.holdSld.value()))
        self.port.readyRead.connect(self.portRead)


    def portRead(self):
        line =  self.port.readLine()
        if  line.contains(b"Speed"):
            print("fond Speed")
            self.ui.speedSld.setValue(int(line.toStdString().strip().split(" ")[1]))
        print(line)

    def connect(self):
        print("connect")
        portName = self.ui.portsCombo.currentText()
        self.port.setPortName(portName)
        self.port.open(QIODevice.OpenModeFlag.ReadWrite)

    def speedChange(self, val:int):
        print("speed" ,val)
        self.ui.speedLine.setText(str(val))

    def holdChange(self, val):
        print("hold", val)
        self.ui.holdLine.setText(str(val))

def main():
    app = QApplication(sys.argv)
    w = Window()
    
    w.show()
    app.exec()

if __name__ == "__main__":
    print("start code")
    main()

