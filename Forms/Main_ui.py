# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(742, 770)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.portsCombo = QComboBox(self.groupBox)
        self.portsCombo.setObjectName(u"portsCombo")
        self.portsCombo.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.portsCombo)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.connectBtn = QPushButton(self.groupBox)
        self.connectBtn.setObjectName(u"connectBtn")

        self.horizontalLayout.addWidget(self.connectBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.groupBox_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        icon = QIcon(QIcon.fromTheme(u"text-x-generic"))
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.speedSld = QSlider(self.groupBox_3)
        self.speedSld.setObjectName(u"speedSld")
        self.speedSld.setOrientation(Qt.Orientation.Horizontal)
        self.speedSld.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.speedSld.setTickInterval(6)

        self.verticalLayout_3.addWidget(self.speedSld)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.speedLine = QLineEdit(self.groupBox_3)
        self.speedLine.setObjectName(u"speedLine")
        self.speedLine.setMinimumSize(QSize(60, 0))
        self.speedLine.setMaximumSize(QSize(60, 16777215))
        self.speedLine.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.speedLine)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.holdSld = QSlider(self.groupBox_3)
        self.holdSld.setObjectName(u"holdSld")
        self.holdSld.setOrientation(Qt.Orientation.Horizontal)
        self.holdSld.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.holdSld.setTickInterval(5)

        self.verticalLayout.addWidget(self.holdSld)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.holdLine = QLineEdit(self.groupBox_3)
        self.holdLine.setObjectName(u"holdLine")
        self.holdLine.setMaximumSize(QSize(60, 16777215))
        self.holdLine.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.holdLine)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"LedDisplay", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Connection", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Auto Connect", None))
        self.connectBtn.setText(QCoreApplication.translate("Form", u"connect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"TextEdit", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Text", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Align", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Speed", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Hold", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"ABCDEFEF", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

