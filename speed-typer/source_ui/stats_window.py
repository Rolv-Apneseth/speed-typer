# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statsWindow(object):
    def setupUi(self, statsWindow):
        statsWindow.setObjectName("statsWindow")
        statsWindow.resize(832, 952)
        statsWindow.setStyleSheet("QWidget {\n"
"    background: rgb(50, 50, 50);\n"
"    color: rgb(235, 235, 235);\n"
"    font-size: 24pt;\n"
"}\n"
"\n"
"QFrame {    \n"
"    border: 1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"QPushButton, QComboBox {    \n"
"    background: rgb(70, 70, 70);\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton::hover, QComboBox::hover {\n"
"    background: rgb(90, 90, 90)\n"
"}\n"
"\n"
"QLabel {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"] {\n"
"    background-color: rgb(235, 235, 235);\n"
"}")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(statsWindow)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.frameCurrent = QtWidgets.QFrame(statsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameCurrent.sizePolicy().hasHeightForWidth())
        self.frameCurrent.setSizePolicy(sizePolicy)
        self.frameCurrent.setMinimumSize(QtCore.QSize(0, 200))
        self.frameCurrent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCurrent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCurrent.setObjectName("frameCurrent")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameCurrent)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelCurrentHighscores = QtWidgets.QLabel(self.frameCurrent)
        self.labelCurrentHighscores.setStyleSheet("font-weight: bold; font-size: 28pt;")
        self.labelCurrentHighscores.setObjectName("labelCurrentHighscores")
        self.verticalLayout_3.addWidget(self.labelCurrentHighscores)
        self.line = QtWidgets.QFrame(self.frameCurrent)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelToday = QtWidgets.QLabel(self.frameCurrent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelToday.sizePolicy().hasHeightForWidth())
        self.labelToday.setSizePolicy(sizePolicy)
        self.labelToday.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelToday.setObjectName("labelToday")
        self.horizontalLayout_2.addWidget(self.labelToday)
        self.labelTodayScore = QtWidgets.QLabel(self.frameCurrent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTodayScore.sizePolicy().hasHeightForWidth())
        self.labelTodayScore.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.labelTodayScore.setFont(font)
        self.labelTodayScore.setObjectName("labelTodayScore")
        self.horizontalLayout_2.addWidget(self.labelTodayScore)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelAllTIme = QtWidgets.QLabel(self.frameCurrent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAllTIme.sizePolicy().hasHeightForWidth())
        self.labelAllTIme.setSizePolicy(sizePolicy)
        self.labelAllTIme.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelAllTIme.setObjectName("labelAllTIme")
        self.horizontalLayout_3.addWidget(self.labelAllTIme)
        self.labelAllTimeScore = QtWidgets.QLabel(self.frameCurrent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAllTimeScore.sizePolicy().hasHeightForWidth())
        self.labelAllTimeScore.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.labelAllTimeScore.setFont(font)
        self.labelAllTimeScore.setObjectName("labelAllTimeScore")
        self.horizontalLayout_3.addWidget(self.labelAllTimeScore)
        self.labelDaysAgo = QtWidgets.QLabel(self.frameCurrent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDaysAgo.sizePolicy().hasHeightForWidth())
        self.labelDaysAgo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.labelDaysAgo.setFont(font)
        self.labelDaysAgo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDaysAgo.setObjectName("labelDaysAgo")
        self.horizontalLayout_3.addWidget(self.labelDaysAgo)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.frameCurrent)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem5)
        self.frameGraphs = QtWidgets.QFrame(statsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameGraphs.sizePolicy().hasHeightForWidth())
        self.frameGraphs.setSizePolicy(sizePolicy)
        self.frameGraphs.setMinimumSize(QtCore.QSize(800, 400))
        self.frameGraphs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGraphs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameGraphs.setObjectName("frameGraphs")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameGraphs)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelGraphTitle = QtWidgets.QLabel(self.frameGraphs)
        self.labelGraphTitle.setStyleSheet("font-weight: bold; font-size: 28pt;")
        self.labelGraphTitle.setObjectName("labelGraphTitle")
        self.verticalLayout_6.addWidget(self.labelGraphTitle)
        self.line_2 = QtWidgets.QFrame(self.frameGraphs)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem6)
        self.graphView = PlotWidget(self.frameGraphs)
        self.graphView.setObjectName("graphView")
        self.verticalLayout_6.addWidget(self.graphView)
        self.verticalLayout_4.addWidget(self.frameGraphs)
        spacerItem7 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem7)
        self.frame = QtWidgets.QFrame(statsWindow)
        self.frame.setMinimumSize(QtCore.QSize(0, 190))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelResetTitle = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResetTitle.sizePolicy().hasHeightForWidth())
        self.labelResetTitle.setSizePolicy(sizePolicy)
        self.labelResetTitle.setStyleSheet("font-weight: bold; font-size: 28pt;")
        self.labelResetTitle.setObjectName("labelResetTitle")
        self.verticalLayout_2.addWidget(self.labelResetTitle)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.buttonResetDaily = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonResetDaily.sizePolicy().hasHeightForWidth())
        self.buttonResetDaily.setSizePolicy(sizePolicy)
        self.buttonResetDaily.setMinimumSize(QtCore.QSize(280, 40))
        self.buttonResetDaily.setObjectName("buttonResetDaily")
        self.horizontalLayout_7.addWidget(self.buttonResetDaily)
        self.buttonResetAllTime = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonResetAllTime.sizePolicy().hasHeightForWidth())
        self.buttonResetAllTime.setSizePolicy(sizePolicy)
        self.buttonResetAllTime.setMinimumSize(QtCore.QSize(280, 40))
        self.buttonResetAllTime.setObjectName("buttonResetAllTime")
        self.horizontalLayout_7.addWidget(self.buttonResetAllTime)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.buttonResetAll = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonResetAll.sizePolicy().hasHeightForWidth())
        self.buttonResetAll.setSizePolicy(sizePolicy)
        self.buttonResetAll.setMinimumSize(QtCore.QSize(240, 40))
        self.buttonResetAll.setObjectName("buttonResetAll")
        self.horizontalLayout_6.addWidget(self.buttonResetAll)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.frame)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.buttonMainMenu = QtWidgets.QPushButton(statsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonMainMenu.sizePolicy().hasHeightForWidth())
        self.buttonMainMenu.setSizePolicy(sizePolicy)
        self.buttonMainMenu.setMinimumSize(QtCore.QSize(150, 40))
        self.buttonMainMenu.setDefault(True)
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        self.horizontalLayout.addWidget(self.buttonMainMenu)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(18, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)

        self.retranslateUi(statsWindow)
        QtCore.QMetaObject.connectSlotsByName(statsWindow)

    def retranslateUi(self, statsWindow):
        _translate = QtCore.QCoreApplication.translate
        statsWindow.setWindowTitle(_translate("statsWindow", "Stats"))
        self.labelCurrentHighscores.setText(_translate("statsWindow", "Current Highscores"))
        self.labelToday.setText(_translate("statsWindow", "Today: "))
        self.labelTodayScore.setText(_translate("statsWindow", "0 WPM"))
        self.labelAllTIme.setText(_translate("statsWindow", "All-time: "))
        self.labelAllTimeScore.setText(_translate("statsWindow", "0 WPM"))
        self.labelDaysAgo.setText(_translate("statsWindow", "-Set 0 days ago"))
        self.labelGraphTitle.setText(_translate("statsWindow", "Graph of Daily Highscores"))
        self.labelResetTitle.setText(_translate("statsWindow", "Reset highscore(s)"))
        self.buttonResetDaily.setText(_translate("statsWindow", "Today\'s"))
        self.buttonResetAllTime.setText(_translate("statsWindow", "All-time and today\'s"))
        self.buttonResetAll.setText(_translate("statsWindow", "All (includes all previous dailies)"))
        self.buttonMainMenu.setText(_translate("statsWindow", "Main Menu"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statsWindow = QtWidgets.QWidget()
    ui = Ui_statsWindow()
    ui.setupUi(statsWindow)
    statsWindow.show()
    sys.exit(app.exec_())
