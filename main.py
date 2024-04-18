import string
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import *
from PyQt5 import uic

abjad = string.printable

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("mtkdiskrit.ui", self)
        
        self.input_teks_isi_encrypt = self.textEdit_isi_encrypt
        self.input_pass_encrypt = self.lineEdit_pass_encrypt
        self.pushButton_encrypt.clicked.connect(self.encrypt)
        
        self.input_chiper_decrypt = self.textEdit_chiperkey_decrypt
        self.input_key_decrypt = self.lineEdit_pasword_decrypt
        self.pushButton_decrypt.clicked.connect(self.decript)

        self.pushButton_clear_encrypt.clicked.connect(self.ClearEncrypt)
        self.pushButton_clear_decrypt.clicked.connect(self.ClearDecrypt)

        self.show()


    def encrypt(self):
        global abjad
        pesan = self.input_teks_isi_encrypt.toPlainText()
        chiper = ''
        key = int(self.input_pass_encrypt.text())
        for i in pesan:
          if i in abjad:
            k = abjad.find(i)
            k = (k + key) % 100
            chiper = chiper + abjad[k]
          else:
            chiper = chiper + i
        self.textEdit_chiperkey_encrypt.setText(chiper)


    def decript(self):
        global abjad
        key = int(self.input_key_decrypt.text())
        pesan = ''
        chiper = self.input_chiper_decrypt.toPlainText()
        for i in chiper:
           if i in abjad:
            k = abjad.find(i)
            k = (k - key) % 100
            pesan = pesan + abjad[k]
        self.textEdit_isi_decrypt.setText(pesan)
        

    def ClearEncrypt(self):
       self.textEdit_isi_encrypt.setText("")
       self.lineEdit_pass_encrypt.setText("")
       self.textEdit_chiperkey_encrypt.setText("")


    def ClearDecrypt(self):
       self.lineEdit_pasword_decrypt.setText("")
       self.textEdit_chiperkey_decrypt.setText("")
       self.textEdit_isi_decrypt.setText("")

        
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()