# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zx.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.send_Button = QtWidgets.QPushButton(self.centralwidget)
        self.send_Button.setGeometry(QtCore.QRect(200, 210, 75, 21))
        self.send_Button.setObjectName("send_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 170, 47, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 170, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 100, 158, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(370, 30, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.message_list = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.message_list.setContentsMargins(0, 0, 0, 0)
        self.message_list.setObjectName("message_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_Button.setText(_translate("MainWindow", "send_Button"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", " enter name"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", " enter date"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "enter message"))
