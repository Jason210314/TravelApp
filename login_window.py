# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login_Window(object):
    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(300, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login_Window.sizePolicy().hasHeightForWidth())
        Login_Window.setSizePolicy(sizePolicy)
        Login_Window.setMinimumSize(QtCore.QSize(300, 350))
        Login_Window.setMaximumSize(QtCore.QSize(300, 350))
        self.gridLayout = QtWidgets.QGridLayout(Login_Window)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Login_Window)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.name_la = QtWidgets.QLabel(self.page)
        self.name_la.setGeometry(QtCore.QRect(30, 95, 70, 22))
        self.name_la.setMinimumSize(QtCore.QSize(70, 0))
        self.name_la.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_la.setFont(font)
        self.name_la.setObjectName("name_la")
        self.pw_la = QtWidgets.QLabel(self.page)
        self.pw_la.setGeometry(QtCore.QRect(30, 150, 70, 22))
        self.pw_la.setMinimumSize(QtCore.QSize(70, 0))
        self.pw_la.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pw_la.setFont(font)
        self.pw_la.setObjectName("pw_la")
        self.name_log = QtWidgets.QLineEdit(self.page)
        self.name_log.setGeometry(QtCore.QRect(109, 95, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setItalic(False)
        self.name_log.setFont(font)
        self.name_log.setText("")
        self.name_log.setMaxLength(16)
        self.name_log.setObjectName("name_log")
        self.pw_log = QtWidgets.QLineEdit(self.page)
        self.pw_log.setGeometry(QtCore.QRect(109, 150, 161, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.pw_log.setFont(font)
        self.pw_log.setMaxLength(16)
        self.pw_log.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_log.setObjectName("pw_log")
        self.login_btn = QtWidgets.QPushButton(self.page)
        self.login_btn.setGeometry(QtCore.QRect(100, 210, 100, 30))
        self.login_btn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setAutoDefault(True)
        self.login_btn.setDefault(True)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.title1 = QtWidgets.QLabel(self.page)
        self.title1.setGeometry(QtCore.QRect(100, 40, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.title1.setFont(font)
        self.title1.setObjectName("title1")
        self.signin_btn = QtWidgets.QPushButton(self.page)
        self.signin_btn.setGeometry(QtCore.QRect(100, 255, 100, 30))
        self.signin_btn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.signin_btn.setFont(font)
        self.signin_btn.setAutoDefault(False)
        self.signin_btn.setDefault(False)
        self.signin_btn.setFlat(False)
        self.signin_btn.setObjectName("signin_btn")
        self.close_btn = QtWidgets.QPushButton(self.page)
        self.close_btn.setGeometry(QtCore.QRect(100, 300, 100, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.close_btn.setFont(font)
        self.close_btn.setAutoDefault(False)
        self.close_btn.setDefault(False)
        self.close_btn.setFlat(False)
        self.close_btn.setObjectName("close_btn")
        self.failed = QtWidgets.QLabel(self.page)
        self.failed.setGeometry(QtCore.QRect(110, 120, 161, 16))
        self.failed.setObjectName("failed")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.title2 = QtWidgets.QLabel(self.page_2)
        self.title2.setGeometry(QtCore.QRect(70, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.title2.setFont(font)
        self.title2.setObjectName("title2")
        self.name_la2 = QtWidgets.QLabel(self.page_2)
        self.name_la2.setGeometry(QtCore.QRect(30, 85, 70, 30))
        self.name_la2.setMinimumSize(QtCore.QSize(70, 25))
        self.name_la2.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_la2.setFont(font)
        self.name_la2.setObjectName("name_la2")
        self.pw_la2 = QtWidgets.QLabel(self.page_2)
        self.pw_la2.setGeometry(QtCore.QRect(30, 185, 70, 25))
        self.pw_la2.setMinimumSize(QtCore.QSize(70, 25))
        self.pw_la2.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pw_la2.setFont(font)
        self.pw_la2.setObjectName("pw_la2")
        self.name_sign = QtWidgets.QLineEdit(self.page_2)
        self.name_sign.setGeometry(QtCore.QRect(110, 90, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name_sign.setFont(font)
        self.name_sign.setMaxLength(16)
        self.name_sign.setObjectName("name_sign")
        self.pw_sign = QtWidgets.QLineEdit(self.page_2)
        self.pw_sign.setGeometry(QtCore.QRect(110, 190, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pw_sign.setFont(font)
        self.pw_sign.setMaxLength(16)
        self.pw_sign.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_sign.setObjectName("pw_sign")
        self.signin_btn2 = QtWidgets.QPushButton(self.page_2)
        self.signin_btn2.setGeometry(QtCore.QRect(40, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signin_btn2.setFont(font)
        self.signin_btn2.setAutoDefault(True)
        self.signin_btn2.setDefault(True)
        self.signin_btn2.setObjectName("signin_btn2")
        self.back_btn = QtWidgets.QPushButton(self.page_2)
        self.back_btn.setGeometry(QtCore.QRect(160, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.show_btn = QtWidgets.QPushButton(self.page_2)
        self.show_btn.setGeometry(QtCore.QRect(250, 190, 20, 20))
        self.show_btn.setText("")
        self.show_btn.setObjectName("show_btn")
        self.invalid_name = QtWidgets.QLabel(self.page_2)
        self.invalid_name.setGeometry(QtCore.QRect(110, 110, 161, 16))
        self.invalid_name.setObjectName("invalid_name")
        self.name_la2_2 = QtWidgets.QLabel(self.page_2)
        self.name_la2_2.setGeometry(QtCore.QRect(30, 135, 70, 25))
        self.name_la2_2.setMinimumSize(QtCore.QSize(70, 25))
        self.name_la2_2.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_la2_2.setFont(font)
        self.name_la2_2.setObjectName("name_la2_2")
        self.name_sign_2 = QtWidgets.QLineEdit(self.page_2)
        self.name_sign_2.setGeometry(QtCore.QRect(110, 140, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name_sign_2.setFont(font)
        self.name_sign_2.setMaxLength(16)
        self.name_sign_2.setObjectName("name_sign_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Login_Window)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "Login Please"))
        self.name_la.setText(_translate("Login_Window", "用户名:"))
        self.pw_la.setText(_translate("Login_Window", "密码:"))
        self.login_btn.setText(_translate("Login_Window", "登录"))
        self.title1.setText(_translate("Login_Window", "鞋程账户登录"))
        self.signin_btn.setText(_translate("Login_Window", "没有账户？"))
        self.close_btn.setText(_translate("Login_Window", "退出"))
        self.failed.setText(_translate("Login_Window", "用户名或密码错误"))
        self.title2.setText(_translate("Login_Window", "买一双鞋，开启旅程"))
        self.name_la2.setText(_translate("Login_Window", "用户名:"))
        self.pw_la2.setText(_translate("Login_Window", "密码:"))
        self.signin_btn2.setText(_translate("Login_Window", "注册"))
        self.back_btn.setText(_translate("Login_Window", "返回"))
        self.invalid_name.setText(_translate("Login_Window", "用户名已存在"))
        self.name_la2_2.setText(_translate("Login_Window", "昵称:"))

