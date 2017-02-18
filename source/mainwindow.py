# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 356)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_instructions = QtWidgets.QLabel(self.centralWidget)
        self.lbl_instructions.setWordWrap(True)
        self.lbl_instructions.setObjectName("lbl_instructions")
        self.verticalLayout.addWidget(self.lbl_instructions)
        self.btnReady = QtWidgets.QPushButton(self.centralWidget)
        self.btnReady.setObjectName("btnReady")
        self.verticalLayout.addWidget(self.btnReady)
        self.rune_result = QtWidgets.QLabel(self.centralWidget)
        self.rune_result.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Runes")
        font.setPointSize(150)
        font.setBold(False)
        font.setWeight(50)
        self.rune_result.setFont(font)
        self.rune_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rune_result.setTextFormat(QtCore.Qt.AutoText)
        self.rune_result.setScaledContents(True)
        self.rune_result.setAlignment(QtCore.Qt.AlignCenter)
        self.rune_result.setWordWrap(True)
        self.rune_result.setIndent(1)
        self.rune_result.setObjectName("rune_result")
        self.verticalLayout.addWidget(self.rune_result)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 442, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Runes (v0.01)"))
        self.lbl_instructions.setText(_translate("MainWindow", "Keep the image of what you would like to divine for clear in your mind\'s eye: hold it for as long as you like."))
        self.btnReady.setText(_translate("MainWindow", "Ready"))
        self.rune_result.setToolTip(_translate("MainWindow", "Your divined Rune"))
        self.rune_result.setAccessibleName(_translate("MainWindow", "runefont"))
        self.rune_result.setAccessibleDescription(_translate("MainWindow", "TTF File \'Runes\'"))
        self.rune_result.setText(_translate("MainWindow", "-"))
        self.btnReady.clicked.connect(self.genrune)

    def genrune(self):
        MainWindow.setWindowTitle=("Runes (v0.01): Generating...")
        pause (10)


        #randomly select ascii letter to represent rune


        self.rune_result.setText("x") #Display the rune
         #this will be a randomly generated result, but using letter as placeholder



''' change button to 'Clear' the result if one has already been produced, Ready for another divination '''
''' this is currently broken

        if self.rune_result.text == ("-"):
                self.btnReady.setText("Ready")
        else:
                self.btnReady.setText("Clear")
         
'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

