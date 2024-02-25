import sys
import numpy as np
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QListWidgetItem
from PySide6 import QtGui as qtg
import sqlite3
import pandas as pd
import os

from Daily_Task_Management.UI.main_daily_window import Ui_Form # Note: standard name in other python file

class mainDaily(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__() # initialization of the parent in this case QWidget
        self.setupUi(self)
        self.cw_calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.pb_SaveChanges.clicked.connect(self.saveChanges)
        self.pb_addTask.clicked.connect(self.addNewTask)
        self.pb_removeTask.clicked.connect(self.removeTask)

    def calendarDateChanged(self):
        #print("The calender date was changed.") # check purposes , i will extract the date info to use later in database.
        dateSelected =self.cw_calendarWidget.selectedDate().toPython() # now we turned it from string to pydata or so to say python data. Later on we need to convert it to string again. You can also format the date by adding .strftime("%m-%d") or sort only year .strftime("%Y") (best format for software developer))
        #print("Date selected.", dateSelected) # it is converted to string
        self.updateTaskList(dateSelected)
    def updateTaskList(self, date):
#        for task in tasks:
#            #add them to list widget
#            item = qtw.QListWidgetItem(task)
#            item.setFlags(item.flags()  |  qtc.Qt.ItemIsUserCheckable)
#            item.setCheckState(qtc.Qt.Unchecked)
#            self.lw_listWidget.addItem(item)
        self.lw_listWidget.clear()

        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/data.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()
        query = ("SELECT task, completed FROM tasks WHERE date = ?")

        row = (date,)
        results = cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | qtc.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(qtc.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(qtc.Qt.Unchecked)
            self.lw_listWidget.addItem(item)


    def saveChanges(self):
        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/data.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()
        date = self.cw_calendarWidget.selectedDate().toPython()

        for i in range(self.lw_listWidget.count()):
            item = self.lw_listWidget.item(i)
            task = item.text()
            if item.checkState() == qtc.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            cursor.execute(query, row)
        db.commit()

        messageBox = qtw.QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(qtw.QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/data.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        date = self.cw_calendarWidget.selectedDate().toPython()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)

        cursor.execute(query, row)
        db.commit() # commit our changes
        self.updateTaskList(date)
        self.taskLineEdit.clear()

    def removeTask(self):

        database = r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db/data.db"
        db = sqlite3.connect(database)
        cursor = db.cursor()

        current_row_index = self.lw_listWidget.currentRow()

        name_item = str(self.lw_listWidget.item(current_row_index))



        if current_row_index < 0:
            Warning = qtw.QMessageBox.warning(self, 'Warning','Please select a record to delete')
        else:
            message = qtw.QMessageBox.question(self, 'Confirmation', 'Are you sure that you want to delete selected task from database?', qtw.QMessageBox.StandardButton.Yes | qtw.QMessageBox.StandardButton.No)

        if message == qtw.QMessageBox.StandardButton.Yes:
            sqlDeleteQuery = """DELETE from tasks where task = ?"""
            cursor.execute(sqlDeleteQuery, (name_item,))
            clicked = self.lw_listWidget.currentRow()
            self.lw_listWidget.takeItem(clicked)
            print("Record deleted successfully ")
        db.commit()

        cursor.close()


if __name__=="__main__":
    app =qtw.QApplication(sys.argv)

    window = mainDaily()
    window.show()

    sys.exit(app.exec())