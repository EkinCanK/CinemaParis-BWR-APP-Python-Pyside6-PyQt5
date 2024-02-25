import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import sqlite3
import webbrowser

from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)

from Main.UI.main_window import Ui_mw_Main
from Persons.add_person import AddPerson
from Application_Login.login import LoginForm
from Add_A_DCP.addDCP import AddDCP
from Add_A_DCP.Ui.AddaDCP_window import Ui_AddaDCP_window
from Daily_Task_Management.main_daily import mainDaily
from KDM.kdm import kdm_management
from Add_A_Trailer.addTrailer import AddTrailer
from Add_A_Trailer.UI.AddaTrailer_window import Ui_AddaTrailer_window


#create a custom class
class MainWindow(qtw.QMainWindow, Ui_mw_Main, Ui_AddaDCP_window, Ui_AddaTrailer_window): #i always want to inherit what
#ecer q is , window or dialog or label etc..
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Quit.triggered.connect(self.close) # instead of clicked trigger
        self.action_Add_Person.triggered.connect(self.open_add_person)

        self.form = LoginForm() # login emits a signal when the log in is 
        #succesfull, so i need to do sth when i get it.
        self.form.login_success.connect(self.show) # if i m successfull in login,
        # the signal is gonna show us the main window.
        self.form.show() # we took it out from main down

        self.pb_GoToYorck.clicked.connect(self.open_Web_Page_Link)
        self.pb_AddDCP.clicked.connect(self.open_add_a_DCP)
        self.pb_AddTrailer.clicked.connect(self.open_add_a_Trailer)
        self.pb_DailyTaskCalenderMS.clicked.connect(self.open_DailyTaskCalenderMS)

        self.tw_tableWidgetToDo.setColumnWidth(0,720)
        self.tw_tableWidgetToDo.setColumnWidth(1,90)

        self.pb_Load.clicked.connect(self.loadData)
        self.pb_clearTable.clicked.connect(self.deleteTable)

        self.tw_tableWidgetToDo_KDM.setColumnWidth(0,100)
        self.tw_tableWidgetToDo_KDM.setColumnWidth(1,125)
        self.tw_tableWidgetToDo_KDM.setColumnWidth(2,125)
        self.tw_tableWidgetToDo_KDM.setColumnWidth(3,150)
        self.tw_tableWidgetToDo_KDM.setColumnWidth(4,100)
        self.tw_tableWidgetToDo_KDM.setColumnWidth(5,100)
        self.tw_tableWidgetToDo_KDM.setColumnWidth(6,100)

        self.pb_Load_KDM.clicked.connect(self.loadDataKDM)
        self.pb_clearTable_KDM.clicked.connect(self.deleteTableKDM)

        self.pb_KDMConrtolSystem.clicked.connect(self.open_KDMControlSystem)


        self.pb_anleitungen.clicked.connect(self.anleitungen)

    @qtc.Slot()
    def deleteTable(self):

        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/data.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()
        query = ("SELECT * FROM tasks WHERE completed = 'NO'")
        results = cursor.execute(query)
        row = 0
        self.tw_tableWidgetToDo.setRowCount(len(database))
        for results in cursor:
            self.tw_tableWidgetToDo.removeRow(row)

        cursor.close()

    @qtc.Slot()
    def deleteTableKDM(self):

        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/kdms.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()
        query = ("SELECT * FROM kdms_list ")
        results = cursor.execute(query)
        row = 0
        self.tw_tableWidgetToDo_KDM.setRowCount(len(database))
        for results in cursor:
            self.tw_tableWidgetToDo_KDM.removeRow(row)

        cursor.close()

    @qtc.Slot()
    def loadDataKDM(self):
        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/kdms.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()
        query = ("SELECT * FROM kdms_list ")
        results = cursor.execute(query)
        row=0
        self.tw_tableWidgetToDo_KDM.setRowCount(len(database))
        for results in cursor:
            self.tw_tableWidgetToDo_KDM.setItem(row, 0, qtw.QTableWidgetItem(results[0])) # task
            self.tw_tableWidgetToDo_KDM.setItem(row, 1, qtw.QTableWidgetItem(results[1])) # date
            self.tw_tableWidgetToDo_KDM.setItem(row, 2, qtw.QTableWidgetItem(results[2])) # date
            self.tw_tableWidgetToDo_KDM.setItem(row, 3, qtw.QTableWidgetItem(results[3])) # date
            self.tw_tableWidgetToDo_KDM.setItem(row, 4, qtw.QTableWidgetItem(results[5])) # date
            self.tw_tableWidgetToDo_KDM.setItem(row, 5, qtw.QTableWidgetItem(results[6])) # date
            self.tw_tableWidgetToDo_KDM.setItem(row, 6, qtw.QTableWidgetItem(results[4])) # date
            row=row+1
        cursor.close()

    @qtc.Slot()
    def loadData(self):
        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/data.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()
        query = ("SELECT * FROM tasks WHERE completed = 'NO'")
        results = cursor.execute(query)
        row=0
        self.tw_tableWidgetToDo.setRowCount(len(database))
        for results in cursor:
            self.tw_tableWidgetToDo.setItem(row, 0, qtw.QTableWidgetItem(results[0])) # task
            self.tw_tableWidgetToDo.setItem(row, 1, qtw.QTableWidgetItem(results[2])) # date

            row=row+1
        cursor.close()

    @qtc.Slot()
    def open_add_person(self):
        self.form = AddPerson()
        self.form.exec()  # this one create whole another event loop until that 
        #loop ends. also there is a difference btw .open and . exec.

    @qtc.Slot()
    def open_add_a_Trailer(self):
        self.window = AddTrailer()
        self.window.show()

    @qtc.Slot()
    def open_KDMControlSystem(self):
        self.window = kdm_management()
        self.window.show()

    @qtc.Slot()
    def open_Web_Page_Link(self):

        # Where the webpage is rendered.
        self.webview = QWebEngineView()
        self.webview.setWindowTitle("Cinema Paris in Yorck Web Seite")
        self.webview.setGeometry(300, 300, 1250, 1000)
        self.webview.load(QUrl("https://yorck.de/kinos/cinema-paris"))
        self.webview.show()
    @qtc.Slot()
    def open_add_a_DCP(self):
        self.window = AddDCP()
        self.window.show()

    @qtc.Slot()
    def open_DailyTaskCalenderMS(self):
        self.window = mainDaily()
        self.window.show()

    @qtc.Slot()
    def anleitungen(self):

        webbrowser.open_new(r'/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/anleitungen.pdf')

#TEST:now we set a new main block, just for test reasons with run command, 
#iterative testing so that we use how it functions and looks
if __name__=="__main__":
    app =qtw.QApplication(sys.argv)

    window = MainWindow()
    #window.show() i took this out  to do login conditiional to main window

    sys.exit(app.exec())
