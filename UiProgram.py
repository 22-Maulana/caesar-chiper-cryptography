# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mtkdiskrit.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 768)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -20, 1021, 141))
        self.frame.setStyleSheet("background-color: rgb(32, 74, 135)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 20, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(243, 243, 243)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 401, 17))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(170, 60, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(237, 212, 0);")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 111, 111))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("LOGO UNESA.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, 119, 521, 601))
        self.frame_2.setStyleSheet("background-color: rgb(46, 52, 54)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(237, 212, 0);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.textEdit_isi_encrypt = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_isi_encrypt.setGeometry(QtCore.QRect(190, 100, 311, 181))
        self.textEdit_isi_encrypt.setAutoFillBackground(False)
        self.textEdit_isi_encrypt.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255)\n"
"")
        self.textEdit_isi_encrypt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_isi_encrypt.setLineWidth(10)
        self.textEdit_isi_encrypt.setObjectName("textEdit_isi_encrypt")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.lineEdit_pass_encrypt = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_pass_encrypt.setGeometry(QtCore.QRect(190, 320, 311, 25))
        self.lineEdit_pass_encrypt.setStyleSheet("color: rgb(255, 255, 255)")
        self.lineEdit_pass_encrypt.setObjectName("lineEdit_pass_encrypt")
        self.pushButton_encrypt = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_encrypt.setGeometry(QtCore.QRect(30, 410, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.pushButton_encrypt.setFont(font)
        self.pushButton_encrypt.setStyleSheet("background-color: rgb(41, 212, 31);\n"
"text-color: rgb(255, 255, 255)")
        self.pushButton_encrypt.setObjectName("pushButton_encrypt")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 350, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_8.setObjectName("label_8")
        self.textEdit_chiperkey_encrypt = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_chiperkey_encrypt.setGeometry(QtCore.QRect(190, 360, 311, 221))
        self.textEdit_chiperkey_encrypt.setAutoFillBackground(False)
        self.textEdit_chiperkey_encrypt.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255)\n"
"")
        self.textEdit_chiperkey_encrypt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_chiperkey_encrypt.setLineWidth(10)
        self.textEdit_chiperkey_encrypt.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit_chiperkey_encrypt.setObjectName("textEdit_chiperkey_encrypt")
        self.pushButton_clear_encrypt = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_clear_encrypt.setGeometry(QtCore.QRect(30, 520, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_clear_encrypt.setFont(font)
        self.pushButton_clear_encrypt.setStyleSheet("background-color: rgb(206, 92, 0)")
        self.pushButton_clear_encrypt.setObjectName("pushButton_clear_encrypt")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(509, 119, 521, 601))
        self.frame_3.setStyleSheet("background-color : rgb(46, 52, 54)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(237, 212, 0);")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 290, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_11.setObjectName("label_11")
        self.lineEdit_pasword_decrypt = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_pasword_decrypt.setGeometry(QtCore.QRect(190, 300, 311, 25))
        self.lineEdit_pasword_decrypt.setStyleSheet("color: rgb(255, 255, 255)")
        self.lineEdit_pasword_decrypt.setObjectName("lineEdit_pasword_decrypt")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.textEdit_chiperkey_decrypt = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_chiperkey_decrypt.setGeometry(QtCore.QRect(190, 100, 311, 171))
        self.textEdit_chiperkey_decrypt.setAutoFillBackground(False)
        self.textEdit_chiperkey_decrypt.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255)\n"
"")
        self.textEdit_chiperkey_decrypt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_chiperkey_decrypt.setLineWidth(10)
        self.textEdit_chiperkey_decrypt.setObjectName("textEdit_chiperkey_decrypt")
        self.textEdit_isi_decrypt = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_isi_decrypt.setGeometry(QtCore.QRect(190, 350, 311, 231))
        self.textEdit_isi_decrypt.setAutoFillBackground(False)
        self.textEdit_isi_decrypt.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255)\n"
"")
        self.textEdit_isi_decrypt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_isi_decrypt.setLineWidth(10)
        self.textEdit_isi_decrypt.setObjectName("textEdit_isi_decrypt")
        self.pushButton_clear_decrypt = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_clear_decrypt.setGeometry(QtCore.QRect(20, 520, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_clear_decrypt.setFont(font)
        self.pushButton_clear_decrypt.setStyleSheet("background-color: rgb(206, 92, 0)")
        self.pushButton_clear_decrypt.setObjectName("pushButton_clear_decrypt")
        self.pushButton_decrypt = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_decrypt.setGeometry(QtCore.QRect(20, 410, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_decrypt.setFont(font)
        self.pushButton_decrypt.setStyleSheet("background-color: rgb(226, 225, 34);")
        self.pushButton_decrypt.setObjectName("pushButton_decrypt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Program Kriptografi Matematika Diskrit"))
        self.label.setText(_translate("MainWindow", "CAESAR CHIPER KRIPTOGRAFI"))
        self.label_2.setText(_translate("MainWindow", "Oleh Kelompok 35 Prodi S1 Teknik Informatika 2023"))
        self.label_3.setText(_translate("MainWindow", "Universitas Negeri Surabaya"))
        self.label_4.setText(_translate("MainWindow", "ENCRYPT"))
        self.label_6.setText(_translate("MainWindow", "Input Isi           :"))
        self.label_7.setText(_translate("MainWindow", "Input Pasword :"))
        self.pushButton_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label_8.setText(_translate("MainWindow", "Chiper Key       :"))
        self.pushButton_clear_encrypt.setText(_translate("MainWindow", "Clear"))
        self.label_5.setText(_translate("MainWindow", "DECRYPT"))
        self.label_10.setText(_translate("MainWindow", "Chiper Key       :"))
        self.label_11.setText(_translate("MainWindow", "Password         :"))
        self.label_12.setText(_translate("MainWindow", "Isi Text              :"))
        self.pushButton_clear_decrypt.setText(_translate("MainWindow", "Clear"))
        self.pushButton_decrypt.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
