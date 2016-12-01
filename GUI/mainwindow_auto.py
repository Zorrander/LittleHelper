# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setBaseSize(QtCore.QSize(800, 480))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget#Main{\n"
"    background-image: url(:/img/background.png)\n"
"}\n"
"\n"
"QWidget#MyPaths, QWidget#Cmd, QWidget#GeneralView, QWidget#TabMotors,QWidget#TabSensors,QWidget#TabCamera\n"
"{\n"
"    background-image: url(:/img/background2.png)\n"
"}\n"
"\n"
"QPushButton{\n"
"    border:none;\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 485))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setStyleSheet("")
        self.Main.setObjectName("Main")
        self.Icone = QtWidgets.QLabel(self.Main)
        self.Icone.setGeometry(QtCore.QRect(40, 130, 121, 291))
        self.Icone.setStyleSheet("background:none")
        self.Icone.setText("")
        self.Icone.setPixmap(QtGui.QPixmap(":/img/miles_power.png"))
        self.Icone.setObjectName("Icone")
        self.Title = QtWidgets.QTextBrowser(self.Main)
        self.Title.setGeometry(QtCore.QRect(280, 40, 301, 51))
        self.Title.setStyleSheet("background-color: rgb(255, 211, 134);\n"
"border:none;")
        self.Title.setObjectName("Title")
        self.myPathsButton = QtWidgets.QPushButton(self.Main)
        self.myPathsButton.setGeometry(QtCore.QRect(240, 140, 350, 40))
        self.myPathsButton.setStyleSheet("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.myPathsButton.setObjectName("myPathsButton")
        self.cmdButton = QtWidgets.QPushButton(self.Main)
        self.cmdButton.setGeometry(QtCore.QRect(270, 200, 350, 40))
        self.cmdButton.setStyleSheet("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.cmdButton.setObjectName("cmdButton")
        self.overviewButton = QtWidgets.QPushButton(self.Main)
        self.overviewButton.setGeometry(QtCore.QRect(300, 260, 350, 40))
        self.overviewButton.setStyleSheet("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.overviewButton.setObjectName("overviewButton")
        self.motorsButton = QtWidgets.QPushButton(self.Main)
        self.motorsButton.setGeometry(QtCore.QRect(330, 320, 350, 40))
        self.motorsButton.setStyleSheet("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.motorsButton.setObjectName("motorsButton")
        self.sensorsButton = QtWidgets.QPushButton(self.Main)
        self.sensorsButton.setGeometry(QtCore.QRect(360, 380, 350, 40))
        self.sensorsButton.setStyleSheet("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.sensorsButton.setObjectName("sensorsButton")
        self.tabWidget.addTab(self.Main, "")
        self.MyPaths = QtWidgets.QWidget()
        self.MyPaths.setObjectName("MyPaths")
        self.textBrowser = QtWidgets.QTextBrowser(self.MyPaths)
        self.textBrowser.setGeometry(QtCore.QRect(120, 40, 571, 41))
        self.textBrowser.setStyleSheet("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.pathButton = QtWidgets.QPushButton(self.MyPaths)
        self.pathButton.setGeometry(QtCore.QRect(90, 170, 500, 40))
        self.pathButton.setStyleSheet("background-color: rgb(254, 211, 133);")
        self.pathButton.setObjectName("pathButton")
        self.pathButton_2 = QtWidgets.QPushButton(self.MyPaths)
        self.pathButton_2.setGeometry(QtCore.QRect(90, 240, 500, 40))
        self.pathButton_2.setStyleSheet("background-color: rgb(255, 211, 134);")
        self.pathButton_2.setObjectName("pathButton_2")
        self.pathButton_3 = QtWidgets.QPushButton(self.MyPaths)
        self.pathButton_3.setGeometry(QtCore.QRect(90, 310, 500, 40))
        self.pathButton_3.setStyleSheet("background-color: rgb(255, 211, 134);")
        self.pathButton_3.setObjectName("pathButton_3")
        self.toolButton = QtWidgets.QToolButton(self.MyPaths)
        self.toolButton.setGeometry(QtCore.QRect(630, 170, 40, 40))
        self.toolButton.setStyleSheet("background-color: rgb(92, 5, 0);\n"
"color: rgb(255, 255, 255);")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.MyPaths)
        self.toolButton_2.setGeometry(QtCore.QRect(630, 240, 40, 40))
        self.toolButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 5, 0);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.MyPaths)
        self.toolButton_3.setGeometry(QtCore.QRect(630, 310, 40, 40))
        self.toolButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(97, 5, 0);\n"
"")
        self.toolButton_3.setObjectName("toolButton_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.MyPaths)
        self.textBrowser_2.setGeometry(QtCore.QRect(130, 436, 611, 25))
        self.textBrowser_2.setStyleSheet("background-color: rgb(98, 4, 0);\n"
"border:none")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.MyPaths, "")
        self.Cmd = QtWidgets.QWidget()
        self.Cmd.setObjectName("Cmd")
        self.forwardButton = QtWidgets.QPushButton(self.Cmd)
        self.forwardButton.setGeometry(QtCore.QRect(90, 170, 300, 40))
        self.forwardButton.setStyleSheet("background-color: rgb(254, 211, 133);")
        self.forwardButton.setObjectName("forwardButton")
        self.backwardButton = QtWidgets.QPushButton(self.Cmd)
        self.backwardButton.setGeometry(QtCore.QRect(90, 240, 300, 40))
        self.backwardButton.setStyleSheet("background-color: rgb(254, 211, 133);")
        self.backwardButton.setObjectName("backwardButton")
        self.stopButton = QtWidgets.QPushButton(self.Cmd)
        self.stopButton.setGeometry(QtCore.QRect(90, 310, 630, 40))
        self.stopButton.setStyleSheet("background-color: rgb(254, 211, 133);")
        self.stopButton.setObjectName("stopButton")
        self.commandsTabTitle = QtWidgets.QTextBrowser(self.Cmd)
        self.commandsTabTitle.setGeometry(QtCore.QRect(120, 40, 571, 41))
        self.commandsTabTitle.setStyleSheet("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.commandsTabTitle.setObjectName("commandsTabTitle")
        self.commandsFooter = QtWidgets.QTextBrowser(self.Cmd)
        self.commandsFooter.setGeometry(QtCore.QRect(130, 436, 611, 25))
        self.commandsFooter.setStyleSheet("background-color: rgb(98, 4, 0);\n"
"border:none")
        self.commandsFooter.setObjectName("commandsFooter")
        self.leftButton = QtWidgets.QPushButton(self.Cmd)
        self.leftButton.setGeometry(QtCore.QRect(420, 170, 300, 40))
        self.leftButton.setStyleSheet("background-color: rgb(254, 211, 133);")
        self.leftButton.setObjectName("leftButton")
        self.rightButton = QtWidgets.QPushButton(self.Cmd)
        self.rightButton.setGeometry(QtCore.QRect(420, 240, 300, 40))
        self.rightButton.setStyleSheet("background-color: rgb(254, 211, 133);")
        self.rightButton.setObjectName("rightButton")
        self.tabWidget.addTab(self.Cmd, "")
        self.GeneralView = QtWidgets.QWidget()
        self.GeneralView.setObjectName("GeneralView")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_5.setGeometry(QtCore.QRect(130, 436, 611, 25))
        self.textBrowser_5.setStyleSheet("background-color: rgb(98, 4, 0);\n"
"border:none")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_8.setGeometry(QtCore.QRect(120, 40, 571, 41))
        self.textBrowser_8.setStyleSheet("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label = QtWidgets.QLabel(self.GeneralView)
        self.label.setGeometry(QtCore.QRect(300, 160, 241, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/car-top-view.png"))
        self.label.setObjectName("label")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_3.setGeometry(QtCore.QRect(120, 170, 111, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_4.setGeometry(QtCore.QRect(120, 250, 111, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_11.setGeometry(QtCore.QRect(120, 330, 111, 41))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_12.setGeometry(QtCore.QRect(610, 250, 111, 41))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_13.setGeometry(QtCore.QRect(610, 330, 111, 41))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_14.setGeometry(QtCore.QRect(610, 170, 111, 41))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_15.setGeometry(QtCore.QRect(300, 110, 81, 41))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_16.setGeometry(QtCore.QRect(460, 110, 81, 41))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.GeneralView)
        self.textBrowser_17.setGeometry(QtCore.QRect(300, 400, 241, 31))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.tabWidget.addTab(self.GeneralView, "")
        self.TabMotors = QtWidgets.QWidget()
        self.TabMotors.setStyleSheet("")
        self.TabMotors.setObjectName("TabMotors")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.TabMotors)
        self.textBrowser_6.setGeometry(QtCore.QRect(130, 436, 611, 25))
        self.textBrowser_6.setStyleSheet("background-color: rgb(98, 4, 0);\n"
"border:none")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.TabMotors)
        self.textBrowser_9.setGeometry(QtCore.QRect(120, 40, 571, 41))
        self.textBrowser_9.setStyleSheet("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.tabWidget.addTab(self.TabMotors, "")
        self.TabSensors = QtWidgets.QWidget()
        self.TabSensors.setStyleSheet("")
        self.TabSensors.setObjectName("TabSensors")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.TabSensors)
        self.textBrowser_7.setGeometry(QtCore.QRect(130, 436, 611, 25))
        self.textBrowser_7.setStyleSheet("background-color: rgb(98, 4, 0);\n"
"border:none")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.TabSensors)
        self.textBrowser_10.setGeometry(QtCore.QRect(120, 40, 571, 41))
        self.textBrowser_10.setStyleSheet("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.tabWidget.addTab(self.TabSensors, "")
        self.TabCamera = QtWidgets.QWidget()
        self.TabCamera.setObjectName("TabCamera")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.TabCamera)
        self.textBrowser_18.setGeometry(QtCore.QRect(120, 40, 571, 41))
        self.textBrowser_18.setStyleSheet("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"")
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.videoFrame = QtWidgets.QLabel(self.TabCamera)
        self.videoFrame.setGeometry(QtCore.QRect(30, 110, 361, 311))
        self.videoFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.videoFrame.setText("")
        self.videoFrame.setObjectName("videoFrame")
        self.tabWidget.addTab(self.TabCamera, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MilesInterface"))
        self.Title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Little Helper </span></p></body></html>"))
        self.myPathsButton.setText(_translate("MainWindow", "My paths"))
        self.cmdButton.setText(_translate("MainWindow", "Commands"))
        self.overviewButton.setText(_translate("MainWindow", "Overview"))
        self.motorsButton.setText(_translate("MainWindow", "Motors "))
        self.sensorsButton.setText(_translate("MainWindow", "Sensors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), _translate("MainWindow", "Main"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Choose where you want to go </span></p></body></html>"))
        self.pathButton.setText(_translate("MainWindow", "Path A"))
        self.pathButton_2.setText(_translate("MainWindow", "Path B"))
        self.pathButton_3.setText(_translate("MainWindow", "Path C"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyPaths), _translate("MainWindow", "My paths"))
        self.forwardButton.setText(_translate("MainWindow", "Move forward"))
        self.backwardButton.setText(_translate("MainWindow", "Move backward"))
        self.stopButton.setText(_translate("MainWindow", "Emergency stop"))
        self.commandsTabTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Apply a simple command to the car</span></p></body></html>"))
        self.commandsFooter.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>"))
        self.leftButton.setText(_translate("MainWindow", "Turn left"))
        self.rightButton.setText(_translate("MainWindow", "Turn right"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cmd), _translate("MainWindow", "Commands"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">General state of the car</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Battery</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GeneralView), _translate("MainWindow", "Overview"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Motors diagnosis</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabMotors), _translate("MainWindow", "Motors"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Sensors diagnosis</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabSensors), _translate("MainWindow", "Sensors"))
        self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Camera point of view</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabCamera), _translate("MainWindow", "Camera"))

import GUI.res_rc
