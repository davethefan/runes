# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainRunes.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string

class Ui_Runes(object):
    def setupUi(self, MainRunes):
        MainRunes.setObjectName("MainRunes")
        MainRunes.resize(442, 374)
        self.centralWidget = QtWidgets.QWidget(MainRunes)
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
        self.lbl_info = QtWidgets.QLabel(self.centralWidget)
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setObjectName("lbl_info")
        self.verticalLayout.addWidget(self.rune_result)
        self.verticalLayout.addWidget(self.lbl_info)
        MainRunes.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainRunes)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 442, 22))
        self.menuBar.setObjectName("menuBar")
        MainRunes.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainRunes)
        self.mainToolBar.setObjectName("mainToolBar")
        MainRunes.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainRunes)
        self.statusBar.setObjectName("statusBar")
        MainRunes.setStatusBar(self.statusBar)

        self.retranslateUi(MainRunes)
        QtCore.QMetaObject.connectSlotsByName(MainRunes)

    def retranslateUi(self, MainRunes):
        _translate = QtCore.QCoreApplication.translate
        MainRunes.setWindowTitle(_translate("MainRunes", "Runes (v0.01)"))
        self.lbl_instructions.setText(_translate("MainRunes", "Close your eyes, and ask your question into your mind's eye. "))
        self.btnReady.setText(_translate("MainRunes", "Ready"))
        self.rune_result.setToolTip(_translate("MainRunes", "Your divined Rune"))
        self.rune_result.setAccessibleName(_translate("MainRunes", "runefont"))
        self.rune_result.setAccessibleDescription(_translate("MainRunes", "TTF File \'Runes\'"))
        self.rune_result.setText(_translate("MainRunes", "-"))
        self.btnReady.clicked.connect(self.genrune)
        self.lbl_info.setText(_translate("MainWindow", "[name]"))


    def genrune(self):
        #randomly select ascii letter to represent rune
        items = (string.ascii_lowercase + string.ascii_uppercase)
        rand_item = random.choice(items)
        self.rune_result.setText(rand_item) #Display the rune
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
    MainRunes = QtWidgets.QMainWindow()
    ui = Ui_Runes()
    ui.setupUi(MainRunes)
    MainRunes.show()
    sys.exit(app.exec_())

