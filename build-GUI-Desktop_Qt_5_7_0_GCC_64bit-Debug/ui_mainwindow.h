/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *Main;
    QLabel *Icone;
    QTextBrowser *Title;
    QPushButton *myPathsButton;
    QPushButton *cmdButton;
    QPushButton *overviewButton;
    QPushButton *motorsButton;
    QPushButton *sensorsButton;
    QWidget *MyPaths;
    QTextBrowser *textBrowser;
    QPushButton *pathButton;
    QPushButton *pathButton_2;
    QPushButton *pathButton_3;
    QToolButton *toolButton;
    QToolButton *toolButton_2;
    QToolButton *toolButton_3;
    QTextBrowser *textBrowser_2;
    QWidget *Cmd;
    QPushButton *pathButton_4;
    QPushButton *pathButton_5;
    QPushButton *pathButton_6;
    QTextBrowser *textBrowser_3;
    QTextBrowser *textBrowser_4;
    QPushButton *pathButton_7;
    QPushButton *pathButton_8;
    QWidget *GeneralView;
    QTextBrowser *textBrowser_5;
    QTextBrowser *textBrowser_8;
    QWidget *TabMotors;
    QTextBrowser *textBrowser_6;
    QTextBrowser *textBrowser_9;
    QWidget *TabSensors;
    QTextBrowser *textBrowser_7;
    QTextBrowser *textBrowser_10;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(800, 480);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setMinimumSize(QSize(800, 480));
        MainWindow->setMaximumSize(QSize(800, 480));
        MainWindow->setBaseSize(QSize(800, 480));
        MainWindow->setAutoFillBackground(false);
        MainWindow->setStyleSheet(QLatin1String("QWidget#Main{\n"
"	background-image: url(:/img/background.png)\n"
"}\n"
"\n"
"QWidget#MyPaths, QWidget#Cmd, QWidget#GeneralView, QWidget#TabMotors,QWidget#TabSensors{\n"
"	background-image: url(:/img/background2.png)\n"
"}\n"
"\n"
"QPushButton{\n"
"	border:none;\n"
"}"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        centralWidget->setStyleSheet(QStringLiteral(""));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setEnabled(true);
        tabWidget->setGeometry(QRect(0, 0, 800, 485));
        tabWidget->setAutoFillBackground(false);
        tabWidget->setStyleSheet(QStringLiteral(""));
        Main = new QWidget();
        Main->setObjectName(QStringLiteral("Main"));
        Main->setStyleSheet(QStringLiteral(""));
        Icone = new QLabel(Main);
        Icone->setObjectName(QStringLiteral("Icone"));
        Icone->setGeometry(QRect(40, 130, 121, 291));
        Icone->setStyleSheet(QStringLiteral("background:none"));
        Icone->setPixmap(QPixmap(QString::fromUtf8(":/img/miles_power.png")));
        Title = new QTextBrowser(Main);
        Title->setObjectName(QStringLiteral("Title"));
        Title->setGeometry(QRect(280, 40, 301, 51));
        Title->setStyleSheet(QLatin1String("background-color: rgb(255, 211, 134);\n"
"border:none;"));
        myPathsButton = new QPushButton(Main);
        myPathsButton->setObjectName(QStringLiteral("myPathsButton"));
        myPathsButton->setGeometry(QRect(240, 140, 350, 40));
        myPathsButton->setStyleSheet(QLatin1String("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
""));
        cmdButton = new QPushButton(Main);
        cmdButton->setObjectName(QStringLiteral("cmdButton"));
        cmdButton->setGeometry(QRect(270, 200, 350, 40));
        cmdButton->setStyleSheet(QLatin1String("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
""));
        overviewButton = new QPushButton(Main);
        overviewButton->setObjectName(QStringLiteral("overviewButton"));
        overviewButton->setGeometry(QRect(300, 260, 350, 40));
        overviewButton->setStyleSheet(QLatin1String("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
""));
        motorsButton = new QPushButton(Main);
        motorsButton->setObjectName(QStringLiteral("motorsButton"));
        motorsButton->setGeometry(QRect(330, 320, 350, 40));
        motorsButton->setStyleSheet(QLatin1String("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
""));
        sensorsButton = new QPushButton(Main);
        sensorsButton->setObjectName(QStringLiteral("sensorsButton"));
        sensorsButton->setGeometry(QRect(360, 380, 350, 40));
        sensorsButton->setStyleSheet(QLatin1String("background-color: rgb(98, 5, 0);\n"
"color: rgb(255, 255, 255);\n"
""));
        tabWidget->addTab(Main, QString());
        MyPaths = new QWidget();
        MyPaths->setObjectName(QStringLiteral("MyPaths"));
        textBrowser = new QTextBrowser(MyPaths);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(120, 40, 571, 41));
        textBrowser->setStyleSheet(QLatin1String("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
""));
        pathButton = new QPushButton(MyPaths);
        pathButton->setObjectName(QStringLiteral("pathButton"));
        pathButton->setGeometry(QRect(90, 170, 500, 40));
        pathButton->setStyleSheet(QStringLiteral("background-color: rgb(254, 211, 133);"));
        pathButton_2 = new QPushButton(MyPaths);
        pathButton_2->setObjectName(QStringLiteral("pathButton_2"));
        pathButton_2->setGeometry(QRect(90, 240, 500, 40));
        pathButton_2->setStyleSheet(QStringLiteral("background-color: rgb(255, 211, 134);"));
        pathButton_3 = new QPushButton(MyPaths);
        pathButton_3->setObjectName(QStringLiteral("pathButton_3"));
        pathButton_3->setGeometry(QRect(90, 310, 500, 40));
        pathButton_3->setStyleSheet(QStringLiteral("background-color: rgb(255, 211, 134);"));
        toolButton = new QToolButton(MyPaths);
        toolButton->setObjectName(QStringLiteral("toolButton"));
        toolButton->setGeometry(QRect(630, 170, 40, 40));
        toolButton->setStyleSheet(QLatin1String("background-color: rgb(92, 5, 0);\n"
"color: rgb(255, 255, 255);"));
        toolButton_2 = new QToolButton(MyPaths);
        toolButton_2->setObjectName(QStringLiteral("toolButton_2"));
        toolButton_2->setGeometry(QRect(630, 240, 40, 40));
        toolButton_2->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 5, 0);"));
        toolButton_3 = new QToolButton(MyPaths);
        toolButton_3->setObjectName(QStringLiteral("toolButton_3"));
        toolButton_3->setGeometry(QRect(630, 310, 40, 40));
        toolButton_3->setStyleSheet(QLatin1String("color: rgb(255, 255, 255);\n"
"background-color: rgb(97, 5, 0);\n"
""));
        textBrowser_2 = new QTextBrowser(MyPaths);
        textBrowser_2->setObjectName(QStringLiteral("textBrowser_2"));
        textBrowser_2->setGeometry(QRect(130, 436, 611, 25));
        textBrowser_2->setStyleSheet(QLatin1String("background-color: rgb(98, 4, 0);\n"
"border:none"));
        tabWidget->addTab(MyPaths, QString());
        Cmd = new QWidget();
        Cmd->setObjectName(QStringLiteral("Cmd"));
        pathButton_4 = new QPushButton(Cmd);
        pathButton_4->setObjectName(QStringLiteral("pathButton_4"));
        pathButton_4->setGeometry(QRect(90, 170, 300, 40));
        pathButton_4->setStyleSheet(QStringLiteral("background-color: rgb(254, 211, 133);"));
        pathButton_5 = new QPushButton(Cmd);
        pathButton_5->setObjectName(QStringLiteral("pathButton_5"));
        pathButton_5->setGeometry(QRect(90, 240, 300, 40));
        pathButton_5->setStyleSheet(QStringLiteral("background-color: rgb(254, 211, 133);"));
        pathButton_6 = new QPushButton(Cmd);
        pathButton_6->setObjectName(QStringLiteral("pathButton_6"));
        pathButton_6->setGeometry(QRect(90, 310, 630, 40));
        pathButton_6->setStyleSheet(QStringLiteral("background-color: rgb(254, 211, 133);"));
        textBrowser_3 = new QTextBrowser(Cmd);
        textBrowser_3->setObjectName(QStringLiteral("textBrowser_3"));
        textBrowser_3->setGeometry(QRect(120, 40, 571, 41));
        textBrowser_3->setStyleSheet(QLatin1String("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
""));
        textBrowser_4 = new QTextBrowser(Cmd);
        textBrowser_4->setObjectName(QStringLiteral("textBrowser_4"));
        textBrowser_4->setGeometry(QRect(130, 436, 611, 25));
        textBrowser_4->setStyleSheet(QLatin1String("background-color: rgb(98, 4, 0);\n"
"border:none"));
        pathButton_7 = new QPushButton(Cmd);
        pathButton_7->setObjectName(QStringLiteral("pathButton_7"));
        pathButton_7->setGeometry(QRect(420, 170, 300, 40));
        pathButton_7->setStyleSheet(QStringLiteral("background-color: rgb(254, 211, 133);"));
        pathButton_8 = new QPushButton(Cmd);
        pathButton_8->setObjectName(QStringLiteral("pathButton_8"));
        pathButton_8->setGeometry(QRect(420, 240, 300, 40));
        pathButton_8->setStyleSheet(QStringLiteral("background-color: rgb(254, 211, 133);"));
        tabWidget->addTab(Cmd, QString());
        GeneralView = new QWidget();
        GeneralView->setObjectName(QStringLiteral("GeneralView"));
        textBrowser_5 = new QTextBrowser(GeneralView);
        textBrowser_5->setObjectName(QStringLiteral("textBrowser_5"));
        textBrowser_5->setGeometry(QRect(130, 436, 611, 25));
        textBrowser_5->setStyleSheet(QLatin1String("background-color: rgb(98, 4, 0);\n"
"border:none"));
        textBrowser_8 = new QTextBrowser(GeneralView);
        textBrowser_8->setObjectName(QStringLiteral("textBrowser_8"));
        textBrowser_8->setGeometry(QRect(120, 40, 571, 41));
        textBrowser_8->setStyleSheet(QLatin1String("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
""));
        tabWidget->addTab(GeneralView, QString());
        TabMotors = new QWidget();
        TabMotors->setObjectName(QStringLiteral("TabMotors"));
        TabMotors->setStyleSheet(QStringLiteral(""));
        textBrowser_6 = new QTextBrowser(TabMotors);
        textBrowser_6->setObjectName(QStringLiteral("textBrowser_6"));
        textBrowser_6->setGeometry(QRect(130, 436, 611, 25));
        textBrowser_6->setStyleSheet(QLatin1String("background-color: rgb(98, 4, 0);\n"
"border:none"));
        textBrowser_9 = new QTextBrowser(TabMotors);
        textBrowser_9->setObjectName(QStringLiteral("textBrowser_9"));
        textBrowser_9->setGeometry(QRect(120, 40, 571, 41));
        textBrowser_9->setStyleSheet(QLatin1String("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
""));
        tabWidget->addTab(TabMotors, QString());
        TabSensors = new QWidget();
        TabSensors->setObjectName(QStringLiteral("TabSensors"));
        TabSensors->setStyleSheet(QStringLiteral(""));
        textBrowser_7 = new QTextBrowser(TabSensors);
        textBrowser_7->setObjectName(QStringLiteral("textBrowser_7"));
        textBrowser_7->setGeometry(QRect(130, 436, 611, 25));
        textBrowser_7->setStyleSheet(QLatin1String("background-color: rgb(98, 4, 0);\n"
"border:none"));
        textBrowser_10 = new QTextBrowser(TabSensors);
        textBrowser_10->setObjectName(QStringLiteral("textBrowser_10"));
        textBrowser_10->setGeometry(QRect(120, 40, 571, 41));
        textBrowser_10->setStyleSheet(QLatin1String("background-color: rgb(114, 114, 114);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
""));
        tabWidget->addTab(TabSensors, QString());
        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MilesInterface", 0));
        Icone->setText(QString());
        Title->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Little Helper </span></p></body></html>", 0));
        myPathsButton->setText(QApplication::translate("MainWindow", "My paths", 0));
        cmdButton->setText(QApplication::translate("MainWindow", "Commands", 0));
        overviewButton->setText(QApplication::translate("MainWindow", "Overview", 0));
        motorsButton->setText(QApplication::translate("MainWindow", "Motors ", 0));
        sensorsButton->setText(QApplication::translate("MainWindow", "Sensors", 0));
        tabWidget->setTabText(tabWidget->indexOf(Main), QApplication::translate("MainWindow", "Main", 0));
        textBrowser->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Choose where you want to go </span></p></body></html>", 0));
        pathButton->setText(QApplication::translate("MainWindow", "Path A", 0));
        pathButton_2->setText(QApplication::translate("MainWindow", "Path B", 0));
        pathButton_3->setText(QApplication::translate("MainWindow", "Path C", 0));
        toolButton->setText(QApplication::translate("MainWindow", "...", 0));
        toolButton_2->setText(QApplication::translate("MainWindow", "...", 0));
        toolButton_3->setText(QApplication::translate("MainWindow", "...", 0));
        textBrowser_2->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(MyPaths), QApplication::translate("MainWindow", "My paths", 0));
        pathButton_4->setText(QApplication::translate("MainWindow", "Move forward", 0));
        pathButton_5->setText(QApplication::translate("MainWindow", "Move backward", 0));
        pathButton_6->setText(QApplication::translate("MainWindow", "Emergency stop", 0));
        textBrowser_3->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Apply a simple command to the car</span></p></body></html>", 0));
        textBrowser_4->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>", 0));
        pathButton_7->setText(QApplication::translate("MainWindow", "Turn left", 0));
        pathButton_8->setText(QApplication::translate("MainWindow", "Turn right", 0));
        tabWidget->setTabText(tabWidget->indexOf(Cmd), QApplication::translate("MainWindow", "Commands", 0));
        textBrowser_5->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>", 0));
        textBrowser_8->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">General state of the car</span></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(GeneralView), QApplication::translate("MainWindow", "Overview", 0));
        textBrowser_6->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>", 0));
        textBrowser_9->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Motors diagnostic</span></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(TabMotors), QApplication::translate("MainWindow", "Motors", 0));
        textBrowser_7->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Miles Prower 2017.</span></p></body></html>", 0));
        textBrowser_10->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Sensors diagnostic</span></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(TabSensors), QApplication::translate("MainWindow", "Sensors", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
