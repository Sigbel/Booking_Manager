# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 473)
        MainWindow.setStyleSheet("#btn_login{\n"
"    background-color:#f38d29;\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"#btn_login:pressed{\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #ecb177;\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"#btn_login:hover{\n"
"    background-color:#ecb177;\n"
"}\n"
"\n"
"#btn_recupera{\n"
"    background-color:#0000ffff\n"
"}\n"
"#btn_recupera:hover{\n"
"    color: #4b4b4b;\n"
"    background-color:#0000ffff\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(70, 20, 551, 201))
        self.columnView.setStyleSheet("background-color:#0000ffff")
        self.columnView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.columnView.setObjectName("columnView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 401, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("styles\\../Images/Entrada.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(140, 210, 401, 81))
        self.columnView_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0.131, x2:0, y2:1, stop:0 rgba(252, 132, 11, 255), stop:1 rgba(227, 197, 106, 255));\n"
"border-radius:8px;")
        self.columnView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.columnView_2.setObjectName("columnView_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.columnView_3 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_3.setGeometry(QtCore.QRect(220, 280, 241, 151))
        self.columnView_3.setStyleSheet("border-radius:8px;")
        self.columnView_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.columnView_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.columnView_3.setObjectName("columnView_3")
        self.scr_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.scr_usuario.setGeometry(QtCore.QRect(230, 310, 221, 21))
        self.scr_usuario.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.scr_usuario.setObjectName("scr_usuario")
        self.scr_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.scr_senha.setGeometry(QtCore.QRect(230, 340, 221, 21))
        self.scr_senha.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.scr_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.scr_senha.setObjectName("scr_senha")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(270, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 260, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.columnView.raise_()
        self.columnView_3.raise_()
        self.columnView_2.raise_()
        self.label_3.raise_()
        self.scr_usuario.raise_()
        self.scr_senha.raise_()
        self.btn_login.raise_()
        self.label_4.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Log In"))
        self.scr_usuario.setPlaceholderText(_translate("MainWindow", "Usuário"))
        self.scr_senha.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.btn_login.setText(_translate("MainWindow", "Log In"))
        self.label_4.setText(_translate("MainWindow", "CONTROLE DE RESERVAS"))
