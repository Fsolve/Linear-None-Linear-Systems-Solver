


from PyQt5 import QtCore, QtGui, QtWidgets
from SystemesLineaire import LUfunction as lu

class Ui_Windowlu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 630)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(220, 220, 187);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 100, 21, 141))
        self.line.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.line.setFont(font)
        self.line.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.a11 = QtWidgets.QLineEdit(self.centralwidget)
        self.a11.setGeometry(QtCore.QRect(120, 120, 31, 21))
        self.a11.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a11.setText("")
        self.a11.setObjectName("a11")
        self.a21 = QtWidgets.QLineEdit(self.centralwidget)
        self.a21.setGeometry(QtCore.QRect(120, 160, 31, 21))
        self.a21.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a21.setText("")
        self.a21.setObjectName("a21")
        self.a31 = QtWidgets.QLineEdit(self.centralwidget)
        self.a31.setGeometry(QtCore.QRect(120, 200, 31, 21))
        self.a31.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a31.setText("")
        self.a31.setObjectName("a31")
        self.a12 = QtWidgets.QLineEdit(self.centralwidget)
        self.a12.setGeometry(QtCore.QRect(180, 120, 31, 21))
        self.a12.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a12.setText("")
        self.a12.setObjectName("a12")
        self.a32 = QtWidgets.QLineEdit(self.centralwidget)
        self.a32.setGeometry(QtCore.QRect(180, 200, 31, 21))
        self.a32.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a32.setText("")
        self.a32.setObjectName("a32")
        self.a22 = QtWidgets.QLineEdit(self.centralwidget)
        self.a22.setGeometry(QtCore.QRect(180, 160, 31, 21))
        self.a22.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a22.setText("")
        self.a22.setObjectName("a22")
        self.a13 = QtWidgets.QLineEdit(self.centralwidget)
        self.a13.setGeometry(QtCore.QRect(240, 120, 31, 21))
        self.a13.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a13.setText("")
        self.a13.setObjectName("a13")
        self.a33 = QtWidgets.QLineEdit(self.centralwidget)
        self.a33.setGeometry(QtCore.QRect(240, 200, 31, 21))
        self.a33.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a33.setText("")
        self.a33.setObjectName("a33")
        self.a23 = QtWidgets.QLineEdit(self.centralwidget)
        self.a23.setGeometry(QtCore.QRect(240, 160, 31, 21))
        self.a23.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.a23.setText("")
        self.a23.setObjectName("a23")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(280, 100, 21, 141))
        self.line_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(120, 20, 471, 51))
        self.label_10.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.X = QtWidgets.QPushButton(self.centralwidget)
        self.X.setGeometry(QtCore.QRect(260, 290, 171, 41))
        self.X.clicked.connect(self.press) #IMPoooooortant !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.X.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.X.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"border-radius: 8px;\n"
"align:center;")
        self.X.setObjectName("X")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 140, 31, 51))
        self.label_14.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(380, 130, 41, 51))
        self.label_13.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(450, 100, 21, 141))
        self.line_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(510, 100, 21, 141))
        self.line_4.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.line_4.setFont(font)
        self.line_4.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.b1 = QtWidgets.QLineEdit(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(470, 120, 31, 21))
        self.b1.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.b3 = QtWidgets.QLineEdit(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(470, 200, 31, 21))
        self.b3.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.b2 = QtWidgets.QLineEdit(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(470, 160, 31, 21))
        self.b2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(645, 380, 21, 141))
        self.line_5.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.line_5.setFont(font)
        self.line_5.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.x1 = QtWidgets.QLabel(self.centralwidget)
        self.x1.setGeometry(QtCore.QRect(660, 400, 34, 21))
        self.x1.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.x1.setText("")
        self.x1.setObjectName("x1")
        self.x2 = QtWidgets.QLabel(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(660, 440, 34, 21))
        self.x2.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.x2.setText("")
        self.x2.setObjectName("x2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(595, 410, 41, 51))
        self.label_15.setStyleSheet("color: rgb(85, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(700, 380, 21, 141))
        self.line_6.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.line_6.setFont(font)
        self.line_6.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.x3 = QtWidgets.QLabel(self.centralwidget)
        self.x3.setGeometry(QtCore.QRect(660, 480, 34, 21))
        self.x3.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 170, 127);\n"
"color: rgb(85, 0, 0);")
        self.x3.setText("")
        self.x3.setObjectName("x3")
        self.Resultat = QtWidgets.QLabel(self.centralwidget)
        self.Resultat.setGeometry(QtCore.QRect(20, 370, 260, 221))
        self.Resultat.setText("")
        self.Resultat.setStyleSheet("border: 1px solid #ffaa7f;\n""color: rgb(85, 0, 0);\n""border-radius: 8px 8px 8px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"text-align:center")
        self.Resultat.setObjectName("Resultat")
        self.Resultat_2 = QtWidgets.QLabel(self.centralwidget)
        self.Resultat_2.setGeometry(QtCore.QRect(295, 370, 260, 221))
        self.Resultat_2.setText("")
        self.Resultat_2.setStyleSheet("border: 1px solid #ffaa7f;\n""color: rgb(85, 0, 0);\n""border-radius: 8px 8px 8px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"text-align:center")
        self.Resultat_2.setObjectName("Resultat_2")
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
        self.label_10.setText(_translate("MainWindow", "Resolution de Ax = B avec Decomposition LU"))
        self.X.setText(_translate("MainWindow", "   Calculer X "))
        self.label_14.setText(_translate("MainWindow", "A ="))
        self.label_13.setText(_translate("MainWindow", " B ="))
        self.label_15.setText(_translate("MainWindow", " x ="))
    def press(self):   #IMPOOOOOORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        A= [[float(self.a11.text()), float(self.a12.text()), float(self.a13.text())], [float(self.a21.text()), float(self.a22.text()), float(self.a23.text())], [float(self.a31.text()), float(self.a32.text()), float(self.a33.text())]]
        B=[float(self.b1.text()), float(self.b2.text()), float(self.b3.text())]  
        s = lu.solutionLU(A,B)
        Y =s[0]
        L =s[1]
        U = s[2]
        self.x1.setText(f'{Y[0]}')
        self.x2.setText(f'{Y[1]}')
        self.x3.setText(f'{Y[2]}')
        self.Resultat.setText(f'Matrice L :\n\n {L[0]}\n\n{L[1]}\n\n{L[2]}')
        self.Resultat_2.setText(f'Matrice U :\n\n {U[0]}\n\n{U[1]}\n\n{U[2]}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Windowlu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
