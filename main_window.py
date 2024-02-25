# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import Icons_rc

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.setWindowModality(Qt.WindowModal)
        mw_Main.resize(921, 805)
        mw_Main.setMaximumSize(QSize(921, 805))
        icon = QIcon()
        icon.addFile(u":/Main/CP.png", QSize(), QIcon.Normal, QIcon.Off)
        mw_Main.setWindowIcon(icon)
        mw_Main.setAutoFillBackground(False)
        self.action_Quit = QAction(mw_Main)
        self.action_Quit.setObjectName(u"action_Quit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Quit.setIcon(icon1)
        self.action_Add_Person = QAction(mw_Main)
        self.action_Add_Person.setObjectName(u"action_Add_Person")
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"background-color:rgb(153, 193, 241)")
        self.lb_Logo = QLabel(self.centralwidget)
        self.lb_Logo.setObjectName(u"lb_Logo")
        self.lb_Logo.setGeometry(QRect(20, 10, 271, 241))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 240, 361, 17))
        self.tw_tableWidgetToDo = QTableWidget(self.centralwidget)
        if (self.tw_tableWidgetToDo.columnCount() < 2):
            self.tw_tableWidgetToDo.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_tableWidgetToDo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_tableWidgetToDo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tw_tableWidgetToDo.setObjectName(u"tw_tableWidgetToDo")
        self.tw_tableWidgetToDo.setGeometry(QRect(20, 280, 861, 171))
        self.tw_tableWidgetToDo.setStyleSheet(u"background-color :rgb(255, 255, 255)")
        self.tw_tableWidgetToDo.setRowCount(0)
        self.pb_Load = QPushButton(self.centralwidget)
        self.pb_Load.setObjectName(u"pb_Load")
        self.pb_Load.setGeometry(QRect(20, 460, 141, 25))
        self.pb_Load.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(153, 193, 241);\n"
"selection-color: yellow;\n"
"selection-background-color: red;\n"
"border: 2px solid red;\n"
"border-radius: 8px;\n"
"font-size: 11pt")
        self.pb_clearTable = QPushButton(self.centralwidget)
        self.pb_clearTable.setObjectName(u"pb_clearTable")
        self.pb_clearTable.setGeometry(QRect(180, 460, 141, 25))
        self.pb_clearTable.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(153, 193, 241);\n"
"selection-color: yellow;\n"
"selection-background-color: red;\n"
"border: 2px solid red;\n"
"border-radius: 8px;\n"
"font-size: 11pt")
        self.pb_GoToYorck = QPushButton(self.centralwidget)
        self.pb_GoToYorck.setObjectName(u"pb_GoToYorck")
        self.pb_GoToYorck.setGeometry(QRect(290, 80, 291, 61))
        self.pb_GoToYorck.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(224, 27, 36);\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"border: 6px solid blue;\n"
"border-radius: 8px;\n"
"font-size: 12pt")
        self.pb_KDMConrtolSystem = QPushButton(self.centralwidget)
        self.pb_KDMConrtolSystem.setObjectName(u"pb_KDMConrtolSystem")
        self.pb_KDMConrtolSystem.setGeometry(QRect(590, 80, 291, 61))
        self.pb_KDMConrtolSystem.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(224, 27, 36);\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"border: 6px solid blue;\n"
"border-radius: 8px;\n"
"font-size: 12pt")
        self.pb_AddDCP = QPushButton(self.centralwidget)
        self.pb_AddDCP.setObjectName(u"pb_AddDCP")
        self.pb_AddDCP.setGeometry(QRect(290, 10, 291, 61))
        self.pb_AddDCP.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(224, 27, 36);\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"border: 6px solid blue;\n"
"border-radius: 8px;\n"
"font-size: 12pt")
        self.pb_DailyTaskCalenderMS = QPushButton(self.centralwidget)
        self.pb_DailyTaskCalenderMS.setObjectName(u"pb_DailyTaskCalenderMS")
        self.pb_DailyTaskCalenderMS.setGeometry(QRect(290, 150, 291, 61))
        self.pb_DailyTaskCalenderMS.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(224, 27, 36);\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"border: 6px solid blue;\n"
"border-radius: 8px;\n"
"font-size: 11pt")
        self.pb_AddTrailer = QPushButton(self.centralwidget)
        self.pb_AddTrailer.setObjectName(u"pb_AddTrailer")
        self.pb_AddTrailer.setGeometry(QRect(590, 10, 291, 61))
        self.pb_AddTrailer.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(224, 27, 36);\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"border: 6px solid blue;\n"
"border-radius: 8px;\n"
"font-size: 12pt")
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(900, 0, 20, 761))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.tw_tableWidgetToDo_KDM = QTableWidget(self.centralwidget)
        if (self.tw_tableWidgetToDo_KDM.columnCount() < 7):
            self.tw_tableWidgetToDo_KDM.setColumnCount(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_tableWidgetToDo_KDM.setHorizontalHeaderItem(6, __qtablewidgetitem8)
        self.tw_tableWidgetToDo_KDM.setObjectName(u"tw_tableWidgetToDo_KDM")
        self.tw_tableWidgetToDo_KDM.setGeometry(QRect(20, 500, 861, 171))
        self.tw_tableWidgetToDo_KDM.setStyleSheet(u"background-color :rgb(255, 255, 255)")
        self.tw_tableWidgetToDo_KDM.setRowCount(0)
        self.tw_tableWidgetToDo_KDM.verticalHeader().setMinimumSectionSize(50)
        self.tw_tableWidgetToDo_KDM.verticalHeader().setDefaultSectionSize(50)
        self.pb_Load_KDM = QPushButton(self.centralwidget)
        self.pb_Load_KDM.setObjectName(u"pb_Load_KDM")
        self.pb_Load_KDM.setGeometry(QRect(20, 680, 151, 25))
        self.pb_Load_KDM.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(153, 193, 241);\n"
"selection-color: yellow;\n"
"selection-background-color: red;\n"
"border: 2px solid red;\n"
"border-radius: 8px;\n"
"font-size: 11pt")
        self.pb_clearTable_KDM = QPushButton(self.centralwidget)
        self.pb_clearTable_KDM.setObjectName(u"pb_clearTable_KDM")
        self.pb_clearTable_KDM.setGeometry(QRect(190, 680, 141, 25))
        self.pb_clearTable_KDM.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(153, 193, 241);\n"
"selection-color: yellow;\n"
"selection-background-color: red;\n"
"border: 2px solid red;\n"
"border-radius: 8px;\n"
"font-size: 11pt")
        self.pb_anleitungen = QPushButton(self.centralwidget)
        self.pb_anleitungen.setObjectName(u"pb_anleitungen")
        self.pb_anleitungen.setGeometry(QRect(590, 150, 291, 61))
        self.pb_anleitungen.setStyleSheet(u"color: rgb(246, 245, 244);\n"
"background-color: rgb(224, 27, 36);\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"border: 6px solid blue;\n"
"border-radius: 8px;\n"
"font-size: 12pt")
        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 921, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPerson = QMenu(self.menubar)
        self.menuPerson.setObjectName(u"menuPerson")
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPerson.menuAction())
        self.menuFile.addAction(self.action_Quit)
        self.menuPerson.addAction(self.action_Add_Person)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"CP Application Main Page", None))
        self.action_Quit.setText(QCoreApplication.translate("mw_Main", u"Quit", None))
        self.action_Add_Person.setText(QCoreApplication.translate("mw_Main", u"Add Person", None))
        self.lb_Logo.setText(QCoreApplication.translate("mw_Main", u"<html><head/><body><p><img src=\":/Main/CP.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("mw_Main", u"A new horizon in the world of a film projectionist...", None))
        ___qtablewidgetitem = self.tw_tableWidgetToDo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mw_Main", u"To Do List", None));
        ___qtablewidgetitem1 = self.tw_tableWidgetToDo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mw_Main", u"Due Date", None));
        self.pb_Load.setText(QCoreApplication.translate("mw_Main", u"Load To Do List", None))
        self.pb_clearTable.setText(QCoreApplication.translate("mw_Main", u"Clear To Do List", None))
        self.pb_GoToYorck.setText(QCoreApplication.translate("mw_Main", u"Go to yorck.com", None))
        self.pb_KDMConrtolSystem.setText(QCoreApplication.translate("mw_Main", u"KDM Control System", None))
        self.pb_AddDCP.setText(QCoreApplication.translate("mw_Main", u"Add a DCP", None))
        self.pb_DailyTaskCalenderMS.setText(QCoreApplication.translate("mw_Main", u"Daily Task Calendar Management System", None))
        self.pb_AddTrailer.setText(QCoreApplication.translate("mw_Main", u"Add a Trailer", None))
        ___qtablewidgetitem2 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mw_Main", u"Feature", None));
        ___qtablewidgetitem3 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mw_Main", u"KDM required?", None));
        ___qtablewidgetitem4 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mw_Main", u"KDM Ingested?", None));
        ___qtablewidgetitem5 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mw_Main", u"Ingestion Date/Time", None));
        ___qtablewidgetitem6 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mw_Main", u"Valid from...", None));
        ___qtablewidgetitem7 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mw_Main", u"Valid to...", None));
        ___qtablewidgetitem8 = self.tw_tableWidgetToDo_KDM.horizontalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mw_Main", u"Ingested by ", None));
        self.pb_Load_KDM.setText(QCoreApplication.translate("mw_Main", u"Load KDM Table List", None))
        self.pb_clearTable_KDM.setText(QCoreApplication.translate("mw_Main", u"Clear KDM Table", None))
        self.pb_anleitungen.setText(QCoreApplication.translate("mw_Main", u"BWR Anleitungen", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_Main", u"File", None))
        self.menuPerson.setTitle(QCoreApplication.translate("mw_Main", u"Person", None))
    # retranslateUi

