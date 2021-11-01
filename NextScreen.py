# from _typeshed import Self
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu, QTableWidgetItem, QTableWidget
from dropdownWindow import Ui_Form
import csv
import pandas as pd
class NextPage(object):
    def add_menu(self, data, menu_obj):
        if isinstance(data, dict):
            for k, v in data.items():
                sub_menu = QMenu(k, menu_obj)
                menu_obj.addMenu(sub_menu)
                self.add_menu(v, sub_menu)
        elif isinstance(data, list):
            for element in data:
                self.add_menu(element, menu_obj)
        else:
            action = menu_obj.addAction(data)
            action.setIconVisibleInMenu(False)
    def setupUi1(self, window):
        window.setObjectName("window")
        window.resize(901, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-play-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.tableWidget.setGeometry(QtCore.QRect(0, 130, 961, 431))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("tableWidget->setStyleSheet(\"QTableView::item:selected { color:white; background:#000000; font-weight:900; }\"\n"
"                           \"QTableCornerButton::section { background-color:#232326; }\"\n"
"                           \"QHeaderView::section { color:white; background-color:#232326; }\");")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        # self.tableWidget.setHorizontalHeaderItem(8, item)
        self.excelimport = QtWidgets.QPushButton(window)
        self.excelimport.setGeometry(QtCore.QRect(820, 10, 51, 51))
        self.excelimport.setStyleSheet("\n"
"background-color: rgb(40, 40, 40);\n"
"image: url(:/newPrefix/icons8-export-excel-96.png);")
        self.excelimport.setText("")
#        self.excelimport.clicked.connect()
        self.excelimport.setObjectName("excelimport")
        self.export_2 = QtWidgets.QLabel(window)
        self.export_2.setGeometry(QtCore.QRect(810, 60, 81, 20))
        self.export_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.export_2.setObjectName("export_2")
        states_cities = ['Sort Ascending ','Sort Descending ','Filter']
        #CREATING A DROPDOWN MENU 
        #AND ADDING SUBMENUS 
        menu = QMenu()
        menu.triggered.connect(lambda x: print(x.text()))
        self.add_menu(states_cities, menu)
        #DROPDOWN  MENU BUTTONS 
        self.Song = QtWidgets.QPushButton(window)
        self.Song.setMenu(menu)
        self.Song.setGeometry(QtCore.QRect(78, 131, 21, 23))

        
        self.Song.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Song.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-menu-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Song.setIcon(icon1)
        self.Song.setFlat(True)
        self.Song.setObjectName("Song")


        self.Album = QtWidgets.QPushButton(window)
        self.Album.setMenu(menu)
        self.Album.setGeometry(QtCore.QRect(180, 130, 21, 23))
        self.Album.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Album.setIcon(icon1)
        self.Album.setFlat(True)
        self.Album.setObjectName("Album")

        self.Genre = QtWidgets.QPushButton(window)
        self.Genre.setMenu(menu)
        self.Genre.setGeometry(QtCore.QRect(280, 130, 21, 23))
        self.Genre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Genre.setText("")
        self.Genre.setIcon(icon1)
        self.Genre.setFlat(True)
        self.Genre.setObjectName("Genre")

        self.Artist = QtWidgets.QPushButton(window)
        self.Artist.setMenu(menu)
        self.Artist.setGeometry(QtCore.QRect(380, 130, 21, 23))
        self.Artist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Artist.setText("")
        self.Artist.setIcon(icon1)
        self.Artist.setFlat(True)
        self.Artist.setObjectName("Artist")

        self.Likes = QtWidgets.QPushButton(window)
        self.Likes.setMenu(menu)
        self.Likes.setGeometry(QtCore.QRect(480, 130, 21, 23))
        self.Likes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Likes.setText("")
        self.Likes.setIcon(icon1)
        self.Likes.setFlat(True)
        self.Likes.setObjectName("Likes")

        self.TimesPLayed = QtWidgets.QPushButton(window)
        self.TimesPLayed.setMenu(menu)
        self.TimesPLayed.setGeometry(QtCore.QRect(580, 130, 21, 23))
        self.TimesPLayed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TimesPLayed.setText("")
        self.TimesPLayed.setIcon(icon1)
        self.TimesPLayed.setFlat(True)
        self.TimesPLayed.setObjectName("TimesPLayed")

        self.Duration = QtWidgets.QPushButton(window)
        self.Duration.setMenu(menu)
        self.Duration.setGeometry(QtCore.QRect(680, 130, 21, 23))
        self.Duration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Duration.setText("")
        self.Duration.setIcon(icon1)
        self.Duration.setFlat(True)
        self.Duration.setObjectName("Duration")

        self.Comment = QtWidgets.QPushButton(window)
        self.Comment.setMenu(menu)
        self.Comment.setGeometry(QtCore.QRect(780, 130, 21, 23))
        self.Comment.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Comment.setText("")
        self.Comment.setIcon(icon1)
        self.Comment.setFlat(True)
        self.Comment.setObjectName("Comment")

        self.Year = QtWidgets.QPushButton(window)
        self.Year.setMenu(menu)
        self.Year.setGeometry(QtCore.QRect(880, 130, 21, 23))
        self.Year.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Year.setText("")
        self.Year.setIcon(icon1)
        self.Year.setFlat(True)
        self.Year.setObjectName("Year")

        #Table Widget
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
        item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("window", "Song Title"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("window", "Album"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("window", "Genre"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("window", "Artist"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("window", "Likes"))
        # item = self.tableWidget.horizontalHeaderItem(5)
        # item.setText(_translate("window", "Times Played"))
        # item = self.tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("window", "Duration"))
        # item = self.tableWidget.horizontalHeaderItem(7)
        # item.setText(_translate("window", "Comments"))
        # item = self.tableWidget.horizontalHeaderItem(8)
        # item.setText(_translate("window", "Year"))
        self.export_2.setText(_translate("window", "Export To Excel"))
    
#Code to load data into table 
fileName = 'songsData.csv'
# def openFile():
#     try: 
#         Self.all_data = pd.read('songsData.csv')
#         NumRows = len(Self.all_data.index)
#         Self.tableWidget.setColumnCount(len(Self.all_data.columns))
#         Self.tableWidget.setRowCount(NumRows)
#         Self.tableWidget.setHorizontalHeaderLabels(Self.all_data.columns)
#         for i in range(NumRows):
#             for j in range(len(Self.all_data.columns)):
#                 Self.tableWidget.setItems(i,j,QTableWidgetItem(str(Self.all_data.iat[i,j])))
        
#         Self.tableWidget.resizeColumnsToContents()
#         Self.tableWidget.resizeRowsToContents()
#     except:
#         print("error occured")
        
        
def loadCsv(self, fileName):
    fileName = 'songsData.csv'
    with open(fileName, "r") as fileInput:
        for row in csv.reader(fileInput):    
            items = [
                QtGui.QStandardItem(field)
                for field in row
            ]
            self.model.appendRow(items)

def on_excelimport_clicked(self):
    fileName = 'songsData.csv'
    self.loadCsv(self.fileName)
    
import sources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = NextPage()
    ui.setupUi1(window)
    window.show()
    sys.exit(app.exec_())
