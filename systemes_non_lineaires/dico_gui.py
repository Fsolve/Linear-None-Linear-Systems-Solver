

from PyQt5 import QtCore, QtGui, QtWidgets
from dichotomie_func import dichotomie as dc


class Ui_secondWindow(object):
    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.setFixedSize(512, 634)
        secondWindow.setMinimumSize(QtCore.QSize(512, 0))
        secondWindow.setStyleSheet("color:rgb(53, 44, 72);\n"
"background-color: rgb(18, 141, 117);")
        secondWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputFunc = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFunc.setGeometry(QtCore.QRect(160, 80, 211, 71))
        self.inputFunc.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.inputFunc.setText("")
        self.inputFunc.setObjectName("inputFunc")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 71, 71))
        self.label_2.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 61, 71))
        self.label_3.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 150, 61, 71))
        self.label_4.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.aVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.aVal.setGeometry(QtCore.QRect(150, 150, 71, 71))
        self.aVal.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.aVal.setDecimals(3)
        self.aVal.setMinimum(-100.0)
        self.aVal.setMaximum(100.0)
        self.aVal.setSingleStep(0.1)
        self.aVal.setProperty("value", 0.0)
        self.aVal.setObjectName("aVal")
        self.bVal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.bVal.setGeometry(QtCore.QRect(280, 150, 91, 71))
        self.bVal.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-style: none;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.bVal.setDecimals(3)
        self.bVal.setMinimum(-100.0)
        self.bVal.setMaximum(100.0)
        self.bVal.setSingleStep(0.1)
        self.bVal.setObjectName("bVal")
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.clicked.connect(self.press)
        self.result.setGeometry(QtCore.QRect(140, 260, 171, 51))
        self.result.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255,255,255);\n"
"border-radius: 8px 8px 8px;")
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 541, 51))
        self.label.setStyleSheet("border-radius: 8px 8px 8px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Serif\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.resultfield = QtWidgets.QLabel(self.centralwidget)
        self.resultfield.setGeometry(QtCore.QRect(70, 330, 321, 181))
        self.resultfield.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius: 8px 8px 8px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"text-align:center")
        self.resultfield.setAlignment(QtCore.Qt.AlignCenter)
        self.resultfield.setObjectName("resultfield")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 542, 91, 41))
        self.pushButton.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(255,255,255);\n"
"border-radius: 8px 8px 8px;")
        self.pushButton.setObjectName("pushButton")
        secondWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(secondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 21))
        self.menubar.setObjectName("menubar")
        secondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "MainWindow"))
        self.label_2.setText(_translate("secondWindow", "  f(x)="))
        self.label_3.setText(_translate("secondWindow", "   a="))
        self.label_4.setText(_translate("secondWindow", "  b ="))
        self.result.setText(_translate("secondWindow", "Calculer"))
        self.label.setText(_translate("secondWindow", "Dicothomie:"))
        self.resultfield.setText(_translate("secondWindow", "here shows the result"))
        self.pushButton.setText(_translate("secondWindow", "Retour au Menu"))
    def press(self):   
            a = float(self.aVal.text())
            b = float(self.bVal.text())
            funstr = str(self.inputFunc.text())
            def f(x):
                return eval(funstr) #n.b eval function is not secure
            
            r = dc(f , a,b)
            self.resultfield.setText(f'resultat  :\na = {r[0]}\nb = {r[1]}\n c = {r[2]}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
