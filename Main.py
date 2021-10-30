from PyQt5 import QtCore, QtGui, QtWidgets
import time
from NextScreen import NextPage
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(907, 547)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("E:\\CS\\3rdsemester\\CS261F21PID25\\uploads/icons8-play-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.blackback = QtWidgets.QFrame(Dialog)
        self.blackback.setGeometry(QtCore.QRect(-50, 170, 961, 161))
        self.blackback.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.blackback.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blackback.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blackback.setObjectName("blackback")
        self.label_4 = QtWidgets.QLabel(self.blackback)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 131, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/WhatsApp Image 2021-10-10 at 6.33.24 PM (2).jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.blackback)
        self.label_3.setGeometry(QtCore.QRect(640, 10, 141, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/WhatsApp Image 2021-10-10 at 6.33.24 PM3.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 500, 71, 23))
        self.pushButton.setStyleSheet("background-color: rgb(22, 140, 63);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 500, 81, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(22, 140, 63);\n"
"font: 75 11pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.logo = QtWidgets.QFrame(Dialog)
        self.logo.setGeometry(QtCore.QRect(20, 20, 61, 51))
        self.logo.setStyleSheet("image: url(:/newPrefix/icons8-play-50.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 490, 61, 51))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(lambda status, n_size=100: self.run(n_size))
        self.pushButton_3.setStyleSheet("image: url(:/newPrefix/icons8-play-50.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.help = QtWidgets.QFrame(Dialog)
        self.help.setGeometry(QtCore.QRect(820, 10, 71, 41))
        self.help.setStyleSheet("image: url(:/newPrefix/icons8-question-64.png);")
        self.help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.help.setObjectName("help")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(180, 430, 561, 20))
        self.progressBar.setStyleSheet("QProgressBar:horizontal {\n"
"border-radius: 10px;\n"
"background: white;\n"
"text-align:center\n"
"\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"border-radius: 10px;\n"
"    background-color: rgb(22, 140, 63);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 120, 251, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/WhatsApp Image 2021-10-10 at 6.33.24 PM.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.blackback.raise_()
        self.label.raise_()
        self.logo.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.help.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.label_2.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Playlistical"))
        self.label.setText(_translate("Dialog", "Playlistical"))
        self.pushButton.setText(_translate("Dialog", "Stop"))
        self.pushButton_2.setText(_translate("Dialog", "Resume"))
    import sources_rc
    def run(self, n):
        self.w = None
        for i in range(n):
          time.sleep(0.01)
          self.progressBar.setValue(i+1)
        self.window=QtWidgets.QMainWindow()
        self.ui=NextPage()
        self.ui.setupUi1(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
