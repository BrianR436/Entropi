# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EntropiacCYcBj.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from Recursos import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        MainWindow.setMaximumSize(QSize(1000, 800))
        icon = QIcon()
        icon.addFile(u":/iconos/h.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget\n"
"{\n"
"	background-color:#BDBDBD;\n"
"	color: #3104B4;\n"
"	border-color:#000000;\n"
"}\n"
"QTableWidget\n"
"{\n"
"	background-color:#E6E6E6;\n"
"\n"
"	border-color:#000000;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ejecutar = QPushButton(self.centralwidget)
        self.ejecutar.setObjectName(u"ejecutar")
        self.ejecutar.setGeometry(QRect(590, 520, 75, 24))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 8):
            self.tableWidget.setRowCount(8)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 200, 641, 311))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.tableWidget.setFont(font)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(500)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(30, 30, 641, 71))
        font1 = QFont()
        font1.setPointSize(13)
        self.plainTextEdit.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 110, 381, 31))
        self.ruta = QLineEdit(self.centralwidget)
        self.ruta.setObjectName(u"ruta")
        self.ruta.setGeometry(QRect(30, 140, 641, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Entropia", None))
#if QT_CONFIG(statustip)
        self.ejecutar.setStatusTip(QCoreApplication.translate("MainWindow", u"Asegurate de poner la ruta del fichero", None))
#endif // QT_CONFIG(statustip)
        self.ejecutar.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Datos del fichero", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fuente", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Probabilidad de cada letra", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Informacion de cada letra", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Caracteres leidos", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Entropia", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Informacion total", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Redudancia", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Eficiencia", None));
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Pr\u00e1tica 1. Entropia de un texto como fuente de memoria nula.\n"
"", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese la ruta del fichero de texto", None))
#if QT_CONFIG(statustip)
        self.ruta.setStatusTip(QCoreApplication.translate("MainWindow", u"Ingrese la ruta.", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

