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
        MainRunes.setWindowTitle(_translate("MainRunes", "Runes (v0.0.2)"))
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
        #items = (string.ascii_lowercase + string.ascii_uppercase)
        items=("a","b","B","c","d","e","f","F","g","i","j","k","l","L","m","M"
        ,"n","o","O","p","P","r","R","s","t","T","u","U","w","x","y","z","Z")
        rand_item = random.choice(items)
        self.rune_result.setText(rand_item) #Display the rune
        
    
        if rand_item == "a":
            self.lbl_info.setText("Ansuz")
            self.lbl_info.setToolTip("One of the Æsir gods.")
        if rand_item == "b":
            self.lbl_info.setText("Berkana")
            self.lbl_info.setToolTip("Birch.")
        if rand_item == "c":
            self.lbl_info.setText("Kano")
            self.lbl_info.setToolTip("Torch")
        if rand_item == "B":
            self.lbl_info.setText("Kano (Inverted)")
            self.lbl_info.setToolTip("Torch.")
        if rand_item == "d":
            self.lbl_info.setText("Dagaz")
            self.lbl_info.setToolTip("Day.")
        if rand_item == "e":
            self.lbl_info.setText("Eihwaz")
            self.lbl_info.setToolTip("Horse.")
        if rand_item == "E":
            self.lbl_info.setText("Eihwaz (Inverted)")
            self.lbl_info.setToolTip("Horse.")
        if rand_item == "f":
            self.lbl_info.setText("Fehu")
            self.lbl_info.setToolTip("Wealth, cattle.")
        if rand_item == "F":
            self.lbl_info.setText("Fehu (Inverted)")
            self.lbl_info.setToolTip("Wealth, cattle.")

        if rand_item == "g":
            self.lbl_info.setText("Gebo")
            self.lbl_info.setToolTip("Gift.")
        if rand_item == "h":
            self.lbl_info.setText("Hagaz")
            self.lbl_info.setToolTip("Hail (precipitation).")
        if rand_item == "H":
            self.lbl_info.setText("Hagaz (Inverted)")
            self.lbl_info.setToolTip("Hail (precipitation).")
        
        if rand_item == "i":
            self.lbl_info.setText("Isa")
            self.lbl_info.setToolTip("Ice.")
        if rand_item == "j":
            self.lbl_info.setText("Jera")
            self.lbl_info.setToolTip("Year, good year, good harvest.")
        if rand_item == "k":
            self.lbl_info.setText("Kaunan")
            self.lbl_info.setToolTip("Ulcer")
        if rand_item == "l":
            self.lbl_info.setText("Laguz")
            self.lbl_info.setToolTip("Water, lake")
        if rand_item == "L":
            self.lbl_info.setText("Laguz (Inverted)")
            self.lbl_info.setToolTip("Water, lake")
        if rand_item == "m":
            self.lbl_info.setText("Manaz")
            self.lbl_info.setToolTip("Man.")
        if rand_item == "M":
            self.lbl_info.setText("Manaz (Inverted)")
            self.lbl_info.setToolTip("Man.")

        if rand_item == "n":
            self.lbl_info.setText("Nauthiz")
            self.lbl_info.setToolTip("Need.")
        if rand_item == "o":
            self.lbl_info.setText("Othila")
            self.lbl_info.setToolTip("Heritage, estate, possession.")
        if rand_item == "O":
            self.lbl_info.setText("Othila (Inverted)")
            self.lbl_info.setToolTip("Heratige, estate, possession.")
        if rand_item == "p":
            self.lbl_info.setText("Perth")
            self.lbl_info.setToolTip("Meaning unclear: perhaps 'pear tree'")
        if rand_item == "P":
            self.lbl_info.setText("Perth (Inverted)")
            self.lbl_info.setToolTip("Meaning unclear: perhaps 'pear tree'")
        if rand_item == "r":
            self.lbl_info.setText("Raido")
            self.lbl_info.setToolTip("Ride, journey.")
        if rand_item == "R":
            self.lbl_info.setText("Raido (Inverted)")
            self.lbl_info.setToolTip("Ride, journey.")
        if rand_item == "s":
            self.lbl_info.setText("Sowelu")
            self.lbl_info.setToolTip("Sun")
        if rand_item == "t":
            self.lbl_info.setText("Teiwaz")
            self.lbl_info.setToolTip("The god, Teiwaz")
        if rand_item == "T":
            self.lbl_info.setText("Teiwaz (Inverted)")
            self.lbl_info.setToolTip("The god, Teiwaz.")
        if rand_item == "u":
            self.lbl_info.setText("Uruz")
            self.lbl_info.setToolTip("Water, slag.")
        if rand_item == "U":
            self.lbl_info.setText("Uruz (Inverted)")
            self.lbl_info.setToolTip("Water, slag.")
        #if rand_item == "v":
        #    self.lbl_info.setText("Teiwaz (Inverted)")
        # self.lbl_info.setToolTip("One of the Æsir gods.")
        if rand_item == "w":
            self.lbl_info.setText("Wunjo")
            self.lbl_info.setToolTip("Joy.")
        if rand_item == "y":
            self.lbl_info.setText("Jera")
            self.lbl_info.setToolTip("Year, good year, harvest..")
        if rand_item == "z":
            self.lbl_info.setText("Algiz")
            self.lbl_info.setToolTip("Meaning unclear: possibly 'elk'.")
        if rand_item == "Z":
            self.lbl_info.setText("Algiz (Inverted)")
            self.lbl_info.setToolTip("Meaning unclear: possibly 'elk'.")
        

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

