
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from AlgorithmClass import *


class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(264, 392)
        Form.setAutoFillBackground(False)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint )
        Form.setWindowFlags(flags)
        Form.setStyleSheet("\n""background-color: rgb(255,255,255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0,0,0);")
        self.label.setObjectName("label")
       
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
       

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 100, 181, 31))
        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(20, 350, 81, 31))
        self.pushButton.clicked.connect(self.FilterFun)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(29, 182, 83);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 350, 81, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(7, 8, 38);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 300, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
      
        
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 200, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
       
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Show items with value that:"))
        self.comboBox.setItemText(0, _translate("Form", "None"))
        self.comboBox.setItemText(1, _translate("Form", "is Equal to"))
        self.comboBox.setItemText(2, _translate("Form", "is not Equal to"))
        self.comboBox.setItemText(3, _translate("Form", "Contains"))
        self.comboBox.setItemText(4, _translate("Form", "Does not Contains"))
        self.comboBox.setItemText(5, _translate("Form", "Starts With"))
        self.pushButton.setText(_translate("Form", "Filter"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.comboBox_5.setItemText(0, _translate("Form", "None"))
        self.comboBox_5.setItemText(1, _translate("Form", "Add"))
        self.comboBox_5.setItemText(2, _translate("Form", "Or"))
        self.comboBox_3.setItemText(0, _translate("Form", "Merge Sort"))
        self.comboBox_3.setItemText(1, _translate("Form", "Insertion Sort"))
        self.comboBox_3.setItemText(2, _translate("Form", "Selection Sort"))
        self.comboBox_3.setItemText(3, _translate("Form", "Bubble Sort"))
        self.comboBox_3.setItemText(4, _translate("Form", "Quick Sort"))
        self.comboBox_3.setItemText(5, _translate("Form", "Heap Sort"))
        self.comboBox_3.setItemText(6, _translate("Form", "Counting Sort"))
        self.comboBox_3.setItemText(7, _translate("Form", "Shell Sort"))
        self.comboBox_3.setItemText(8, _translate("Form", "Radix Sort"))

        self.comboBox_2.setItemText(0, _translate("Form", "None"))
        self.comboBox_2.setItemText(1, _translate("Form", "is Equal to"))
        self.comboBox_2.setItemText(2, _translate("Form", "is not Equal to"))
        self.comboBox_2.setItemText(3, _translate("Form", "Contains"))
        self.comboBox_2.setItemText(4, _translate("Form", "Does not Contains"))
        self.comboBox_2.setItemText(5, _translate("Form", "Starts With"))

    #when filter button is pressed
    #return input value to funtion for filtering
    def FilterFun(self):
        firstTextBox = self.textEdit.toPlainText()
        secondTextBox= self.textEdit_2.toPlainText()
        content = self.comboBox.currentText()
        content4 = self.comboBox_2.currentText()
        content2 = self.comboBox_3.currentText()
        content3 = self.comboBox_5.currentText()
        filter(firstTextBox,secondTextBox,content,content3,content4,content2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
