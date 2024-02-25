import os
import sys
from PySide6 import QtWidgets as qtw
import sqlite3

from datetime import datetime

now = datetime.now() # current date and time



from KDM.UI.kdm_window import Ui_KDM_Control # Note: standard name in other python file

class kdm_management(qtw.QWidget, Ui_KDM_Control):
    def __init__(self):
        super().__init__() # initialization of the parent in this case QWidget
        self.setupUi(self)
        self.pb_addAndSave.clicked.connect(self.addAndSave)
        self.pb_deleteAll.clicked.connect(self.deleteallKDMentry)
        self.pb_deleteAllTable.clicked.connect(self.deleteallTABLE)
        self.pb_showInfo.clicked.connect(self.ShowFeaturesandKDMinfoUpdate)
        self.pb_update.clicked.connect(self.update_data)
        self.pb_pick.clicked.connect(self.call_data)

        #self.pb_insertData.clicked.connect(self.insert_data)



    #def insert_data(self):
    #    self.cursor = self.create_connection().cursor()


#        self.cursor.execute("create table kdms_list(Feature,required,ingested,ingestionDT,ingestedBY,ValidityDATEfrom,ValidityDATEto)")

#        self.List_of_kdms= [("a","b","c","d","e","f","g"),
#                            ("a","b","c","d","e","f","g"),
#                            ("a","b","c","d","e","f","g"),
#                            ("a","b","c","d","e","f","g"),
#                            ]

#        self.cursor.executemany("Insert into kdms_list values (?,?,?,?,?,?,?)",self.List_of_kdms)
#        print("inserted demo data succesfully")
#        self.connection.commit()
#        self.connection.close()
#####
    def create_connection(self):
        os.chdir(r"/home/karasu/PycharmProjects/pythonProjectMainCP_GUI_Application/db")
        self.connection = sqlite3.connect("kdms.db")
        return self.connection

    def addAndSave(self):
        self.cursor = self.create_connection().cursor()

        self.new_kdms =[
            self.le_featureName.text(),
            self.le_required.text(),
            self.le_ingested.text(),
            self.dte_ingestedDate.text(),
            self.le_ingestedBy.text(),
            self.dte_from.text(),
            self.dte_to.text(),
        ]

        self.cursor.execute("Insert into kdms_list values(?,?,?,?,?,?,?)", self.new_kdms)

        #print("New KDM is added: ",self.le_featureName.text())


        self.le_featureName.clear()
        self.le_required.clear()
        self.le_ingested.clear()
        self.dte_ingestedDate.clear()
        self.le_ingestedBy.clear()
        self.dte_from.clear()
        self.dte_to.clear()
        self.connection.commit()
        self.connection.close()

        messageBox = qtw.QMessageBox()
        messageBox.setText("New KDM is added to database, press Refresh KDM Info Table button to refresh the table.")
        messageBox.setStandardButtons(qtw.QMessageBox.Ok)
        messageBox.exec()

        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        log1='KDM is added by manager on {}'.format(date_time)
        self.log_KDM(log1)

    def log_KDM(self,log1):

        f = open('logFile_KDM.txt', 'a')
        print(log1, file=f)
        print('logFile_KDM is written')


    def deleteallKDMentry(self):
        self.le_featureName.clear()
        self.le_required.clear()
        self.le_ingested.clear()
        self.dte_ingestedDate.clear()
        self.le_ingestedBy.clear()
        self.dte_from.clear()
        self.dte_to.clear()



    def deleteallTABLE(self):
        self.cursor = self.create_connection().cursor()
        current_row_index = self.tv_tableWidget.currentRow()

        feature_item = str(self.tv_tableWidget.item(current_row_index,0).text())
        if current_row_index < 0:
            Warning = qtw.QMessageBox.warning(self, 'Warning','Please select a record to delete.')
        else:
            message = qtw.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the selected row?', qtw.QMessageBox.StandardButton.Yes | qtw.QMessageBox.StandardButton.No )

        if message == qtw.QMessageBox.StandardButton.Yes:
            sqlquery =" DELETE FROM kdms_list WHERE Feature=?"
            self.cursor.execute(sqlquery, (feature_item,))
            #print("You deleted ", feature_item)
            Warning = qtw.QMessageBox.warning(self, 'Warning', 'KDM is deleted from the table.To refresh the table push the Refresh KDM Info Table button.')
        self.connection.commit()
        self.connection.close()

        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        log2 = 'KDM is deleted by manager on {}'.format(date_time)
        self.log_KDM_del(log2)

    def log_KDM_del(self, log2):

        f = open('logFile_KDM.txt', 'a')
        print(log2, file=f)

    def ShowFeaturesandKDMinfoUpdate(self):

        self.cursor = self.create_connection().cursor()
        rowCount_sqlquery = "SELECT COUNT(*) FROM kdms_list"
        kdms_sqlquery = "SELECT *FROM kdms_list"

        self.cursor.execute(rowCount_sqlquery)
        results = self.cursor.fetchone()
        #print("Number of rows: ",results[0])
        self.tv_tableWidget.setRowCount(results[0])

        table_row=0
        for i in self.cursor.execute(kdms_sqlquery):
            self.tv_tableWidget.setItem(table_row, 0 , qtw.QTableWidgetItem(i[0]))
            self.tv_tableWidget.setItem(table_row, 1 , qtw.QTableWidgetItem(i[1]))
            self.tv_tableWidget.setItem(table_row, 2 , qtw.QTableWidgetItem(i[2]))
            self.tv_tableWidget.setItem(table_row, 3 , qtw.QTableWidgetItem(i[3]))
            self.tv_tableWidget.setItem(table_row, 4 , qtw.QTableWidgetItem(i[4]))
            self.tv_tableWidget.setItem(table_row, 5 , qtw.QTableWidgetItem(i[5]))
            self.tv_tableWidget.setItem(table_row, 6 , qtw.QTableWidgetItem(i[6]))
            table_row= table_row +1

        self.le_featureName.clear()
        self.le_required.clear()
        self.le_ingested.clear()
        self.dte_ingestedDate.clear()
        self.le_ingestedBy.clear()
        self.dte_from.clear()
        self.dte_to.clear()

    def call_data(self):
        current_row_index = self.tv_tableWidget.currentRow()

        if current_row_index < 0:
            Warning = qtw.QMessageBox.warning(self, 'Warning','Please select a record first.')
        else:

            self.Feature_edit = str(self.tv_tableWidget.item(current_row_index,0).text())
            self.required_edit = str(self.tv_tableWidget.item(current_row_index,1).text())
            self.ingested_edit = str(self.tv_tableWidget.item(current_row_index,2).text())
            self.ingestionDT_edit = str(self.tv_tableWidget.item(current_row_index,3))
            self.ingestedBY_edit = str(self.tv_tableWidget.item(current_row_index,4).text())
            self.ValidityDATEfrom_edit = str(self.tv_tableWidget.item(current_row_index,5))
            self.ValidityDATEto_edit = str(self.tv_tableWidget.item(current_row_index,6))

            self.le_featureName.setText(self.Feature_edit)
            self.le_required.setText(self.required_edit)
            self.le_ingested.setText(self.ingested_edit)
            self.le_ingestedBy.setText(self.ingestedBY_edit)
    def update_data(self):
        self.cursor = self.create_connection().cursor()
        rowCount_sqlquery = "SELECT COUNT(*) FROM kdms_list"
        kdms_sqlquery = "SELECT *FROM kdms_list"

        self.cursor.execute(rowCount_sqlquery)
        results = self.cursor.fetchone()
        #print("Number of rows: ", results[0])
        self.tv_tableWidget.setRowCount(results[0])

        table_row = 0
        for i in self.cursor.execute(kdms_sqlquery):
            self.tv_tableWidget.setItem(table_row, 0, qtw.QTableWidgetItem(i[0]))
            self.tv_tableWidget.setItem(table_row, 1, qtw.QTableWidgetItem(i[1]))
            self.tv_tableWidget.setItem(table_row, 2, qtw.QTableWidgetItem(i[2]))
            self.tv_tableWidget.setItem(table_row, 3, qtw.QTableWidgetItem(i[3]))
            self.tv_tableWidget.setItem(table_row, 4, qtw.QTableWidgetItem(i[4]))
            self.tv_tableWidget.setItem(table_row, 5, qtw.QTableWidgetItem(i[5]))
            self.tv_tableWidget.setItem(table_row, 6, qtw.QTableWidgetItem(i[6]))
            table_row = table_row + 1

        self.le_featureName.clear()
        self.le_required.clear()
        self.le_ingested.clear()
        self.dte_ingestedDate.clear()
        self.le_ingestedBy.clear()
        self.dte_from.clear()
        self.dte_to.clear()



if __name__=="__main__":
    app =qtw.QApplication(sys.argv)

    window = kdm_management()
    window.show()


    sys.exit(app.exec())