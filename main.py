from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from  PyQt5.QtCore import *
from  PyQt5.QtGui import *
from  PyQt5.QtWidgets import *
import os
import sys
import subprocess
from PyQt5.QtWidgets import QMessageBox
import threading
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import user_rc
import db
from time import sleep
from functools import partial
import invoice
import schedule
import datetime
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1378, 702)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_15 = QtWidgets.QWidget(self.centralwidget)
        self.widget_15.setEnabled(True)
        self.widget_15.setMinimumSize(QtCore.QSize(1055, 60))
        self.widget_15.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_15.setStyleSheet("")
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_25 = QtWidgets.QFrame(self.widget_15)
        self.frame_25.setMinimumSize(QtCore.QSize(600, 60))
        self.frame_25.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_7.setContentsMargins(0, -1, 200, -1)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_53 = QtWidgets.QLabel(self.frame_25)
        self.label_53.setMinimumSize(QtCore.QSize(198, 0))
        self.label_53.setMaximumSize(QtCore.QSize(198, 40))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_7.addWidget(self.label_53, 0, QtCore.Qt.AlignLeft)
        self.line = QtWidgets.QFrame(self.frame_25)
        self.line.setStyleSheet("background-color: rgb(105, 59, 177);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        self.label_54 = QtWidgets.QLabel(self.frame_25)
        self.label_54.setMinimumSize(QtCore.QSize(380, 0))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_7.addWidget(self.label_54, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_4.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.widget_15)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_2.setContentsMargins(30, 12, 30, 20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_12.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_12.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"border-radius : 17px; \n"
"\n"
"background-repeat:none;\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(252, 252, 252);\n"
"qproperty-icon:url(:/newPrefix/switch.png);\n"
"qproperty-iconSize: 30px;\n"
"background-repeat:none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(234, 234, 234);\n"
"    \n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_26, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.widget_15)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(108, 61, 183);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_81 = QtWidgets.QFrame(self.frame_2)
        self.frame_81.setMaximumSize(QtCore.QSize(188, 16777215))
        self.frame_81.setStyleSheet("background-color: rgb(108, 61, 183);")
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_81)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"qproperty-icon: url(:/newPrefix/icons8-customer-64.png);\n"
"qproperty-iconSize: 30px;\n"
"background-repeat:none;\n"
"border-radius:1px;\n"
"text-align: left; \n"
"border-left: 15px solid rgb(108, 61, 183);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(98, 55, 166);\n"
"    border-left: 15px solid rgb(98, 55, 166);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(78, 44, 132);\n"
"    border-left: 15px solid  rgb(78, 44, 132);\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_2.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_25.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"qproperty-icon: url(:/newPrefix/icons8-new-product-64.png);\n"
"qproperty-iconSize: 30px;\n"
"background-repeat:none;\n"
"border-radius:1px;\n"
"text-align: left; \n"
"border-left: 15px solid rgb(108, 61, 183);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(98, 55, 166);\n"
"    border-left: 15px solid rgb(98, 55, 166);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(78, 44, 132);\n"
"    border-left: 15px solid  rgb(78, 44, 132);\n"
"}")
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_2.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_26.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_26.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"qproperty-icon:url(:/newPrefix/icons8-shopping-cart-64.png);\n"
"qproperty-iconSize: 30px;\n"
"background-repeat:none;\n"
"border-radius:1px;\n"
"text-align: left; \n"
"border-left: 15px solid rgb(108, 61, 183);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(98, 55, 166);\n"
"    border-left: 15px solid rgb(98, 55, 166);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(78, 44, 132);\n"
"    border-left: 15px solid  rgb(78, 44, 132);\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_2.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"qproperty-icon:url(:/newPrefix/icons8-settings-64.png);\n"
"qproperty-iconSize: 30px;\n"
"background-repeat:none;\n"
"border-radius:1px;\n"
"text-align: left; \n"
"border-left: 15px solid rgb(108, 61, 183);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(98, 55, 166);\n"
"    border-left: 15px solid rgb(98, 55, 166);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(78, 44, 132);\n"
"    border-left: 15px solid  rgb(78, 44, 132);\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_2.addWidget(self.pushButton_27)


        self.pushButton_schedule = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_schedule.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_schedule.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_schedule.setFont(font)
        self.pushButton_schedule.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"background:transparent;\n"
"qproperty-icon:url(:/newPrefix/icons-sechdule.png);\n"
"qproperty-iconSize: 30px;\n"
"background-repeat:none;\n"
"border-radius:1px;\n"
"text-align: left; \n"
"border-left: 15px solid rgb(108, 61, 183);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(98, 55, 166);\n"
"    border-left: 15px solid rgb(98, 55, 166);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(78, 44, 132);\n"
"    border-left: 15px solid  rgb(78, 44, 132);\n"
"}")
        self.pushButton_schedule.setObjectName("pushButton_schedule")
        self.verticalLayout_2.addWidget(self.pushButton_schedule)

        self.horizontalLayout_2.addWidget(self.frame_81, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setStyleSheet("background-color:rgb(238, 235, 241)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.page_12)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.frame_50 = QtWidgets.QFrame(self.page_12)
        self.frame_50.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_50.setStyleSheet("text-align:center;")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_50)
        self.frame_3.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_180 = QtWidgets.QFrame(self.frame_3)
        self.frame_180.setMinimumSize(QtCore.QSize(400, 300))
        self.frame_180.setMaximumSize(QtCore.QSize(400, 440))
        self.frame_180.setStyleSheet("image:none;\n"
"background-color: rgb(250, 250, 250);\n"
"border-radius:19px;")
        self.frame_180.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_180.setObjectName("frame_180")
        self.verticalLayout_168 = QtWidgets.QVBoxLayout(self.frame_180)
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName("verticalLayout_168")
        self.frame_181 = QtWidgets.QFrame(self.frame_180)
        self.frame_181.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_181.setStyleSheet("border:0px;")
        self.frame_181.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_181.setObjectName("frame_181")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_181)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_50 = QtWidgets.QLabel(self.frame_181)
        self.label_50.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_3.addWidget(self.label_50, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_168.addWidget(self.frame_181, 0, QtCore.Qt.AlignHCenter)
        self.frame_182 = QtWidgets.QFrame(self.frame_180)
        self.frame_182.setMinimumSize(QtCore.QSize(141, 111))
        self.frame_182.setMaximumSize(QtCore.QSize(141, 111))
        self.frame_182.setStyleSheet("border:0px;\n"
"image: url(:/16x16/icons/24x24/user_logo.png);")
        self.frame_182.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_182.setObjectName("frame_182")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_182)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_182)
        self.label.setStyleSheet("image:url(:/newPrefix/7947586491595453760-512.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_168.addWidget(self.frame_182, 0, QtCore.Qt.AlignHCenter)
        self.frame_183 = QtWidgets.QFrame(self.frame_180)
        self.frame_183.setStyleSheet("border:0px;")
        self.frame_183.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_183.setObjectName("frame_183")
        self.verticalLayout_170 = QtWidgets.QVBoxLayout(self.frame_183)
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName("verticalLayout_170")
        self.frame_184 = QtWidgets.QFrame(self.frame_183)
        self.frame_184.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_184.setObjectName("frame_184")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_184)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_55 = QtWidgets.QLabel(self.frame_184)
        self.label_55.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color: rgb(21, 21, 21);")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_4.addWidget(self.label_55, 0, QtCore.Qt.AlignLeft)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame_184)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_29.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_29.setStyleSheet("border:1px solid rgb(108, 61, 183);\n"
"border-radius:6px;")
        self.lineEdit_29.setClearButtonEnabled(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.verticalLayout_4.addWidget(self.lineEdit_29, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_170.addWidget(self.frame_184)
        self.frame_185 = QtWidgets.QFrame(self.frame_183)
        self.frame_185.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_185.setObjectName("frame_185")
        self.verticalLayout_172 = QtWidgets.QVBoxLayout(self.frame_185)
        self.verticalLayout_172.setObjectName("verticalLayout_172")
        self.label_56 = QtWidgets.QLabel(self.frame_185)
        self.label_56.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_56.setFont(font)
        self.label_56.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_56.setStyleSheet("color: rgb(21, 21, 21);")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_172.addWidget(self.label_56, 0, QtCore.Qt.AlignLeft)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame_185)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_30.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_30.setStyleSheet("border:1px solid rgb(108, 61, 183);\n"
"border-radius:6px;")
        self.lineEdit_30.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_30.setPlaceholderText("")
        self.lineEdit_30.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_30.setClearButtonEnabled(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.verticalLayout_172.addWidget(self.lineEdit_30, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_170.addWidget(self.frame_185)
        self.verticalLayout_168.addWidget(self.frame_183)
        self.frame_186 = QtWidgets.QFrame(self.frame_180)
        self.frame_186.setStyleSheet("border:0px;")
        self.frame_186.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_186.setObjectName("frame_186")
        self.verticalLayout_173 = QtWidgets.QVBoxLayout(self.frame_186)
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName("verticalLayout_173")
        self.frame_187 = QtWidgets.QFrame(self.frame_186)
        self.frame_187.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_187.setObjectName("frame_187")
        self.verticalLayout_174 = QtWidgets.QVBoxLayout(self.frame_187)
        self.verticalLayout_174.setContentsMargins(150, 0, -1, 0)
        self.verticalLayout_174.setObjectName("verticalLayout_174")
        self.pushButton_63 = QtWidgets.QPushButton(self.frame_187)
        self.pushButton_63.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_63.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_63.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_63.setObjectName("pushButton_63")
        self.verticalLayout_174.addWidget(self.pushButton_63)
        self.verticalLayout_173.addWidget(self.frame_187)
        self.verticalLayout_168.addWidget(self.frame_186)
        self.verticalLayout_6.addWidget(self.frame_180, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_40.addWidget(self.frame_50)
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.page_13)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_51 = QtWidgets.QFrame(self.page_13)
        self.frame_51.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_57 = QtWidgets.QFrame(self.frame_51)
        self.frame_57.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_57.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_57.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_57)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_33 = QtWidgets.QFrame(self.frame_57)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_51 = QtWidgets.QLabel(self.frame_33)
        self.label_51.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_15.addWidget(self.label_51)
        self.label_2 = QtWidgets.QLabel(self.frame_33)
        self.label_2.setMinimumSize(QtCore.QSize(100, 70))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_15.addWidget(self.label_2)
        self.verticalLayout_7.addWidget(self.frame_33, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.frame_57)
        self.frame_4 = QtWidgets.QFrame(self.frame_51)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_21.setSpacing(20)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_5 = QtWidgets.QFrame(self.frame_11)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_57 = QtWidgets.QLabel(self.frame_5)
        self.label_57.setMinimumSize(QtCore.QSize(100, 0))
        self.label_57.setMaximumSize(QtCore.QSize(109, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_5.addWidget(self.label_57)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_31.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_31.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.horizontalLayout_5.addWidget(self.lineEdit_31)
        self.horizontalLayout_9.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_11)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_58 = QtWidgets.QLabel(self.frame_6)
        self.label_58.setMinimumSize(QtCore.QSize(100, 0))
        self.label_58.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_8.addWidget(self.label_58)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_32.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_32.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_32.setText("")
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.horizontalLayout_8.addWidget(self.lineEdit_32)
        self.horizontalLayout_9.addWidget(self.frame_6)
        self.verticalLayout_21.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_9 = QtWidgets.QFrame(self.frame_12)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_61 = QtWidgets.QLabel(self.frame_9)
        self.label_61.setMinimumSize(QtCore.QSize(80, 0))
        self.label_61.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_13.addWidget(self.label_61)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_35.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_35.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.horizontalLayout_13.addWidget(self.lineEdit_35)
        self.horizontalLayout_12.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_12)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_59 = QtWidgets.QLabel(self.frame_8)
        self.label_59.setMinimumSize(QtCore.QSize(80, 0))
        self.label_59.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_11.addWidget(self.label_59)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_33.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_33.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_33.setText("")
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.horizontalLayout_11.addWidget(self.lineEdit_33)
        self.horizontalLayout_12.addWidget(self.frame_8)
        self.verticalLayout_21.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_7 = QtWidgets.QFrame(self.frame_14)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_60 = QtWidgets.QLabel(self.frame_7)
        self.label_60.setMinimumSize(QtCore.QSize(90, 0))
        self.label_60.setMaximumSize(QtCore.QSize(89, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_10.addWidget(self.label_60)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_34.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_34.setMaximumSize(QtCore.QSize(1677218, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.horizontalLayout_10.addWidget(self.lineEdit_34)
        self.verticalLayout_10.addWidget(self.frame_7)
        self.verticalLayout_21.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_3.setContentsMargins(20, 15, 20, 15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_13)
        self.frame_10.setMinimumSize(QtCore.QSize(120, 40))
        self.frame_10.setMaximumSize(QtCore.QSize(120, 1621778))
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(87, 71, 127);")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_10, 0, 0, 1, 1)
        self.verticalLayout_21.addWidget(self.frame_13)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.frame_60 = QtWidgets.QFrame(self.frame_51)
        self.frame_60.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_60)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_60)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_14.addWidget(self.pushButton_4)
        self.verticalLayout_8.addWidget(self.frame_60, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_44.addWidget(self.frame_51)
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_14)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_56 = QtWidgets.QFrame(self.page_14)
        self.frame_56.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_56)
        self.verticalLayout_11.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_58 = QtWidgets.QFrame(self.frame_56)
        self.frame_58.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_58.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_34 = QtWidgets.QFrame(self.frame_58)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_52 = QtWidgets.QLabel(self.frame_34)
        self.label_52.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_16.addWidget(self.label_52)
        self.label_3 = QtWidgets.QLabel(self.frame_34)
        self.label_3.setMinimumSize(QtCore.QSize(100, 70))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_16.addWidget(self.label_3)
        self.verticalLayout_9.addWidget(self.frame_34, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_11.addWidget(self.frame_58)
        self.frame_15 = QtWidgets.QFrame(self.frame_56)
        self.frame_15.setStyleSheet("")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_62 = QtWidgets.QLabel(self.frame_17)
        self.label_62.setMinimumSize(QtCore.QSize(100, 0))
        self.label_62.setMaximumSize(QtCore.QSize(109, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_18.addWidget(self.label_62)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_36.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_36.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_36.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.horizontalLayout_18.addWidget(self.lineEdit_36)
        self.horizontalLayout_17.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_63 = QtWidgets.QLabel(self.frame_18)
        self.label_63.setMinimumSize(QtCore.QSize(100, 0))
        self.label_63.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_6.addWidget(self.label_63)
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame_18)
        self.lineEdit_42.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_42.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_42.setText("")
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.horizontalLayout_6.addWidget(self.lineEdit_42)
        self.horizontalLayout_17.addWidget(self.frame_18)
        self.verticalLayout_13.addWidget(self.frame_16)
        self.frame_19 = QtWidgets.QFrame(self.frame_15)
        self.frame_19.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_22.setSpacing(20)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_21 = QtWidgets.QFrame(self.frame_19)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_64 = QtWidgets.QLabel(self.frame_21)
        self.label_64.setMinimumSize(QtCore.QSize(100, 0))
        self.label_64.setMaximumSize(QtCore.QSize(109, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_24.addWidget(self.label_64)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_21)
        self.lineEdit_38.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_38.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.horizontalLayout_24.addWidget(self.lineEdit_38)
        self.horizontalLayout_22.addWidget(self.frame_21)
        self.frame_23 = QtWidgets.QFrame(self.frame_19)
        self.frame_23.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_65 = QtWidgets.QLabel(self.frame_23)
        self.label_65.setMinimumSize(QtCore.QSize(100, 0))
        self.label_65.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_25.addWidget(self.label_65)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_39.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_39.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_39.setText("")
        self.lineEdit_39.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.horizontalLayout_25.addWidget(self.lineEdit_39)
        self.horizontalLayout_22.addWidget(self.frame_23)
        self.verticalLayout_13.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_15)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_66 = QtWidgets.QLabel(self.frame_22)
        self.label_66.setMinimumSize(QtCore.QSize(100, 0))
        self.label_66.setMaximumSize(QtCore.QSize(109, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_26.addWidget(self.label_66)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame_22)
        self.lineEdit_40.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_40.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.horizontalLayout_26.addWidget(self.lineEdit_40)
        self.horizontalLayout_23.addWidget(self.frame_22)
        self.frame_24 = QtWidgets.QFrame(self.frame_20)
        self.frame_24.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_24.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_67 = QtWidgets.QLabel(self.frame_24)
        self.label_67.setMinimumSize(QtCore.QSize(100, 0))
        self.label_67.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_28.addWidget(self.label_67)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.frame_24)
        self.lineEdit_41.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_41.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_41.setText("")
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.horizontalLayout_28.addWidget(self.lineEdit_41)
        self.horizontalLayout_23.addWidget(self.frame_24)
        self.verticalLayout_13.addWidget(self.frame_20)
        self.verticalLayout_11.addWidget(self.frame_15)
        self.frame_69 = QtWidgets.QFrame(self.frame_56)
        self.frame_69.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_69)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_69)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_14.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_11.addWidget(self.frame_69)
        self.verticalLayout_15.addWidget(self.frame_56)
        self.stackedWidget.addWidget(self.page_14)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_70 = QtWidgets.QFrame(self.page)
        self.frame_70.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_70)
        self.verticalLayout_25.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_25.setSpacing(20)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_71 = QtWidgets.QFrame(self.frame_70)
        self.frame_71.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_71.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_71)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_35 = QtWidgets.QFrame(self.frame_71)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_68 = QtWidgets.QLabel(self.frame_35)
        self.label_68.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_68.setFont(font)
        self.label_68.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_37.addWidget(self.label_68)
        self.label_4 = QtWidgets.QLabel(self.frame_35)
        self.label_4.setMinimumSize(QtCore.QSize(100, 70))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_37.addWidget(self.label_4)
        self.verticalLayout_12.addWidget(self.frame_35, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_25.addWidget(self.frame_71)
        self.frame_37 = QtWidgets.QFrame(self.frame_70)
        self.frame_37.setStyleSheet("")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_38 = QtWidgets.QFrame(self.frame_37)
        self.frame_38.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_38.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_18.setContentsMargins(0, 20, 0, 20)
        self.verticalLayout_18.setSpacing(40)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_39 = QtWidgets.QFrame(self.frame_38)
        self.frame_39.setMaximumSize(QtCore.QSize(374, 79))
        self.frame_39.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_79 = QtWidgets.QLabel(self.frame_39)
        self.label_79.setMinimumSize(QtCore.QSize(100, 0))
        self.label_79.setMaximumSize(QtCore.QSize(109, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setObjectName("label_79")
        self.horizontalLayout_38.addWidget(self.label_79)
        self.lineEdit_52 = QtWidgets.QLineEdit(self.frame_39)
        self.lineEdit_52.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_52.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_52.setFont(font)
        self.lineEdit_52.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_52.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.horizontalLayout_38.addWidget(self.lineEdit_52)
        self.verticalLayout_18.addWidget(self.frame_39, 0, QtCore.Qt.AlignHCenter)
        self.frame_41 = QtWidgets.QFrame(self.frame_38)
        self.frame_41.setMaximumSize(QtCore.QSize(374, 79))
        self.frame_41.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_84 = QtWidgets.QLabel(self.frame_41)
        self.label_84.setMinimumSize(QtCore.QSize(100, 0))
        self.label_84.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_84.setAlignment(QtCore.Qt.AlignCenter)
        self.label_84.setObjectName("label_84")
        self.horizontalLayout_40.addWidget(self.label_84)
        self.lineEdit_57 = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit_57.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_57.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_57.setFont(font)
        self.lineEdit_57.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_57.setText("")
        self.lineEdit_57.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.horizontalLayout_40.addWidget(self.lineEdit_57)
        self.verticalLayout_18.addWidget(self.frame_41, 0, QtCore.Qt.AlignHCenter)
        self.frame_40 = QtWidgets.QFrame(self.frame_38)
        self.frame_40.setMaximumSize(QtCore.QSize(374, 79))
        self.frame_40.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_80 = QtWidgets.QLabel(self.frame_40)
        self.label_80.setMinimumSize(QtCore.QSize(100, 0))
        self.label_80.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("color: rgb(87, 71, 127);")
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.horizontalLayout_39.addWidget(self.label_80)
        self.lineEdit_53 = QtWidgets.QLineEdit(self.frame_40)
        self.lineEdit_53.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_53.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.lineEdit_53.setText("")
        self.lineEdit_53.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.horizontalLayout_39.addWidget(self.lineEdit_53)
        self.verticalLayout_18.addWidget(self.frame_40, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_27.addWidget(self.frame_38)
        self.verticalLayout_25.addWidget(self.frame_37)
        self.frame_78 = QtWidgets.QFrame(self.frame_70)
        self.frame_78.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_78.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_78)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_78)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_11.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_28.addWidget(self.pushButton_11, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_25.addWidget(self.frame_78)
        self.verticalLayout_30.addWidget(self.frame_70)
        self.stackedWidget.addWidget(self.page)


        self.schedule_page = QtWidgets.QWidget()
        self.schedule_page.setObjectName("schedule_page")
        self.schedule_verticalLayout_15 = QtWidgets.QVBoxLayout(self.schedule_page)
        self.schedule_verticalLayout_15.setObjectName("schedule_verticalLayout_15")
        self.schedule_frame_56 = QtWidgets.QFrame(self.schedule_page)
        self.schedule_frame_56.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.schedule_frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_56.setObjectName("schedule_frame_56")
        self.schedule_verticalLayout_2 = QtWidgets.QVBoxLayout(self.schedule_frame_56)
        self.schedule_verticalLayout_2.setObjectName("schedule_verticalLayout_2")
        self.schedule_frame_58 = QtWidgets.QFrame(self.schedule_frame_56)
        self.schedule_frame_58.setMaximumSize(QtCore.QSize(16777215, 100))
        self.schedule_frame_58.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.schedule_frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_58.setObjectName("schedule_frame_58")
        self.schedule_verticalLayout_9 = QtWidgets.QVBoxLayout(self.schedule_frame_58)
        self.schedule_verticalLayout_9.setObjectName("schedule_verticalLayout_9")
        self.schedule_frame_34 = QtWidgets.QFrame(self.schedule_frame_58)
        self.schedule_frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_34.setObjectName("schedule_frame_34")
        self.schedule_horizontalLayout_16 = QtWidgets.QHBoxLayout(self.schedule_frame_34)
        self.schedule_horizontalLayout_16.setObjectName("schedule_horizontalLayout_16")
        self.schedule_label_52 = QtWidgets.QLabel(self.schedule_frame_34)
        self.schedule_label_52.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.schedule_label_52.setFont(font)
        self.schedule_label_52.setStyleSheet("color: rgb(108, 61, 183);")
        self.schedule_label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_label_52.setObjectName("schedule_label_52")
        self.schedule_horizontalLayout_16.addWidget(self.schedule_label_52)
        self.schedule_label_3 = QtWidgets.QLabel(self.schedule_frame_34)
        self.schedule_label_3.setMinimumSize(QtCore.QSize(100, 70))
        self.schedule_label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.schedule_label_3.setText("")
        self.schedule_label_3.setObjectName("schedule_label_3")
        self.schedule_horizontalLayout_16.addWidget(self.schedule_label_3)
        self.schedule_verticalLayout_9.addWidget(self.schedule_frame_34, 0, QtCore.Qt.AlignHCenter)
        self.schedule_verticalLayout_2.addWidget(self.schedule_frame_58)
        self.schedule_horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.schedule_horizontalLayout_41.setObjectName("schedule_horizontalLayout_41")
        self.schedule_frame_15 = QtWidgets.QFrame(self.schedule_frame_56)
        self.schedule_frame_15.setStyleSheet("")
        self.schedule_frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_15.setMinimumWidth(450)
        self.schedule_frame_15.setMaximumWidth(550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_frame_15.sizePolicy().hasHeightForWidth())
        self.schedule_frame_15.setSizePolicy(sizePolicy)
        self.schedule_frame_15.setObjectName("schedule_frame_15")
        self.schedule_verticalLayout_13 = QtWidgets.QVBoxLayout(self.schedule_frame_15)
        self.schedule_verticalLayout_13.setObjectName("schedule_verticalLayout_13")
        self.schedule_frame_24 = QtWidgets.QFrame(self.schedule_frame_15)
        self.schedule_frame_24.setMinimumSize(QtCore.QSize(0, 250))
        self.schedule_frame_24.setMaximumSize(QtCore.QSize(16777215, 300))
        self.schedule_frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_24.setObjectName("schedule_frame_24")
        self.schedule_gridLayout_5 = QtWidgets.QGridLayout(self.schedule_frame_24)
        self.schedule_gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.schedule_gridLayout_5.setObjectName("schedule_gridLayout_5")
        self.schedule_calendarWidget_2 = QtWidgets.QCalendarWidget(self.schedule_frame_24)
        self.schedule_calendarWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.schedule_calendarWidget_2.setAutoFillBackground(True)
#         self.schedule_calendarWidget_2.setStyleSheet("background-color: rgb(196, 215, 238);\n"
# "alternate-background-color: rgb(24, 255, 58);\n"
# "font: 12pt \"MS Shell Dlg 2\";\n"
# "color: rgb(0, 0, 0);\n"
# "")
        self.schedule_calendarWidget_2.setGridVisible(True)
        self.schedule_calendarWidget_2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.schedule_calendarWidget_2.setNavigationBarVisible(True)
        self.schedule_calendarWidget_2.setDateEditEnabled(True)
        self.schedule_calendarWidget_2.setObjectName("schedule_calendarWidget_2")
        # self.schedule_calendarWidget_2.setStyleSheet(
        #     """
        #     background-color: rgb(196, 215, 238);
        #     selection-background-color: rgb(170, 85, 255);
        #     alternate-background-color: rgb(24, 255, 58);
        #     font: 12pt 'MS Shell Dlg 2';
        #     """
        # )
        # self.schedule_calendarWidget_2.setStyleSheet("background-color: lightgreen;")

        self.schedule_calendarWidget_2.setStyleSheet(
                "background-color: lightgreen;"
                "alternate-background-color:  rgb(24, 255, 58);"
                "selection-background-color: rgb(170, 85, 255);"
                "font: 12pt 'MS Shell Dlg 2';"
                # "QCalendarWidget"
                # "{"
                # "background-color: lightgreen;"
                # "selection-background-color: rgb(170, 85, 255);"
                # "font: 12pt 'MS Shell Dlg 2';"
                # "}"
                # "QCalendarWidget QToolButton"
                # "{"
                # "font: 12pt 'MS Shell Dlg 2'; background-color: lightgreen; color : black;"
                # "}"
                # "QCalendarWidget QToolButton::hover"
                # "{"
                # "background-color: cyan;"
                # "}"
                # "QCalendarWidget QToolButton::pressed"
                # "{"
                # "background-color: white;"
                # "}"
                # """
                # QCalendarWidget  QWidget{
                # alternate-background-color:  rgb(24, 255, 58);
                # }
                # QCalendarWidget QAbstractItemView:enabled {
                # font: 12pt 'MS Shell Dlg 2';
                # background-color: lightgreen;
                # selection-background-color: rgb(170, 85, 255);
                # }
                # """
        )

        
        self.date_painter = QTextCharFormat()
        self.date_painter.setFont(QFont("Times", 18, 200))
        # self.date_painter.setBackground(QBrush(QColor("red")))
        # self.date_brush = QBrush()
        # self.date_brush.setColor(Qt.blue)

        self.schedule_gridLayout_5.addWidget(self.schedule_calendarWidget_2, 0, 0, 1, 1)
        self.schedule_verticalLayout_13.addWidget(self.schedule_frame_24)
        self.schedule_frame_19 = QtWidgets.QFrame(self.schedule_frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_frame_19.sizePolicy().hasHeightForWidth())
        self.schedule_frame_19.setSizePolicy(sizePolicy)
        self.schedule_frame_19.setMaximumSize(QtCore.QSize(16777215, 90))
        self.schedule_frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_19.setObjectName("schedule_frame_19")
        self.schedule_horizontalLayout_22 = QtWidgets.QHBoxLayout(self.schedule_frame_19)
        self.schedule_horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_22.setSpacing(2)
        self.schedule_horizontalLayout_22.setObjectName("schedule_horizontalLayout_22")
        self.schedule_frame_21 = QtWidgets.QFrame(self.schedule_frame_19)
        self.schedule_frame_21.setMinimumSize(QtCore.QSize(0, 50))
        self.schedule_frame_21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.schedule_frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_21.setObjectName("schedule_frame_21")
        self.schedule_horizontalLayout_24 = QtWidgets.QHBoxLayout(self.schedule_frame_21)
        self.schedule_horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_24.setSpacing(0)
        self.schedule_horizontalLayout_24.setObjectName("schedule_horizontalLayout_24")
        self.schedule_label_64 = QtWidgets.QLabel(self.schedule_frame_21)
        self.schedule_label_64.setMinimumSize(QtCore.QSize(60, 0))
        self.schedule_label_64.setMaximumSize(QtCore.QSize(109, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label_64.setFont(font)
        self.schedule_label_64.setStyleSheet("color: rgb(87, 71, 127);")
        self.schedule_label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_label_64.setObjectName("schedule_label_64")
        self.schedule_horizontalLayout_24.addWidget(self.schedule_label_64)
        self.schedule_dateEdit = QtWidgets.QDateEdit(self.schedule_frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_dateEdit.sizePolicy().hasHeightForWidth())
        self.schedule_dateEdit.setSizePolicy(sizePolicy)
        self.schedule_dateEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.schedule_dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.schedule_dateEdit.setStyleSheet("color: rgb(87, 71, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"")
        self.schedule_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.schedule_dateEdit.setObjectName("schedule_dateEdit")
        self.schedule_horizontalLayout_24.addWidget(self.schedule_dateEdit)
        self.schedule_horizontalLayout_22.addWidget(self.schedule_frame_21)
        self.schedule_frame_23 = QtWidgets.QFrame(self.schedule_frame_19)
        self.schedule_frame_23.setMinimumSize(QtCore.QSize(0, 50))
        self.schedule_frame_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.schedule_frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_23.setObjectName("schedule_frame_23")
        self.schedule_horizontalLayout_25 = QtWidgets.QHBoxLayout(self.schedule_frame_23)
        self.schedule_horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_25.setSpacing(0)
        self.schedule_horizontalLayout_25.setObjectName("schedule_horizontalLayout_25")
        self.schedule_label_65 = QtWidgets.QLabel(self.schedule_frame_23)
        self.schedule_label_65.setMinimumSize(QtCore.QSize(60, 0))
        self.schedule_label_65.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label_65.setFont(font)
        self.schedule_label_65.setStyleSheet("color: rgb(87, 71, 127);")
        self.schedule_label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_label_65.setObjectName("schedule_label_65")
        self.schedule_horizontalLayout_25.addWidget(self.schedule_label_65)
        self.schedule_timeEdit = QtWidgets.QTimeEdit(self.schedule_frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_timeEdit.sizePolicy().hasHeightForWidth())
        self.schedule_timeEdit.setSizePolicy(sizePolicy)
        self.schedule_timeEdit.setMinimumSize(QtCore.QSize(100, 25))
        self.schedule_timeEdit.setStyleSheet("color: rgb(87, 71, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.schedule_timeEdit.setWrapping(False)
        self.schedule_timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_timeEdit.setDisplayFormat("hh:mm")
        self.schedule_timeEdit.setObjectName("schedule_timeEdit")
        self.schedule_horizontalLayout_25.addWidget(self.schedule_timeEdit)
        self.schedule_horizontalLayout_22.addWidget(self.schedule_frame_23)
        self.schedule_verticalLayout_13.addWidget(self.schedule_frame_19)
        self.schedule_frame_16 = QtWidgets.QFrame(self.schedule_frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_frame_16.sizePolicy().hasHeightForWidth())
        self.schedule_frame_16.setSizePolicy(sizePolicy)
        self.schedule_frame_16.setMaximumSize(QtCore.QSize(16777215, 90))
        self.schedule_frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_16.setObjectName("schedule_frame_16")
        self.schedule_horizontalLayout_17 = QtWidgets.QHBoxLayout(self.schedule_frame_16)
        self.schedule_horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_17.setSpacing(0)
        self.schedule_horizontalLayout_17.setObjectName("schedule_horizontalLayout_17")
        self.schedule_frame_17 = QtWidgets.QFrame(self.schedule_frame_16)
        self.schedule_frame_17.setMinimumSize(QtCore.QSize(0, 50))
        self.schedule_frame_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.schedule_frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_17.setObjectName("schedule_frame_17")
        self.schedule_horizontalLayout_18 = QtWidgets.QHBoxLayout(self.schedule_frame_17)
        self.schedule_horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_18.setSpacing(0)
        self.schedule_horizontalLayout_18.setObjectName("schedule_horizontalLayout_18")
        self.schedule_label_62 = QtWidgets.QLabel(self.schedule_frame_17)
        self.schedule_label_62.setMinimumSize(QtCore.QSize(120, 0))
        self.schedule_label_62.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label_62.setFont(font)
        self.schedule_label_62.setStyleSheet("color: rgb(87, 71, 127);")
        self.schedule_label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_label_62.setObjectName("schedule_label_62")
        self.schedule_horizontalLayout_18.addWidget(self.schedule_label_62)
        self.schedule_lineEdit_36 = QtWidgets.QLineEdit(self.schedule_frame_17)
        self.schedule_lineEdit_36.setMinimumSize(QtCore.QSize(120, 30))
        self.schedule_lineEdit_36.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.schedule_lineEdit_36.setFont(font)
        self.schedule_lineEdit_36.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.schedule_lineEdit_36.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.schedule_lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_lineEdit_36.setObjectName("schedule_lineEdit_36")
        self.schedule_horizontalLayout_18.addWidget(self.schedule_lineEdit_36)
        self.schedule_horizontalLayout_17.addWidget(self.schedule_frame_17)
        self.schedule_frame_18 = QtWidgets.QFrame(self.schedule_frame_16)
        self.schedule_frame_18.setMinimumSize(QtCore.QSize(0, 50))
        self.schedule_frame_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.schedule_frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_18.setObjectName("schedule_frame_18")
        self.schedule_horizontalLayout_6 = QtWidgets.QHBoxLayout(self.schedule_frame_18)
        self.schedule_horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_6.setSpacing(0)
        self.schedule_horizontalLayout_6.setObjectName("schedule_horizontalLayout_6")
        self.schedule_label_63 = QtWidgets.QLabel(self.schedule_frame_18)
        self.schedule_label_63.setMinimumSize(QtCore.QSize(60, 0))
        self.schedule_label_63.setMaximumSize(QtCore.QSize(108, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label_63.setFont(font)
        self.schedule_label_63.setStyleSheet("color: rgb(87, 71, 127);")
        self.schedule_label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_label_63.setObjectName("schedule_label_63")
        self.schedule_horizontalLayout_6.addWidget(self.schedule_label_63)
        self.schedule_lineEdit_42 = QtWidgets.QLineEdit(self.schedule_frame_18)
        self.schedule_lineEdit_42.setMinimumSize(QtCore.QSize(120, 30))
        self.schedule_lineEdit_42.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.schedule_lineEdit_42.setFont(font)
        self.schedule_lineEdit_42.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.schedule_lineEdit_42.setText("")
        self.schedule_lineEdit_42.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_lineEdit_42.setObjectName("schedule_lineEdit_42")
        self.schedule_horizontalLayout_6.addWidget(self.schedule_lineEdit_42)
        self.schedule_horizontalLayout_17.addWidget(self.schedule_frame_18)
        self.schedule_verticalLayout_13.addWidget(self.schedule_frame_16)
        self.schedule_frame_20 = QtWidgets.QFrame(self.schedule_frame_15)
        self.schedule_frame_20.setMaximumSize(QtCore.QSize(16777215, 90))
        self.schedule_frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_20.setObjectName("schedule_frame_20")
        self.schedule_horizontalLayout_23 = QtWidgets.QHBoxLayout(self.schedule_frame_20)
        self.schedule_horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_23.setSpacing(0)
        self.schedule_horizontalLayout_23.setObjectName("schedule_horizontalLayout_23")
        self.schedule_frame_22 = QtWidgets.QFrame(self.schedule_frame_20)
        self.schedule_frame_22.setMinimumSize(QtCore.QSize(0, 50))
        self.schedule_frame_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.schedule_frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_22.setObjectName("schedule_frame_22")
        self.schedule_horizontalLayout_26 = QtWidgets.QHBoxLayout(self.schedule_frame_22)
        self.schedule_horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.schedule_horizontalLayout_26.setSpacing(0)
        self.schedule_horizontalLayout_26.setObjectName("schedule_horizontalLayout_26")
        self.schedule_label_66 = QtWidgets.QLabel(self.schedule_frame_22)
        self.schedule_label_66.setMinimumSize(QtCore.QSize(150, 0))
        self.schedule_label_66.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_label_66.setFont(font)
        self.schedule_label_66.setStyleSheet("color: rgb(87, 71, 127);")
        self.schedule_label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_label_66.setObjectName("schedule_label_66")
        self.schedule_horizontalLayout_26.addWidget(self.schedule_label_66)
        self.schedule_lineEdit_40 = QtWidgets.QLineEdit(self.schedule_frame_22)
        self.schedule_lineEdit_40.setMinimumSize(QtCore.QSize(150, 30))
        self.schedule_lineEdit_40.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.schedule_lineEdit_40.setFont(font)
        self.schedule_lineEdit_40.setStyleSheet("border:1px solid rgb(86, 123, 142);")
        self.schedule_lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.schedule_lineEdit_40.setValidator(QIntValidator())
        self.schedule_lineEdit_40.setMaximumWidth(200)
        self.schedule_lineEdit_40.setObjectName("schedule_lineEdit_40")
        self.schedule_horizontalLayout_26.addWidget(self.schedule_lineEdit_40)
        self.schedule_horizontalLayout_23.addWidget(self.schedule_frame_22)
        self.schedule_verticalLayout_13.addWidget(self.schedule_frame_20)
        self.schedule_frame_69 = QtWidgets.QFrame(self.schedule_frame_15)
        self.schedule_frame_69.setMaximumSize(QtCore.QSize(16777215, 50))
        self.schedule_frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schedule_frame_69.setObjectName("schedule_frame_69")
        self.schedule_verticalLayout_14 = QtWidgets.QVBoxLayout(self.schedule_frame_69)
        self.schedule_verticalLayout_14.setObjectName("schedule_verticalLayout_14")
        self.schedule_pushButton_8 = QtWidgets.QPushButton(self.schedule_frame_69)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_pushButton_8.sizePolicy().hasHeightForWidth())
        self.schedule_pushButton_8.setSizePolicy(sizePolicy)
        self.schedule_pushButton_8.setMinimumSize(QtCore.QSize(150, 40))
        self.schedule_pushButton_8.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedule_pushButton_8.setFont(font)
        self.schedule_pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.schedule_pushButton_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;")
        self.schedule_pushButton_8.setAutoDefault(False)
        self.schedule_pushButton_8.setDefault(False)
        self.schedule_pushButton_8.setFlat(False)
        self.schedule_pushButton_8.setObjectName("schedule_pushButton_8")
        self.schedule_verticalLayout_14.addWidget(self.schedule_pushButton_8, 0, QtCore.Qt.AlignHCenter)
        self.schedule_verticalLayout_13.addWidget(self.schedule_frame_69)
        # self.schedule_verticalLayout_13.setStretch(0, 1)
        # self.schedule_verticalLayout_13.setStretch(1, 1)
        # self.schedule_verticalLayout_13.setStretch(2, 1)
        self.schedule_horizontalLayout_41.addWidget(self.schedule_frame_15)
        self.schedule_frame_36 = QtWidgets.QFrame(self.schedule_frame_56)
        self.schedule_frame_36.setMinimumSize(QtCore.QSize(600, 0))
        self.schedule_frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schedule_frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedule_frame_36.sizePolicy().hasHeightForWidth())

        self.schedule_frame_36.setSizePolicy(sizePolicy)
        self.schedule_frame_36.setObjectName("schedule_frame_36")
        self.schedule_gridLayout_4 = QtWidgets.QGridLayout(self.schedule_frame_36)
        self.schedule_gridLayout_4.setObjectName("schedule_gridLayout_4")

        self.schedule_tableWidget = QtWidgets.QTableWidget(self.schedule_frame_36)
        self.schedule_tableWidget.setObjectName("schedule_tableWidget")
        # self.schedule_tableWidget.setColumnCount(0)
        # self.schedule_tableWidget.setRowCount(0)
        self.schedule_tableWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(108, 61, 182);\n"
"    height:25px;\n"
"    color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;\n"
"padding: 4px;\n"
"    font-size: 12pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-right: 1px solid rgb(238, 235, 241);\n"
"}\n"
"QTableWidget::item {\n"
"border: 4px;\n"
"padding: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar\n"
"{\n"
"background :rgb(255, 255, 255);\n"
"width: 10px;\n"
"border:none;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : rgb(108, 61, 183);\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(100, 56, 170);\n"
"}")
        self.schedule_tableWidget.setColumnCount(8)
        self.schedule_tableWidget.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tableWidget.setItem(0, 4, item)
        self.schedule_tableWidget.resizeColumnsToContents()
        self.schedule_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.schedule_tableWidget.verticalHeader().setVisible(False)




        self.schedule_gridLayout_4.addWidget(self.schedule_tableWidget, 0, 0, 1, 1)
        self.schedule_horizontalLayout_41.addWidget(self.schedule_frame_36)
        self.schedule_verticalLayout_2.addLayout(self.schedule_horizontalLayout_41)
        self.schedule_verticalLayout_15.addWidget(self.schedule_frame_56)
        self.stackedWidget.addWidget(self.schedule_page)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.page_15)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.verticalLayout_83 = QtWidgets.QVBoxLayout(self.page_16)
        self.verticalLayout_83.setObjectName("verticalLayout_83")
        self.frame_53 = QtWidgets.QFrame(self.page_16)
        self.frame_53.setStyleSheet("")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_16.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_55 = QtWidgets.QFrame(self.frame_53)
        self.frame_55.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_55.setStyleSheet("background-color: rgb(238, 235, 241);\n"
"border-radius:10px;")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_19.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_19.setSpacing(30)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_72 = QtWidgets.QFrame(self.frame_55)
        self.frame_72.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_72.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_72)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_81 = QtWidgets.QLabel(self.frame_72)
        self.label_81.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_81.setFont(font)
        self.label_81.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.verticalLayout_31.addWidget(self.label_81)
        self.verticalLayout_19.addWidget(self.frame_72)
        self.frame_29 = QtWidgets.QFrame(self.frame_55)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_31.setSpacing(20)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.frame_30)
        self.lineEdit_55.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_55.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_55.setFont(font)
        self.lineEdit_55.setStyleSheet("border:1px solid rgb(86, 123, 142);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_55.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_55.setClearButtonEnabled(True)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.horizontalLayout_31.addWidget(self.lineEdit_55)
        self.frame_66 = QtWidgets.QFrame(self.frame_30)
        self.frame_66.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_66.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_66.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_66)
        self.horizontalLayout_32.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_66)
        self.pushButton_14.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_14.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"border-radius : 20; \n"
"background-repeat:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(252, 252, 252);\n"
"qproperty-icon:url(:/newPrefix/search.png);\n"
"qproperty-iconSize: 20px;\n"
"background-repeat:none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(234, 234, 234);\n"
"    \n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_32.addWidget(self.pushButton_14, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_31.addWidget(self.frame_66)
        self.horizontalLayout_30.addWidget(self.frame_30)
        self.frame_67 = QtWidgets.QFrame(self.frame_29)
        self.frame_67.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_67.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_67.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_67)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_67)
        self.pushButton_15.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_15.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"border-radius : 15; \n"
"\n"
"background-repeat:none;\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 194, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(59, 177, 0);\n"
"    \n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_33.addWidget(self.pushButton_15, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_30.addWidget(self.frame_67)
        self.verticalLayout_19.addWidget(self.frame_29)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.frame_55)
        self.tableWidget_5.setMaximumSize(QtCore.QSize(16277721, 16722271))
        self.tableWidget_5.setStyleSheet("#tableWidget_5{border-radius:6px;}\n"
"QHeaderView::section {\n"
"    background-color: rgb(108, 61, 182);\n"
"    height:25px;\n"
"    color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;\n"
"padding: 4px;\n"
"    font-size: 12pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-right: 1px solid rgb(238, 235, 241);\n"
"}\n"
"QTableWidget::item {\n"
"border: 4px;\n"
"padding: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar\n"
"{\n"
"background :rgb(255, 255, 255);\n"
"width: 10px;\n"
"border:none;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : rgb(108, 61, 183);\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(100, 56, 170);\n"
"}")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(10)
        self.tableWidget_5.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 7, item)
        self.verticalLayout_19.addWidget(self.tableWidget_5)
        self.verticalLayout_16.addWidget(self.frame_55)
        self.verticalLayout_83.addWidget(self.frame_53)
        self.stackedWidget.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.page_17)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_77 = QtWidgets.QFrame(self.page_17)
        self.frame_77.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_77.setStyleSheet("background-color: rgb(238, 235, 241);\n"
"border-radius:10px;")
        self.frame_77.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_77)
        self.verticalLayout_17.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_68 = QtWidgets.QFrame(self.frame_77)
        self.frame_68.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_68.setStyleSheet("background-color: rgb(238, 235, 241);\n"
"border-radius:10px;")
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_68)
        self.verticalLayout_24.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_24.setSpacing(30)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_74 = QtWidgets.QFrame(self.frame_68)
        self.frame_74.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_74.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_74)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_83 = QtWidgets.QLabel(self.frame_74)
        self.label_83.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_83.setFont(font)
        self.label_83.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setObjectName("label_83")
        self.verticalLayout_33.addWidget(self.label_83)
        self.verticalLayout_24.addWidget(self.frame_74)
        self.frame_31 = QtWidgets.QFrame(self.frame_68)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_35.setSpacing(20)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.frame_32)
        self.lineEdit_56.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_56.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_56.setFont(font)
        self.lineEdit_56.setStyleSheet("border:1px solid rgb(86, 123, 142);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_56.setClearButtonEnabled(True)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.horizontalLayout_35.addWidget(self.lineEdit_56)
        self.frame_75 = QtWidgets.QFrame(self.frame_32)
        self.frame_75.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_75.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_75.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_75)
        self.horizontalLayout_36.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_75)
        self.pushButton_16.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_16.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"border-radius : 20; \n"
"background-repeat:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(252, 252, 252);\n"
"qproperty-icon:url(:/newPrefix/search.png);\n"
"qproperty-iconSize: 20px;\n"
"background-repeat:none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(234, 234, 234);\n"
"    \n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_36.addWidget(self.pushButton_16, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_35.addWidget(self.frame_75)
        self.horizontalLayout_34.addWidget(self.frame_32)
        self.frame_76 = QtWidgets.QFrame(self.frame_31)
        self.frame_76.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_76.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_76.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_76.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_76)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_76)
        self.pushButton_17.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_17.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"border-radius : 15; \n"
"\n"
"background-repeat:none;\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 194, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(59, 177, 0);\n"
"    \n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_20.addWidget(self.pushButton_17, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_34.addWidget(self.frame_76)
        self.verticalLayout_24.addWidget(self.frame_31)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.frame_68)
        self.tableWidget_8.setMaximumSize(QtCore.QSize(16277721, 16722271))
        self.tableWidget_8.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(108, 61, 182);\n"
"    height:25px;\n"
"    color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;\n"
"padding: 4px;\n"
"    font-size: 12pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-right: 1px solid rgb(238, 235, 241);\n"
"}\n"
"QTableWidget::item {\n"
"border: 4px;\n"
"padding: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar\n"
"{\n"
"background :rgb(255, 255, 255);\n"
"width: 10px;\n"
"border:none;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : rgb(108, 61, 183);\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(100, 56, 170);\n"
"}")
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(6)
        self.tableWidget_8.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setItem(0, 4, item)
        self.verticalLayout_24.addWidget(self.tableWidget_8)
        self.verticalLayout_17.addWidget(self.frame_68)
        self.verticalLayout_34.addWidget(self.frame_77)
        self.stackedWidget.addWidget(self.page_17)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_22)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_62 = QtWidgets.QFrame(self.page_22)
        self.frame_62.setStyleSheet("")
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_62)
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_63 = QtWidgets.QFrame(self.frame_62)
        self.frame_63.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_63.setStyleSheet("background-color: rgb(238, 235, 241);\n"
"border-radius:10px;")
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_63)
        self.verticalLayout_22.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_22.setSpacing(30)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_73 = QtWidgets.QFrame(self.frame_63)
        self.frame_73.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_73.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:9px;")
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_73)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_82 = QtWidgets.QLabel(self.frame_73)
        self.label_82.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("color: rgb(108, 61, 183);")
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.verticalLayout_32.addWidget(self.label_82)
        self.verticalLayout_22.addWidget(self.frame_73)
        self.frame_27 = QtWidgets.QFrame(self.frame_63)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_29.setSpacing(20)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.frame_28)
        self.lineEdit_54.setMinimumSize(QtCore.QSize(250, 30))
        self.lineEdit_54.setMaximumSize(QtCore.QSize(376, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_54.setFont(font)
        self.lineEdit_54.setStyleSheet("border:1px solid rgb(86, 123, 142);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_54.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_54.setClearButtonEnabled(True)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.horizontalLayout_29.addWidget(self.lineEdit_54)
        self.frame_65 = QtWidgets.QFrame(self.frame_28)
        self.frame_65.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_65.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_65.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_65)
        self.horizontalLayout_21.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_65)
        self.pushButton_13.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_13.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"border-radius : 20; \n"
"background-repeat:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(252, 252, 252);\n"
"qproperty-icon:url(:/newPrefix/search.png);\n"
"qproperty-iconSize: 20px;\n"
"background-repeat:none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(234, 234, 234);\n"
"    \n"
"}")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_21.addWidget(self.pushButton_13, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_29.addWidget(self.frame_65, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_27.addWidget(self.frame_28)
        self.frame_64 = QtWidgets.QFrame(self.frame_27)
        self.frame_64.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_64.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_64.setStyleSheet("background-color: rgb(238, 235, 241);")
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_64)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_64)
        self.pushButton_10.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"border-radius : 15; \n"
"\n"
"background-repeat:none;\n"
"\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(64, 194, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(59, 177, 0);\n"
"    \n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_19.addWidget(self.pushButton_10, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_27.addWidget(self.frame_64)
        self.verticalLayout_22.addWidget(self.frame_27)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.frame_63)
        self.tableWidget_7.setMaximumSize(QtCore.QSize(16277721, 16722271))
        self.tableWidget_7.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(108, 61, 182);\n"
"    height:25px;\n"
"    color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:5px;\n"
"padding: 4px;\n"
"    font-size: 12pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-right: 1px solid rgb(238, 235, 241);\n"
"}\n"
"QTableWidget::item {\n"
"border: 4px;\n"
"padding: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar\n"
"{\n"
"background :rgb(255, 255, 255);\n"
"width: 10px;\n"
"border:none;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : rgb(108, 61, 183);\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(100, 56, 170);\n"
"}")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(10)
        self.tableWidget_7.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setItem(0, 7, item)
        self.verticalLayout_22.addWidget(self.tableWidget_7)
        self.verticalLayout_20.addWidget(self.frame_63)
        self.verticalLayout_23.addWidget(self.frame_62)
        self.stackedWidget.addWidget(self.page_22)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_53.setText(_translate("MainWindow", "  360-CRM "))
        self.label_54.setText(_translate("MainWindow", "Welcome Back"))
        self.pushButton_24.setText(_translate("MainWindow", "  Customer"))
        self.pushButton_25.setText(_translate("MainWindow", "  Inventory"))
        self.pushButton_26.setText(_translate("MainWindow", "  Orders"))
        self.pushButton_27.setText(_translate("MainWindow", "  Settings"))
        self.pushButton_schedule.setText(_translate("MainWindow", "  Schedule"))
        

        self.label_50.setText(_translate("MainWindow", "Login"))
        self.label_55.setText(_translate("MainWindow", "Username         "))
        self.label_56.setText(_translate("MainWindow", "Password        "))
        self.pushButton_63.setText(_translate("MainWindow", "Submit"))
        self.label_51.setText(_translate("MainWindow", "Add Customer"))
        self.label_57.setText(_translate("MainWindow", "First Name"))
        self.label_58.setText(_translate("MainWindow", "Last Name"))
        self.label_61.setText(_translate("MainWindow", "Email"))
        self.label_59.setText(_translate("MainWindow", "Phone"))
        self.label_60.setText(_translate("MainWindow", "Address"))
        self.checkBox.setText(_translate("MainWindow", "Employee"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.label_52.setText(_translate("MainWindow", "Add Order"))
        self.label_62.setText(_translate("MainWindow", "Customer"))
        self.label_63.setText(_translate("MainWindow", "Date"))
        self.label_64.setText(_translate("MainWindow", "Item/Service"))
        self.label_65.setText(_translate("MainWindow", "Quantity"))
        self.label_66.setText(_translate("MainWindow", "Price $"))
        self.label_67.setText(_translate("MainWindow", "Discount %"))
        self.pushButton_8.setText(_translate("MainWindow", "Add Order"))

        self.schedule_label_52.setText(_translate("MainWindow", "Meeting Schedule"))

        self.schedule_label_62.setText(_translate("MainWindow", "Customer"))
        self.schedule_label_63.setText(_translate("MainWindow", "Title"))
        self.schedule_label_64.setText(_translate("MainWindow", "Date"))
        self.schedule_label_65.setText(_translate("MainWindow", "Time"))
        self.schedule_label_66.setText(_translate("MainWindow", "Duration(min)"))
        # self.schedule_label_67.setText(_translate("MainWindow", "Discount %"))
        
        item = self.schedule_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.schedule_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No"))
        item = self.schedule_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer"))
        item = self.schedule_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.schedule_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.schedule_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        item = self.schedule_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.schedule_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.schedule_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cancel"))

        self.schedule_pushButton_8.setText(_translate("MainWindow", "New Schedule"))

        self.label_68.setText(_translate("MainWindow", "Add Inventory"))
        self.label_79.setText(_translate("MainWindow", "Name"))
        self.label_84.setText(_translate("MainWindow", "Quantity"))
        self.label_80.setText(_translate("MainWindow", "Price $"))
        self.pushButton_11.setText(_translate("MainWindow", "Add"))
        self.label_81.setText(_translate("MainWindow", "Customers"))
        self.pushButton_15.setText(_translate("MainWindow", "➕"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Employee"))
        item = self.tableWidget_5.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.tableWidget_5.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidget_5.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Generate Invoice"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.label_83.setText(_translate("MainWindow", "Inventory"))
        self.pushButton_17.setText(_translate("MainWindow", "➕"))
        item = self.tableWidget_8.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        __sortingEnabled = self.tableWidget_8.isSortingEnabled()
        self.tableWidget_8.setSortingEnabled(False)
        self.tableWidget_8.setSortingEnabled(__sortingEnabled)
        self.label_82.setText(_translate("MainWindow", "Orders"))
        self.pushButton_10.setText(_translate("MainWindow", "➕"))
        item = self.tableWidget_7.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.No"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Item/Service"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget_7.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Discount"))
        item = self.tableWidget_7.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.tableWidget_7.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Delete"))
        item = self.tableWidget_7.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Invoice"))
        __sortingEnabled = self.tableWidget_7.isSortingEnabled()
        self.tableWidget_7.setSortingEnabled(False)
        self.tableWidget_7.setSortingEnabled(__sortingEnabled)

class MainWindow(QMainWindow):
    add_customer_signal=pyqtSignal()
    add_order_signal=pyqtSignal()
    add_inventory_signal=pyqtSignal()

    send_invoice_signal = pyqtSignal(int)
    send_invoice_order_signal = pyqtSignal(int)
    send_schedule_signal = pyqtSignal(int, str)
    
    populate_customer_signal = pyqtSignal(bool)
    populate_order_signal = pyqtSignal(bool)
    populate_inventory_signal = pyqtSignal(bool)
    populate_schedule_signal = pyqtSignal(bool)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowTitle('')
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_12)
        self.ui.frame_2.hide()
        self.ui.pushButton_12.hide()
        self.add_drop_shadow()
        self.button_connection()
        self.initialize_data()
        self.movie = QtGui.QMovie("animation_200_lcuxl90f.gif")
        self.ui.label_2.setMovie(self.movie)
        self.ui.label_2.hide()

        self.movie2 = QtGui.QMovie("animation_200_lcuxl90f.gif")
        self.ui.label_3.setMovie(self.movie2)
        self.ui.label_3.hide()

        self.schedule_movie2 = QtGui.QMovie("animation_200_lcuxl90f.gif")
        self.ui.schedule_label_3.setMovie(self.schedule_movie2)
        self.ui.schedule_label_3.hide()

        self.movie3 = QtGui.QMovie("animation_200_lcuxl90f.gif")
        self.ui.label_4.setMovie(self.movie3)
        self.ui.label_4.hide()

        self.ui.lineEdit_42.setText(str(datetime.date.today()))
        self.ui.lineEdit_39.setText("1")

        today = QtCore.QDate.currentDate()
        self.ui.schedule_calendarWidget_2.setSelectedDate(today)
        self.ui.schedule_calendarWidget_2.showSelectedDate()

        # self.ui.schedule_calendarWidget_2.clearFocus()
        self.ui.schedule_calendarWidget_2.setDateTextFormat(today, self.ui.date_painter)
        self.ui.schedule_dateEdit.setDate(today)


    def button_connection(self):
        self.ui.pushButton_63.clicked.connect(self.login)
        self.ui.pushButton_15.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_13))
        self.ui.pushButton_24.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_16))
        self.ui.pushButton_25.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_17))
        self.ui.pushButton_26.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_22))
        self.ui.pushButton_schedule.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.schedule_page))
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.schedule_pushButton_8.clicked.connect(self.add_schedule)
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_14))
        self.ui.pushButton_12.clicked.connect(lambda: self.logout())
        self.ui.pushButton_4.clicked.connect(lambda:self.add_customer_signal.emit())
        self.add_customer_signal.connect(self.add_customer)
        self.ui.pushButton_8.clicked.connect(lambda: self.add_order_signal.emit())
        self.add_order_signal.connect(self.add_order)
        self.ui.pushButton_11.clicked.connect(lambda: self.add_inventory_signal.emit())
        self.add_inventory_signal.connect(self.add_inventory)

        self.ui.lineEdit_55.textChanged.connect(partial(self.search,"customer",self.ui.lineEdit_55,None))
        self.ui.pushButton_14.clicked.connect(lambda:self.search("customer",self.ui.lineEdit_55,True))

        self.ui.lineEdit_54.textChanged.connect(partial(self.search, "order", self.ui.lineEdit_54, None))
        self.ui.pushButton_13.clicked.connect(lambda: self.search("order", self.ui.lineEdit_54, True))
        self.ui.schedule_calendarWidget_2.clicked[QDate].connect(self.update_selected_date)

        self.populate_customer_signal.connect(self.add_data_to_customer)
        self.populate_order_signal.connect(self.add_data_to_order)
        self.populate_inventory_signal.connect(self.add_data_to_inventory)
        self.populate_schedule_signal.connect(self.add_data_to_schedule)

        self.send_invoice_signal.connect(self.send_invoice)
        self.send_invoice_order_signal.connect(self.send_invoice_order)
        self.send_schedule_signal.connect(self.send_meeting_schedule)


    def logout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_12)
        self.ui.frame_2.hide()
        self.ui.pushButton_12.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_12)

    def send_invoice(self,id):
        s=threading.Thread(target=invoice.generate,args=(id,))
        s.start()

    def send_invoice_order(self, id):
        s = threading.Thread(target=invoice.generate2, args=(id,))
        s.start()
        # s.join()

    def send_meeting_schedule(self,id, content="add"):
        s=threading.Thread(target=schedule.set_meeting, args=(id,content,))
        s.start()

    # def send_invoice_order(self, id):
    #     s = threading.Thread(target=invoice.generate2, args=(id,))
    #     s.start()

    def search(self,page,field,button=None):

        if field.text()=="":
            if page == "customer":
                self.populate_customer_signal.emit(False)
            if page == "order":
                self.populate_order_signal.emit(False)
        if button !=None:
            print("search exist...")
            if page == "customer":
                self.populate_customer_signal.emit(True)
            if page == "order":
                self.populate_order_signal.emit(True)

    def update_selected_date(self, clicked_date=None):
        # print("Selected Date: ", self.ui.schedule_calendarWidget_2.selectedDate())

        self.ui.schedule_calendarWidget_2.setDateTextFormat(QDate(), self.ui.date_painter)
        if clicked_date is not None:
            self.ui.schedule_calendarWidget_2.setDateTextFormat(clicked_date, self.ui.date_painter)
            # self.ui.schedule_calendarWidget_2.setba(clicked_date, self.ui.date_painter)
            # self.date_brush

            self.ui.schedule_dateEdit.setDate(self.ui.schedule_calendarWidget_2.selectedDate())

    def add_drop_shadow(self):
        frames=[self.ui.frame_180,self.ui.widget_15,self.ui.frame_72,self.ui.pushButton_12,
                self.ui.pushButton_16,self.ui.pushButton_17,self.ui.frame_74,self.ui.pushButton_14,
                self.ui.pushButton_15,self.ui.pushButton_12,self.ui.frame_73,self.ui.pushButton_13,
                self.ui.pushButton_12,self.ui.pushButton_10,self.ui.frame_57,self.ui.frame_58,self.ui.frame_71]
        pushbuttons = [x for x in frames if isinstance(x, QtWidgets.QPushButton)]
        frames = [x for x in frames if isinstance(x, QtWidgets.QFrame)]
        frames2=[self.ui.frame_5,self.ui.frame_6,
                self.ui.frame_5,self.ui.frame_9,self.ui.frame_8,self.ui.frame_7,self.ui.frame_10,
                self.ui.frame_17,self.ui.frame_18,self.ui.frame_21,self.ui.frame_23,self.ui.frame_22,self.ui.frame_24,
                self.ui.frame_39,self.ui.frame_40,self.ui.frame_41,self.ui.tableWidget_8, self.ui.tableWidget_7,self.ui.tableWidget_5, self.ui.schedule_tableWidget]  # self.ui.schedule_tableWidget
        for frame in frames:
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(50)
                shadow.setOffset(1, 1)
                shadow.setColor(QColor(210, 210, 210))
                frame.setGraphicsEffect(shadow)
        for frame in frames2:
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(25)
                shadow.setOffset(1, 1)
                shadow.setColor(QColor(210, 210, 210))
                frame.setGraphicsEffect(shadow)
        for button in pushbuttons:
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(20)
                shadow.setOffset(1, 1)
                shadow.setColor(QColor(200, 200, 200))
                button.setGraphicsEffect(shadow)


    def login(self):
        email = self.ui.lineEdit_29.text().casefold()
        password = self.ui.lineEdit_30.text()
        a = db.log_in(email)
        print(a)
        if len(a)>0:
                db_email = a[0][1]
                db_password = a[0][2]
                name= a[0][3].capitalize()

                if email == db_email and password == db_password:
                        print("Login successfully.")
                        self.ui.frame_2.show()
                        self.ui.label_54.setText("   Welcome Back "+str(name))
                        self.ui.stackedWidget.setCurrentWidget(self.ui.page_16)
                        self.ui.pushButton_12.show()
                else:
                        print("Login Fail.")

    def resizeEvent(self, event):
        # self.ui.tableWidget_5.setGeometry(self.ui.frame_55.geometry())
        self.ui.tableWidget_5.resize(self.ui.frame_55.size().width()-80,self.ui.frame_55.size().height()-300)
        self.ui.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableWidget_7.resize(self.ui.frame_63.size().width() - 80, self.ui.frame_63.size().height() - 300)
        self.ui.tableWidget_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableWidget_8.resize(self.ui.frame_68.size().width() - 80, self.ui.frame_68.size().height() - 300)
        self.ui.tableWidget_8.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # print(self.ui.schedule_tableWidget.size())
        # self.ui.schedule_tableWidget.resize(int(self.ui.schedule_frame_56.size().width()/2) - 10, self.ui.schedule_frame_56.size().height() - 30)
        self.ui.schedule_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # self.ui.schedule_tableWidget.resize(500, 400)
        # print(self.ui.schedule_tableWidget.size())
        # # print((int(self.ui.meeting_frame.size().width() / 2), self.ui.meeting_frame.size().height() - 300))
        # self.ui.schedule_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def initialize_data(self):

        self.add_data_to_customer()
        self.add_data_to_order()
        self.add_data_to_inventory()
        self.add_data_to_schedule()

    def stop_noti(self,label,movie):
        label.hide()
        movie.stop()
        try:
            if self.ui.lineEdit_55.text() == "":
                self.populate_customer_signal.emit(False)
            else:
                self.populate_customer_signal.emit(True)

            if self.ui.lineEdit_54.text() == "":
                self.populate_order_signal.emit(False)
            else:
                self.populate_order_signal.emit(True)


            if self.ui.lineEdit_56.text() == "":
                self.populate_inventory_signal.emit(False)
            else:
                self.populate_inventory_signal.emit(True)
            # s = threading.Thread(target=self.add_data_to_customer)
            # s.start()
        #     if self.ui.lineEdit_56.text() == "":
        #         self.populate_schedule_signal.emit(False)
        #     else:

            self.populate_schedule_signal.emit(True)

        except:
            pass
        pass

    def crud(self,table_name,id,row,operation):
        print(table_name)
        print(id)
        if table_name == "inventory":
            if operation == "update":
                name = self.ui.tableWidget_8.item(row, 1).text()
                price = self.ui.tableWidget_8.item(row, 2).text()
                quantity = self.ui.tableWidget_8.item(row, 3).text()

                data = [name,price,quantity]
                print(data)
                db.update_inventory(id,data)
                if self.ui.lineEdit_56.text()=="":
                    self.populate_inventory_signal.emit(False)
                else:
                    self.populate_inventory_signal.emit(True)
            if operation == "delete":
                db.delete_inventory(id)
                if self.ui.lineEdit_56.text() == "":
                    self.populate_inventory_signal.emit(False)
                else:
                    self.populate_inventory_signal.emit(True)
        if table_name == "customer":
            if operation == "update":
                first_name = self.ui.tableWidget_5.item(row, 1).text()
                last_name = self.ui.tableWidget_5.item(row, 2).text()
                address = self.ui.tableWidget_5.item(row, 3).text()
                phone = self.ui.tableWidget_5.item(row, 4).text()
                email = self.ui.tableWidget_5.item(row, 5).text()
                employee = self.ui.tableWidget_5.item(row, 6).text()
                data = [first_name,last_name,address,phone,email,employee]
                print(data)
                db.update_customer(id,data)
                if self.ui.lineEdit_55.text()=="":
                    self.populate_customer_signal.emit(False)
                else:
                    self.populate_customer_signal.emit(True)
            if operation == "delete":
                db.delete_customer(id)
                if self.ui.lineEdit_55.text() == "":
                    self.populate_customer_signal.emit(False)
                else:
                    self.populate_customer_signal.emit(True)
            if operation == "invoice":
                self.send_invoice_signal.emit(id)

        if table_name == "order":
            if operation == "update":
                date = self.ui.tableWidget_7.item(row, 2).text()
                item = self.ui.tableWidget_7.item(row, 3).text()
                quantity = self.ui.tableWidget_7.item(row, 4).text()
                price = self.ui.tableWidget_7.item(row, 5).text()
                discount = self.ui.tableWidget_7.item(row, 6).text()

                data = [date,item,quantity,price,discount]
                print(data)
                db.update_order(id,data)
                if self.ui.lineEdit_54.text()=="":
                    self.populate_order_signal.emit(False)
                else:
                    self.populate_order_signal.emit(True)
            if operation == "delete":
                db.delete_order(id)
                if self.ui.lineEdit_54.text() == "":
                    self.populate_order_signal.emit(False)
                else:
                    self.populate_order_signal.emit(True)
            if operation == "invoice":
                self.send_invoice_order_signal.emit(id)

        if table_name == "schedule":
            if operation == "update":
                # date = self.ui.tableWidget_7.item(row, 2).text()
                # item = self.ui.tableWidget_7.item(row, 3).text()
                # quantity = self.ui.tableWidget_7.item(row, 4).text()
                # price = self.ui.tableWidget_7.item(row, 5).text()
                # discount = self.ui.tableWidget_7.item(row, 6).text()
                print(row)

                customer_name = self.ui.schedule_tableWidget.item(row, 1).text()
                print(customer_name)
                date = self.ui.schedule_tableWidget.cellWidget(row, 3).date().toString("yyyy-MM-dd")
                print(date)
                time = self.ui.schedule_tableWidget.cellWidget(row, 4).time().toString("hh:mm")
                title = self.ui.schedule_tableWidget.item(row, 2).text()

                duration = self.ui.schedule_tableWidget.item(row, 5).text()

                data = [title, date, time, duration]

                print(data)
                db.update_schedule(id,data)
                # if self.ui.lineEdit_54.text()=="":
                #     self.populate_order_signal.emit(False)
                # else:
                self.send_schedule_signal.emit(id, "update")
                
                self.populate_schedule_signal.emit(True)
            if operation == "cancel":
                s=threading.Thread(target=schedule.set_meeting, args=(id,"cancel",))
                s.start()
                s.join()

                while True:
                    if s.is_alive():
                        time.sleep(1)
                        continue
                    break

                db.delete_schedule(id)
                self.populate_schedule_signal.emit(True)


    def add_data_to_customer(self,status=False):
        print(status)
        if status:
            customer_name = self.ui.lineEdit_55.text()
        else:
            customer_name = None
        all_data = db.get_customer_data(customer_name)
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_5.verticalHeader().setVisible(False)
        # Get the current number of rows in the table
        customers = []
        customer_search = []
        for data in all_data:
            row = self.ui.tableWidget_5.rowCount()

             # Add a new row to the table
            self.ui.tableWidget_5.insertRow(row)

            # Add the data to the new row
            for i, item in enumerate(data):
                try:
                    item=item.capitalize()
                except:
                    pass
                self.ui.tableWidget_5.setItem(row, i, QtWidgets.QTableWidgetItem(str(item)))
            customer_name = str(data[1]) + " " + str(data[2]) + " (" + str(data[0]) + ")"
            customers.append(customer_name)
            customer_search.append(str(data[1]))
            btn = QPushButton(self.ui.tableWidget_5)
            btn.setText('Update')
            # btn.setStyleSheet("background-color: rgb(238, 163, 11); color:white;")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(partial(self.crud,"customer",data[0],row,"update"))
            self.ui.tableWidget_5.setCellWidget(row, 7, btn)

            btn2 = QPushButton(self.ui.tableWidget_5)
            btn2.setText('Delete')
            btn2.setStyleSheet("color:red;")
            btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn2.clicked.connect(partial(self.crud, "customer", data[0], row,"delete"))
            self.ui.tableWidget_5.setCellWidget(row, 8, btn2)

            btn3 = QPushButton(self.ui.tableWidget_5)
            btn3.setText('Generate Invoice')
            btn3.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:1px;")
            btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn3.clicked.connect(partial(self.crud, "customer", data[0], row,"invoice"))
            self.ui.tableWidget_5.setCellWidget(row, 9, btn3)
        completer = QCompleter(customers)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit_36.setCompleter(completer)

        completer = QCompleter(customers)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.schedule_lineEdit_36.setCompleter(completer)

        completer2 = QCompleter(customer_search)
        completer2.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit_55.setCompleter(completer2)
        # self.ui.tableWidget_5.setGeometry(self.ui.frame_55.geometry())

    def add_customer(self):
        first_name = self.ui.lineEdit_31.text()
        last_name = self.ui.lineEdit_32.text()
        address = self.ui.lineEdit_34.text()
        phone = self.ui.lineEdit_33.text()
        email = self.ui.lineEdit_35.text()
        employee = self.ui.checkBox.isChecked()
        s=threading.Thread(target=db.insert_customer,args=(first_name, last_name, address, phone, email, employee,))
        s.start()
        s.join()

        # Show message box with "Success" message
        self.ui.label_2.show()
        self.movie.start()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(2200)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda:self.stop_noti(self.ui.label_2,self.movie))
        self.timer.start()


    def add_data_to_order(self,status=False):
        print(status)
        if status:
            customer_name = self.ui.lineEdit_54.text()
        else:
            customer_name = None
        all_data = db.get_order_data(customer_name)
        self.ui.tableWidget_7.setRowCount(0)
        self.ui.tableWidget_7.verticalHeader().setVisible(False)
        # Get the current number of rows in the table
        orders = []
        order_search = []
        for data in all_data:
            row = self.ui.tableWidget_7.rowCount()

             # Add a new row to the table
            self.ui.tableWidget_7.insertRow(row)

            # Add the data to the new row

            for i, item in enumerate(data):
                try:
                    item=item.capitalize()
                except:
                    pass
                self.ui.tableWidget_7.setItem(row, i, QtWidgets.QTableWidgetItem(str(item)))

            customer_name = str(data[1])
            orders.append(customer_name)
            order_search.append(str(data[1]))

            btn = QPushButton(self.ui.tableWidget_7)
            btn.setText('Update')
            # btn.setStyleSheet("background-color: rgb(238, 163, 11); color:white;")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(partial(self.crud, "order", data[0], row,"update"))
            self.ui.tableWidget_7.setCellWidget(row, 7, btn)

            btn2 = QPushButton(self.ui.tableWidget_7)
            btn2.setText('Delete')
            btn2.setStyleSheet("color:red;")
            btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn2.clicked.connect(partial(self.crud, "order", data[0], row,"delete"))
            self.ui.tableWidget_7.setCellWidget(row, 8, btn2)

            btn3 = QPushButton(self.ui.tableWidget_7)
            btn3.setText('Generate Invoice')
            btn3.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.5, y2:1, stop:0 rgba(101, 172, 236, 255), stop:1 rgba(109, 55, 196, 255));\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius:1px;")
            btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn3.clicked.connect(partial(self.crud, "order", data[0], row,"invoice"))
            self.ui.tableWidget_7.setCellWidget(row, 9, btn3)

        completer = QCompleter(orders)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit_54.setCompleter(completer)
        # self.ui.tableWidget_5.setGeometry(self.ui.frame_55.geometry())

    def add_order(self):
        customer_name = int(self.ui.lineEdit_36.text().split("(")[1].replace(")",""))
        date = self.ui.lineEdit_42.text()
        order_item = self.ui.lineEdit_38.text()
        quantity = self.ui.lineEdit_39.text()
        price = self.ui.lineEdit_40.text()
        discount = self.ui.lineEdit_41.text()
        # x = db.insert_order(customer_name, date, order_item, quantity, price)
        s=threading.Thread(target=db.insert_order,args=(customer_name, date, order_item, quantity, price,discount,))
        s.start()
        s.join()
        # threading.Thread(target=self.add_data_to_order).start()
        # Show message box with "Success" message
        self.ui.label_3.show()
        self.movie2.start()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(2200)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda:self.stop_noti(self.ui.label_3,self.movie2))
        self.timer.start()

    def add_data_to_inventory(self,status=False):
        all_data = db.get_inventory_data()
        self.ui.tableWidget_8.setRowCount(0)
        self.ui.tableWidget_8.verticalHeader().setVisible(False)
        # Get the current number of rows in the table
        for data in all_data:
            row = self.ui.tableWidget_8.rowCount()

             # Add a new row to the table
            self.ui.tableWidget_8.insertRow(row)

            # Add the data to the new row
            for i, item in enumerate(data):
                try:
                    item=item.capitalize()
                except:
                    pass
                self.ui.tableWidget_8.setItem(row, i, QtWidgets.QTableWidgetItem(str(item)))

            # self.ui.tableWidget_5.setGeometry(self.ui.frame_55.geometry())
            btn = QPushButton(self.ui.tableWidget_8)
            btn.setText('Update')
            # btn.setStyleSheet("background-color: rgb(238, 163, 11); color:white;")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(partial(self.crud, "inventory", data[0], row, "update"))
            self.ui.tableWidget_8.setCellWidget(row, 4, btn)

            btn2 = QPushButton(self.ui.tableWidget_8)
            btn2.setText('Delete')
            btn2.setStyleSheet("color:red;")
            btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn2.clicked.connect(partial(self.crud, "inventory", data[0], row, "delete"))
            self.ui.tableWidget_8.setCellWidget(row, 5, btn2)

    def add_inventory(self):

        product_name = self.ui.lineEdit_52.text()
        price = self.ui.lineEdit_53.text()
        quantity = self.ui.lineEdit_57.text()
        # x = db.insert_inventory(product_name, category, quantity)
        s=threading.Thread(target=db.insert_inventory,args=(product_name, price, quantity,))
        s.start()
        s.join()
        # threading.Thread(target=self.add_data_to_inventory).start()
        # Show message box with "Success" message
        self.ui.label_4.show()
        self.movie3.start()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(2200)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda:self.stop_noti(self.ui.label_4,self.movie3))
        self.timer.start()


    def add_data_to_schedule(self,status=False):
        all_data = db.get_schedule_data()
        print(f"{all_data=}")
        self.ui.schedule_tableWidget.setRowCount(0)
        self.ui.schedule_tableWidget.verticalHeader().setVisible(False)
        # Get the current number of rows in the table
        for data in all_data:
            row = self.ui.schedule_tableWidget.rowCount()

             # Add a new row to the table
            self.ui.schedule_tableWidget.insertRow(row)

            # Add the data to the new row
            for i, item in enumerate(data):
                if i == 3:
                    # item = [int(d) for d in item.split("-")]
                    date_ = QDate.fromString(item, "yyyy-MM-dd")
                    item = QtWidgets.QDateEdit()
                    item.setDate(date_)
                    item.setDisplayFormat("yy-MM-dd")
                    # item.setMinimumSize(QtCore.QSize(100, 20))
                    item.setFrame(False)
                    # self.schedule_dateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
                    # self.schedule_dateEdit.setStyleSheet("color: rgb(87, 71, 127);\n"
                    # "font: 75 12pt \"MS Shell Dlg 2\";\n"
                    # "")
                    self.ui.schedule_tableWidget.setCellWidget(row, i, item)
                elif i == 4:
                    # item = [int(d) for d in item.split(":")]
                    time_ = QTime.fromString(item, "hh:mm")
                    item = QtWidgets.QTimeEdit()
                    item.setTime(time_)
                    item.setFrame(False)
                    item.setDisplayFormat("hh:mm")
                    self.ui.schedule_tableWidget.setCellWidget(row, i, item)
                else:
                    try:
                        item=item.capitalize()
                    except:
                        pass

                    item = QtWidgets.QTableWidgetItem(str(item))
                    if i == 1:
                        item.setFlags(item.flags()  ^ QtCore.Qt.ItemIsEditable)                                                    
                    self.ui.schedule_tableWidget.setItem(row, i, item)

            # self.ui.tableWidget_5.setGeometry(self.ui.frame_55.geometry())
            btn = QPushButton(self.ui.schedule_tableWidget)
            btn.setText('Update')
            btn.setFlat(True)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(partial(self.crud, "schedule", data[0], row, "update"))
            self.ui.schedule_tableWidget.setCellWidget(row, 6, btn)

            btn2 = QPushButton(self.ui.schedule_tableWidget)
            btn2.setText('Cancel')
            btn2.setFlat(True)

            btn2.setStyleSheet("color:red;")
            btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn2.clicked.connect(partial(self.crud, "schedule", data[0], row, "cancel"))
            self.ui.schedule_tableWidget.setCellWidget(row, 7, btn2)


    def add_schedule(self):
        try:
            customer_name = int(self.ui.schedule_lineEdit_36.text().split("(")[1].replace(")","")) #   int(self.ui.schedule_lineEdit_36.text().split("(")[1].replace(")",""))
        except Exception as e:
            error_retval = QMessageBox.warning(
                None,
                "Warning",
                "Invalid Customer Name...",
                QMessageBox.Ok
            )
            return
        date = self.ui.schedule_dateEdit.date().toString("yyyy-MM-dd")
        title = self.ui.schedule_lineEdit_42.text()
        if title.strip() == "":
            error_retval = QMessageBox.warning(
                None,
                "Warning",
                "Title is empty. Please input the title.",
                QMessageBox.Ok
            )
            return
        time = self.ui.schedule_timeEdit.time().toString("hh:mm")
        duration = self.ui.schedule_lineEdit_40.text()
        if duration.strip() == "":
            error_retval = QMessageBox.warning(
                None,
                "Warning",
                "Meeting Period is not set. Please input the duration.",
                QMessageBox.Ok
            )
            return


        # x = db.insert_schedule(customer_name, title, date, time, duration)
        s=threading.Thread(target=db.insert_schedule,args=(customer_name, title, date, time, duration,))
        s.start()
        s.join()
        # Show message box with "Success" message
        self.ui.schedule_label_3.show()
        self.schedule_movie2.start()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(2200)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda:self.stop_noti(self.ui.schedule_label_3,self.schedule_movie2))
        self.timer.start()

        while True:
            if s.is_alive():
                time.sleep(1)
                continue
            self.send_schedule_signal.emit(-1, "add")
            break


        # if label.objectName() == "schedule_label_3":


from sys import exit as sysExit

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # app.exec_()
    sys.exit(app.exec_())
