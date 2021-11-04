
import sources_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QDialog, QMenu, QMessageBox, QPushButton, QTableWidgetItem,QInputDialog
from dropdownWindow import *
import pandas as pd
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class NextPage(object):
    def __init__(self):
        self.count=0
    
     #MENU 
    def add_menu(self, data, menu_obj):
        if isinstance(data, list):
            for element in data:
                self.add_menu(element, menu_obj)
        else:
            action = menu_obj.addAction(data)
            action.setIconVisibleInMenu(False)

    def setupUi1(self, window):
        #DisplayButton
        self.btn = QtWidgets.QPushButton(window)
        self.btn.setGeometry(QtCore.QRect(850, 90, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setStyleSheet('QPushButton {background-color: rgb(29, 182, 83); color: white;}')
        self.btn.setText("Load Data")
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.run)
        window.setObjectName("window")
        window.resize(1000, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-play-50.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.playlistical = QtWidgets.QLabel(window)
        self.playlistical.setGeometry(QtCore.QRect(80, 30, 121, 21))
        self.playlistical.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 16pt \"Times New Roman\";\n"
                                        "font: 16pt \"Times New Roman\";")
        self.playlistical.setObjectName("playlistical")
        self.main = QtWidgets.QFrame(window)
        self.main.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.main.setStyleSheet("image: url(:/newPrefix/icons8-play-50.png);")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.tableWidget = QtWidgets.QTableWidget(window)
        self.tableWidget.setGeometry(QtCore.QRect(0, 130, 1000, 561))

        self.tableWidget.resizeColumnsToContents()
        font = QtGui.QFont()
        
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        # self.tableWidget.setColumnWidth(0, 1)
        # self.tableWidget.setColumnWidth(1, 10)
        # self.tableWidget.setColumnWidth(2, 10)
        self.tableWidget.setStyleSheet("color: black;"
            "background-color: white")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)


        self.excelimport = QtWidgets.QPushButton(window)
        self.excelimport.clicked.connect(self.showdialog)
        self.excelimport.setGeometry(QtCore.QRect(870, 10, 51, 51))
        self.excelimport.setStyleSheet("\n"
                                       "background-color: rgb(40, 40, 40);\n"
                                       "image: url(:/newPrefix/icons8-export-excel-96.png);")
        self.excelimport.setText("")
        self.excelimport.setObjectName("excelimport")
        self.export_2 = QtWidgets.QLabel(window)
        self.export_2.setGeometry(QtCore.QRect(860, 60, 81, 20))
        self.export_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.export_2.setObjectName("export_2")
        self.runtime = QtWidgets.QLabel(window)
        self.runtime.setGeometry(QtCore.QRect(100, 80, 81, 20))
        self.runtime.setStyleSheet("color: rgb(255, 255, 255);")
        self.runtime.setObjectName("runtime")
        self.runtime.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 70 14pt \"Times New Roman\";\n"
                                        "font: 14pt \"Times New Roman\";")
        sorting = ['Sort Ascending ', 'Sort Descending ', 'Filter']
        # CREATING A DROPDOWN MENU
        # AND ADDING SUBMENUS
        menu = QMenu()
        menu.triggered.connect(lambda x: self.FilterMenu(x.text()))
        self.add_menu(sorting, menu)
        # DROPDOWN  MENU BUTTONS
        self.Song = QtWidgets.QPushButton(window)

        self.Song.setMenu(menu)
        self.Song.setGeometry(QtCore.QRect(60, 131, 21, 23))
        self.Song.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Song.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            ":/newPrefix/icons8-menu-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Song.setIcon(icon1)
        self.Song.setFlat(True)
        self.Song.setObjectName("Song")

        self.Album = QtWidgets.QPushButton(window)
        self.Album.setMenu(menu)
        self.Album.setGeometry(QtCore.QRect(340, 130, 21, 23))
        self.Album.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Album.setIcon(icon1)
        self.Album.setFlat(True)
        self.Album.setObjectName("Album")

        self.Genre = QtWidgets.QPushButton(window)
        self.Genre.setMenu(menu)
        self.Genre.setGeometry(QtCore.QRect(460, 130, 21, 23))
        self.Genre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Genre.setText("")
        self.Genre.setIcon(icon1)
        self.Genre.setFlat(True)
        self.Genre.setObjectName("Genre")

        self.Artist = QtWidgets.QPushButton(window)
        self.Artist.setMenu(menu)
        self.Artist.setGeometry(QtCore.QRect(580, 130, 21, 23))
        self.Artist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Artist.setText("")
        self.Artist.setIcon(icon1)
        self.Artist.setFlat(True)
        self.Artist.setObjectName("Artist")

        self.Likes = QtWidgets.QPushButton(window)
        self.Likes.setMenu(menu)
        self.Likes.setGeometry(QtCore.QRect(720, 130, 21, 23))
        self.Likes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Likes.setText("")
        self.Likes.setIcon(icon1)
        self.Likes.setFlat(True)
        self.Likes.setObjectName("Likes")

        self.TimesPLayed = QtWidgets.QPushButton(window)
        self.TimesPLayed.setMenu(menu)
        self.TimesPLayed.setGeometry(QtCore.QRect(780, 130, 21, 23))
        self.TimesPLayed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TimesPLayed.setText("")
        self.TimesPLayed.setIcon(icon1)
        self.TimesPLayed.setFlat(True)
        self.TimesPLayed.setObjectName("TimesPLayed")

        self.Duration = QtWidgets.QPushButton(window)
        self.Duration.setMenu(menu)
        self.Duration.setGeometry(QtCore.QRect(840, 130, 21, 23))
        self.Duration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Duration.setText("")
        self.Duration.setIcon(icon1)
        self.Duration.setFlat(True)
        self.Duration.setObjectName("Duration")

        self.Comment = QtWidgets.QPushButton(window)
        self.Comment.setMenu(menu)
        self.Comment.setGeometry(QtCore.QRect(890, 130, 21, 23))
        self.Comment.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Comment.setText("")
        self.Comment.setIcon(icon1)
        self.Comment.setFlat(True)
        self.Comment.setObjectName("Comment")

        self.Year = QtWidgets.QPushButton(window)
        self.Year.setMenu(menu)
        self.Year.setGeometry(QtCore.QRect(950, 130, 21, 23))
        self.Year.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Year.setText("")
        self.Year.setIcon(icon1)
        self.Year.setFlat(True)
        self.Year.setObjectName("Year")

        # Table Widget
        self.tableWidget.raise_()
        self.playlistical.raise_()
        self.main.raise_()
        self.excelimport.raise_()
        self.export_2.raise_()
        self.Song.raise_()
        self.Album.raise_()
        self.Genre.raise_()
        self.Artist.raise_()
        self.Likes.raise_()
        self.TimesPLayed.raise_()
        self.Duration.raise_()
        self.Comment.raise_()
        self.Year.raise_()

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Playlistical"))
        self.playlistical.setText(_translate("window", "Playlistical"))
        self.export_2.setText(_translate("window", "Export To Excel"))
        self.runtime.setText(_translate("window", ": Run Time  "))

# Code to load data into table

    def run(self):
        #directdata from csv file to table
        import pandas as pd
        try:
            self.all_data = pd.read_csv('data.csv')
        except:
            print("An Error Occured!")
        
        NumRows = len(self.all_data.index)
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
    

    def FilterMenu(self,text):
        if(text=='Filter'):
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()
        if(text=='Sort Ascending '):
            self.count=self.getTextInputDialog()
            self.tableWidget.sortItems(self.count, QtCore.Qt.AscendingOrder)
        if(text=='Sort Descending '):
            self.count=self.getTextInputDialog()
            self.tableWidget.sortItems(self.count, QtCore.Qt.DescendingOrder)
    def getTextInputDialog(self):
        integer , pressed = QInputDialog.getInt(None, "Input Column Number","Column:", 0, 0, 9, 1)
        if pressed:
         return integer
    def showdialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("For More Updated Version Stay Tuned")
        msgBox.setWindowTitle("Export to Excel")
        msgBox.setStandardButtons(QMessageBox.Cancel)
        msgBox.exec()
      
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = NextPage()
    ui.setupUi1(window)
    window.show()
    sys.exit(app.exec_())
    