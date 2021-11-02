from NextScreen import NextPage
class DriverWindow():
    # def __init__():
    def getdata(self):
        col=9
        data = []
        for row in range(NextPage.setupUi1.tableWidget.rowCount()):
          it = NextPage.setupUi1.tablewidget.item(row, col)
          text = it.text() if it is not None else ""
          data.append(text)
        print(data)
