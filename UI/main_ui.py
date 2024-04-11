# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #3a3a3a;")
        self.top = QFrame(self.centralwidget)
        self.top.setObjectName(u"top")
        self.top.setGeometry(QRect(0, 0, 600, 211))
        self.top.setStyleSheet(u"background-color: #e4e734;")
        self.top.setFrameShape(QFrame.Shape.StyledPanel)
        self.top.setFrameShadow(QFrame.Shadow.Raised)
        self.label4 = QLabel(self.top)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(170, 20, 273, 32))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label4.setFont(font)
        self.label5 = QLabel(self.top)
        self.label5.setObjectName(u"label5")
        self.label5.setGeometry(QRect(170, 60, 271, 141))
        self.label5.setPixmap(QPixmap(u"media/free-icon-money-exchange-8350929.png"))
        self.label5.setScaledContents(True)
        self.down = QWidget(self.centralwidget)
        self.down.setObjectName(u"down")
        self.down.setGeometry(QRect(0, 210, 600, 401))
        self.down.setStyleSheet(u"background-color: rgb(52, 52, 52);")
        self.trigger = QPushButton(self.down)
        self.trigger.setObjectName(u"trigger")
        self.trigger.setGeometry(QRect(220, 350, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.trigger.setFont(font1)
        self.trigger.setStyleSheet(u"QPushButton{\n"
"	background-color: #e4e734;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(52, 52, 52);\n"
"	border: 2px solid #e4e734;\n"
"}\n"
"	")
        self.widget = QWidget(self.down)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(190, 10, 191, 311))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.widget)
        self.label1.setObjectName(u"label1")
        self.label1.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label1.setFont(font2)
        self.label1.setStyleSheet(u"color: white;\n"
"")
        self.label1.setScaledContents(False)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setWordWrap(False)

        self.verticalLayout.addWidget(self.label1)

        self.fromm = QLineEdit(self.widget)
        self.fromm.setObjectName(u"fromm")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromm.sizePolicy().hasHeightForWidth())
        self.fromm.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.fromm.setFont(font3)
        self.fromm.setStyleSheet(u"border: 2px solid #e4e734;\n"
"border-radius: 10px;")
        self.fromm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.fromm)

        self.label2 = QLabel(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font2)
        self.label2.setStyleSheet(u"color: white;")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label2)

        self.to = QLineEdit(self.widget)
        self.to.setObjectName(u"to")
        sizePolicy.setHeightForWidth(self.to.sizePolicy().hasHeightForWidth())
        self.to.setSizePolicy(sizePolicy)
        self.to.setFont(font3)
        self.to.setStyleSheet(u"border: 2px solid #e4e734;\n"
"border-radius: 10px;")
        self.to.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.to)

        self.label3 = QLabel(self.widget)
        self.label3.setObjectName(u"label3")
        self.label3.setFont(font2)
        self.label3.setStyleSheet(u"color: white;")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label3)

        self.sum = QLineEdit(self.widget)
        self.sum.setObjectName(u"sum")
        sizePolicy.setHeightForWidth(self.sum.sizePolicy().hasHeightForWidth())
        self.sum.setSizePolicy(sizePolicy)
        self.sum.setFont(font3)
        self.sum.setStyleSheet(u"border: 2px solid #e4e734;\n"
"border-radius: 10px;")
        self.sum.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.sum)

        self.final_text = QLabel(self.widget)
        self.final_text.setObjectName(u"final_text")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(True)
        self.final_text.setFont(font4)
        self.final_text.setStyleSheet(u"color: white;")
        self.final_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.final_text)

        self.result = QLineEdit(self.widget)
        self.result.setObjectName(u"result")
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        self.result.setFont(font3)
        self.result.setStyleSheet(u"border: 2px solid #e4e734;\n"
"border-radius: 10px;")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.result)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041d\u0412\u0415\u0420\u0422\u0415\u0420 \u0412\u0410\u041b\u042e\u0422", None))
        self.label5.setText("")
        self.trigger.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0415\u041e\u0411\u0420\u0410\u0417\u041e\u0412\u0410\u0422\u042c", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0417", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"\u0412", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0423\u041c\u041c\u0410", None))
        self.final_text.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0415\u0417\u0423\u041b\u042c\u0422\u0410\u0422", None))
    # retranslateUi

