# To run this file PyQt5 must be installed.
import random
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 650)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.CharacterRace  = QtWidgets.QListWidget(self.centralwidget)
        self.CharacterRace.setGeometry(QtCore.QRect(10, 10, 125, 25))
        self.CharacterRace.setObjectName("CharacterRace")

        self.GenerateRace = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateRace.setGeometry(QtCore.QRect(10, 45, 125, 25))
        self.GenerateRace.setObjectName("GenerateRace")

        self.CharacterClass = QtWidgets.QListWidget(self.centralwidget)
        self.CharacterClass.setGeometry(QtCore.QRect(145, 10, 125, 25))
        self.CharacterClass.setObjectName("CharacterClass")

        self.GenerateClass = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateClass.setGeometry(QtCore.QRect(145, 45, 125, 25))
        self.GenerateClass.setObjectName("GenerateClass")

        self.CharacterSubrace = QtWidgets.QListWidget(self.centralwidget)
        self.CharacterSubrace.setGeometry(QtCore.QRect(280, 10, 125, 25))
        self.CharacterSubrace.setObjectName("CharacterSubrace")

        self.GenerateSubrace = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateSubrace.setGeometry(QtCore.QRect(280, 45, 125, 25))
        self.GenerateSubrace.setObjectName("GenerateSubrace")

        self.CharacterSubclass = QtWidgets.QListWidget(self.centralwidget)
        self.CharacterSubclass.setGeometry(QtCore.QRect(415, 10, 125, 25))
        self.CharacterSubclass.setObjectName("CharacterSubclass")

        self.GenerateSubclass = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateSubclass.setGeometry(QtCore.QRect(415, 45, 125, 25))
        self.GenerateSubclass.setObjectName("GenerateSubclass")

        self.GenerateCharacter = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateCharacter.setGeometry(QtCore.QRect(10, 80, 530, 25))
        self.GenerateCharacter.setObjectName("GenerateCharacter")

        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(10, 115, 530, 25))
        self.Clear.setObjectName("Clear")

        self.RaceTraits = QtWidgets.QListWidget(self.centralwidget)
        self.RaceTraits.setGeometry(QtCore.QRect(10, 150, 260, 490))
        self.RaceTraits.setObjectName("RaceTraits")

        self.ClassTraits = QtWidgets.QListWidget(self.centralwidget)
        self.ClassTraits.setGeometry(QtCore.QRect(280, 150, 260, 490))
        self.ClassTraits.setObjectName("ClassTraits")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.GenerateRace.clicked.connect(self.RaceGen)
        self.GenerateClass.clicked.connect(self.ClassGen)
        self.GenerateSubrace.clicked.connect(self.SubRGen)
        self.GenerateSubclass.clicked.connect(self.SubCGen)
        self.GenerateCharacter.clicked.connect(self.RaceGen)
        self.GenerateCharacter.clicked.connect(self.ClassGen)
        self.GenerateCharacter.clicked.connect(self.SubRGen)
        self.GenerateCharacter.clicked.connect(self.SubCGen)
        self.Clear.clicked.connect(self.FClear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "D&D Character Generater"))
        self.GenerateRace.setText(_translate("MainWindow", "Generate Race"))
        self.GenerateClass.setText(_translate("MainWindow", "Generate Class"))
        self.GenerateSubrace.setText(_translate("MainWindow", "Generate Subrace"))
        self.GenerateSubclass.setText(_translate("MainWindow", "Generate Subclass"))
        self.GenerateCharacter.setText(_translate("MainWindow", "Generate Character"))
        self.Clear.setText(_translate("MainWindow", "Clear"))

    def RaceGen(self):
        CR=random.randint(1, 1)
        if CR==1:
            CR="Dwarf"
            RT=["CON +2", "Size: Medium", "Speed: 25", "Darkvision: 60", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning"]
        elif CR==2:
            CR="Dragonborn"
        elif CR==3:
            CR="Elf"
        elif CR==4:
            CR="Gnome"
        elif CR==5:
            CR="Half-Elf"
        elif CR==6:
            CR="Half-Orc"
        elif CR==7:
            CR="Halfling"
        elif CR==8:
            CR="Human"
        elif CR==9:
            CR="Tiefling"
        self.CharacterRace.clear()
        self.CharacterSubrace.clear()
        self.CharacterRace.addItem(CR)
        self.RaceTraits.clear()
        for x in RT:
            self.RaceTraits.addItem(x)

    def SubRGen(self):
        if self.CharacterRace.item(0).text()=="Dwarf":
            SR=random.randint(1, 2)
            if SR==1:
                SR="Hill"
                RT=["CON +2", "WIS: +1", "Size: Medium", "Speed: 25", "Darkvision: 60", "Dwarven Combat Training", "Dwarven Toughness", "Tool Proficiency", "Stonecunning"]
            elif SR==2:
                SR="Mountain"
                RT=["CON +2", "STR: +1", "Size: Medium", "Speed: 25", "Darkvision: 60", "Dwarven Combat Training", "Dwarven Armour Training", "Tool Proficiency", "Stonecunning"]
        elif self.CharacterRace.item(0).text()=="Dragonborn":
            SR=random.randint(1, 10)
            if SR==1:
                SR="Black"
            elif SR==2:
                SR="Blue"
            elif SR==3:
                SR="Brass"
            elif SR==4:
                SR="Bronze"
            elif SR==5:
                SR="Copper"
            elif SR==6:
                SR="Gold"
            elif SR==7:
                SR="Green"
            elif SR==8:
                SR="Red"
            elif SR==9:
                SR="Silver"
            elif SR==10:
                SR="White"
        elif self.CharacterRace.item(0).text()=="Elf":
            SR=random.randint(1, 3)
            if SR==1:
                SR="Dark"
            elif SR==2:
                SR="High"
            elif SR==3:
                SR="Wood"
        elif self.CharacterRace.item(0).text()=="Gnome":
            SR=random.randint(1, 2)
            if SR==1:
                SR="Forest"
            elif SR==2:
                SR="Rock"
        elif self.CharacterRace.item(0).text()=="Halfling":
            SR=random.randint(1, 2)
            if SR==1:
                SR="Lightfoot"
            elif SR==2:
                SR="Stout"
        else:
            SR="N/A"

        self.CharacterSubrace.clear()
        self.CharacterSubrace.addItem(SR)
        self.RaceTraits.clear()
        for x in RT:
            self.RaceTraits.addItem(x)

    def ClassGen(self):
        CC=random.randint(1, 12)
        if CC==1:
            CC="Barbarian"
        elif CC==2:
            CC="Bard"
        elif CC==3:
            CC="Cleric"
        elif CC==4:
            CC="Druid"
        elif CC==5:
            CC="Fighter"
        elif CC==6:
            CC="Monk"
        elif CC==7:
            CC="Paladin"
        elif CC==8:
            CC="Ranger"
        elif CC==9:
            CC="Rogue"
        elif CC==10:
            CC="Sorcerer"
        elif CC==11:
            CC="Warlock"
        elif CC==12:
            CC="Wizard"
        self.CharacterClass.clear()
        self.CharacterClass.addItem(CC)

    def SubCGen(self):
        if self.CharacterClass.item(0).text()=="Barbarian":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Berserker"
            elif SC==2:
                SC="Totem Warrior"
        if self.CharacterClass.item(0).text()=="Bard":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Lore"
            elif SC==2:
                SC="Valour"
        if self.CharacterClass.item(0).text()=="Cleric":
            SC=random.randint(1, 7)
            if SC==1:
                SC="Knowledge"
            elif SC==2:
                SC="Life"
            elif SC==3:
                SC="Light"
            elif SC==4:
                SC="Nature"
            elif SC==5:
                SC="Tempest"
            elif SC==6:
                SC="Trickery"
            elif SC==7:
                SC="War"
        if self.CharacterClass.item(0).text()=="Druid":
            SC=random.randint(1, 2)
            if SC==1:
                L=random.randint(1, 8)
                if L==1:
                    SC="Arctic"
                elif L==2:
                    SC=="Coast"
                elif L==3:
                    SC=="Desert"
                elif L==4:
                    SC=="Forest"
                elif L==5:
                    SC=="Grassland"
                elif L==6:
                    SC="Mountain"
                elif L==7:
                    SC="Swamp"
                elif L==8:
                    SC=="Underdark"
            elif SC==2:
                SC="Moon"
        if self.CharacterClass.item(0).text()=="Fighter":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Battle Master"
            elif SC==2:
                SC="Champion"
            elif SC==3:
                SC="Eldritch Knight"
        if self.CharacterClass.item(0).text()=="Monk":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Four Elements"
            elif SC==2:
                SC="Open Hand"
            elif SC==3:
                SC="Shadow"
        if self.CharacterClass.item(0).text()=="Paladin":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Ancients"
            elif SC==2:
                SC="Devotion"
            elif SC==3:
                SC="Vengeance"
        if self.CharacterClass.item(0).text()=="Ranger":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Beast Master"
            elif SC==2:
                SC="Hunter"
        if self.CharacterClass.item(0).text()=="Rogue":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Arcane Trickster"
            elif SC==2:
                SC="Assassin"
            elif SC==3:
                SC="Thief"
        if self.CharacterClass.item(0).text()=="Sorcerer":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Draconic"
            elif SC==2:
                SC="Wild Magic"
        if self.CharacterClass.item(0).text()=="Warlock":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Archfey"
            elif SC==2:
                SC="Fiend"
            elif SC==3:
                SC="Great Old One"
        if self.CharacterClass.item(0).text()=="Wizard":
            SC=random.randint(1, 8)
            if SC==1:
                SC="Abjuration"
            elif SC==2:
                SC="Conjuration"
            elif SC==3:
                SC="Divination"
            elif SC==4:
                SC="Enchantment"
            elif SC==5:
                SC="Evocation"
            elif SC==6:
                SC="Illusion"
            elif SC==7:
                SC="Necromancy"
            elif SC==8:
                SC="Transmutation"
        self.CharacterSubclass.clear()
        self.CharacterSubclass.addItem(SC)

    def FClear(self):
        self.CharacterRace.clear()
        self.CharacterClass.clear()
        self.CharacterSubrace.clear()
        self.CharacterSubclass.clear()
        self.RaceTraits.clear()
        self.ClassTraits.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
