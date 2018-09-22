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
        CR=random.randint(1, 9)
        if CR==1:
            CR="Dwarf"
            RT=["CON +2", "Size: Medium", "Speed: 25", "Darkvision: 60", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning"]
        elif CR==2:
            CR="Dragonborn"
            RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30"]
        elif CR==3:
            CR="Elf"
            RT=["DEX: +2", "Size: Medium", "Speed: 30", "Darkvision: 60", "Keen Senses", "Fey Ancestry", "Trance"]
        elif CR==4:
            CR="Gnome"
            RT=["INT; +2", "Size: Small", "Speed: 25", "Darkvision: 60"]
        elif CR==5:
            CR="Half-Elf"
            RT=["CHA: +2", "X: +1", "Size: Medium", "Speed: 30", "Darkvision: 60","Fey Ancestry", "Skill Versatilities"]
        elif CR==6:
            CR="Half-Orc"
            RT=["STR: +2", "CON: +1", "Size: Medium", "Speed: 30", "Darkvision: 60", "Menacing", "Relentless Endurance", "Savage Attacks"]
        elif CR==7:
            CR="Halfling"
            RT=["DEX: +2", "Size: Small", "Speed: 25", "Lucky", "Brave", "Halfling Nimbleness"]
        elif CR==8:
            CR="Human"
            RT=["All: +1", "Size: Medium", "Speed: 30"]
        elif CR==9:
            CR="Tiefling"
            RT=["CHA: +2", "INT: +1", "Nessian Legacy"]
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
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Acid", "Damage Resistance: Acid"]
            elif SR==2:
                SR="Blue"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Lightning", "Damage Resistance: Lightning"]
            elif SR==3:
                SR="Brass"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Fire", "Damage Resistance: Fire"]
            elif SR==4:
                SR="Bronze"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Lightning", "Damage Resistance: Lightning"]
            elif SR==5:
                SR="Copper"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Acid", "Damage Resistance: Acid"]
            elif SR==6:
                SR="Gold"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Fire", "Damage Resistance: Fire"]
            elif SR==7:
                SR="Green"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Acid", "Damage Resistance: Poison"]
            elif SR==8:
                SR="Red"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Fire", "Damage Resistance: Fire"]
            elif SR==9:
                SR="Silver"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Cold", "Damage Resistance: Cold"]
            elif SR==10:
                SR="White"
                RT=["STR: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Breath Weapon: Cold", "Damage Resistance: Cold"]
        elif self.CharacterRace.item(0).text()=="Elf":
            SR=random.randint(1, 3)
            if SR==1:
                SR="Dark"
                RT=["DEX: +2", "CHA: +1", "Size: Medium", "Speed: 30", "Darkvision: 120", "Sunlight Sensitivity", "Drow Magic", "Drow Weapon Training", "Keen Senses", "Fey Ancestry", "Trance"]
            elif SR==2:
                SR="High"
                RT=["DEX: +2", "INT: +1", "Size: Medium", "Speed: 30", "Darkvision: 60", "Elf Weapon Training", "Cantrip", "Extra Language", "Keen Senses", "Fey Ancestry", "Trance"]
            elif SR==3:
                SR="Wood"
                RT=["DEX: +2", "WIS: +1", "Size: Medium", "Speed: 35", "Darkvision: 60", "Mask of the Wild", "Keen Senses", "Fey Ancestry", "Trance"]
        elif self.CharacterRace.item(0).text()=="Gnome":
            SR=random.randint(1, 2)
            if SR==1:
                SR="Forest"
                RT=["INT; +2", "DEX: +1", "Size: Small", "Speed: 25", "Darkvision: 60", "Natural Illusionist", "Speak with Small Beasts"]
            elif SR==2:
                SR="Rock"
                RT=["INT; +2", "CON: +1" "Size: Small" "Speed: 25", "Darkvision: 60", "Artificer's Lore", "Tinkerer"]
        elif self.CharacterRace.item(0).text()=="Halfling":
            SR=random.randint(1, 2)
            if SR==1:
                SR="Lightfoot"
                RT=["DEX: +2", "CHA: +1", "Size: Small", "Speed: 25", "Lucky", "Brave", "Halfling Nimbleness", "Naturally Stealthy"]
            elif SR==2:
                SR="Stout"
                RT=["DEX: +2", "CON: +1", "Size: Small", "Speed: 25", "Lucky", "Brave", "Halfling Nimbleness", "Stout Resilience"]
        elif self.CharacterRace.item(0).text()=="Half-Elf":
            SR="N/A"
            RT=["CHA: +2", "X: +1", "Size: Medium", "Speed: 30", "Darkvision: 60", "Fey Ancestry", "Skill Versatilities"]
        elif self.CharacterRace.item(0).text()=="Half-Orc":
            SR="N/A"
            RT=["STR: +2", "CON: +1", "Size: Medium", "Speed: 30", "Darkvision: 60", "Menacing", "Relentless Endurance", "Savage Attacks"]
        elif self.CharacterRace.item(0).text()=="Human":
            SR="N/A"
            RT=["All: +1", "Size: Medium", "Speed: 30"]
        elif self.CharacterRace.item(0).text()=="Tiefling":
            SR="N/A"
            RT=["CHA: +2", "INT: +1", "Nessian Legacy"]

        self.CharacterSubrace.clear()
        self.CharacterSubrace.addItem(SR)
        self.RaceTraits.clear()
        for x in RT:
            self.RaceTraits.addItem(x)

    def ClassGen(self):
        CC=random.randint(1, 12)
        if CC==1:
            CC="Barbarian"
            CT=["Hit Die: d12", "", "Proficiencies:", "Armour: Light, Medium, Shields", "Weapons: Simple, Martial", "Tools: None", "Saving Throws: STR, CON", "", "Traits:", "Rage", "Unarmoured Defense", "Reckless Attack", "Danger Sense", "Ability Score Imporvement", "Extra Attack", "Fast Movement", "Feral Instinct", "Brutal Critical", "Relentless Rage", "Persistent Rage", "Indomitable Might", "Primal Champion"]
        elif CC==2:
            CC="Bard"
            CT=["Hit Die: d8", "", "Proficiencies:", "Armour: Light", "Weapons: Simple, Hand Crossbows, Longswords, Rapiers, Shortswords", "Tools: 3 musical instruments", "Saving Throws: DEX, CHA", "", "Traits:", "Bardic Inspiration", "Jack of All Trades", "Song of Rest", "Expertise", "font of Inspiration", "Countercharm", "Magical Secrets", "Superior Inspiration"]
        elif CC==3:
            CC="Cleric"
            CT=["Hit Die: d8", "", "Proficiences:", "Armour: Light, Medium, Shields", "Weapons: Simple", "Tools: None", "Saving Throws: WIS, CHA", "Channel Divinity: Turn Undead", "", "Traits:", "Destroy Undead", "Divine Intervention"]
        elif CC==4:
            CC="Druid"
            CT=["Hit Die: d8", "", "Proficiences:", "Armour (non-metal): Light, Medium, Shields", "Weapons: Clubs, Daggers, Darts, Javelins, Maces, Quarterstaffs, Scimitars, Sickles, Slings, Spears", "Tools: Herbalism Kit", "Saving Throws: INT, WIS", "", "Traits:", "Wild Shape", "Timeless Body", "Beast Spells", "Archdruid"]
        elif CC==5:
            CC="Fighter"
            CT=["Hit Die: d10", "", "Proficiences:", "Armour: All, Sheilds" "Weapons: Simple, Martial", "Tools: None", "Saving Throws: STR, CON", "", "Traits:", "Fighting Style", "Second Wind", "Action Surge", "Martial Archtype", "Extra Attack", "Indomitable"]
        elif CC==6:
            CC="Monk"
            CT=["Hit Die: d8", "", "Proficiences:", "Armour: None", "Weapons: Simple, Shortswords", "Tools: 1 Artisan tool or 1 musical instrument", "Saving Throws: STR, DEX", "", "Traits:", "Unarmoured Defense", "Martial ARts", "Ki", "Uarmoured Movement", "Deflect Missiles", "Slow Fall", "Extra Attack", "Stunning Strike", "Ki-Empowered Strikes", "Evasion", "Stillness of Mind", "Purity of Body", "Tongue of the Sun and Moon", "Diamond Soul", "Timeless Body", "Empty Body", "Perfect Self"]
        elif CC==7:
            CC="Paladin"
            CT=["Hit Die: d10", "", "Proficiences:", "Armour: All, shields", "Weapons: Simple, Martial", "Tools: None", "Saving Throws: WIS, CHA", "", "Traits:", "Divine Sense", "Lay on Hands", "Fighting Style", "Divine Smite", "Divine health", "Sacred Oath", "Extra Attack", "Aura of Protection", "Aura of Courage", "Improved Divine Smite", "Cleansing Touch"]
        elif CC==8:
            CC="Ranger"
            CT=["Hit Die: d8", "", "Proficiences:", "Armour: Light, Medium, Shields", "Weapons: Simple, Martial", "Tools: None", "Saving Throws: STR, DEX", "", "Traits:", "Favoured Enemy", "Natural Explorer", "Fighting Style", "Primeval Awareness", "Extra Attack", "Land's Stride", "Hide in Play Sight", "Vanish", "Feral Senses", "Foe Slyaer"]
        elif CC==9:
            CC="Rogue"
            CT=["Hit Die: d8", "", "Proficiences:", "Armour: Light", "Weapons: Simple, Hand Crossbows, Longswords, Rapiers, Shortswords", "Tools: Thieves' tools", "Saving Throws: DEX, INT", "", "Traits:", "Expertise", "Sneak Attack", "Theives' Cant", "Cunning Action", "Uncanny Dodge", "Evasion", "Reliable Talent", "Blindsense", "Slippery Mind", "Elusive", "Stroke of Luck"]
        elif CC==10:
            CC="Sorcerer"
            CT=["Hit Die: d6", "", "Proficiences:", "Armour: None", "Weapons: Daggers, Dats, Slings, Quarterstaffs, Light Crossbows", "Tools: None", "Saving Throws: CON, CHA", "", "Traits:", "Font of Magic", "Metamagic", "Sorcerous Restoration"]
        elif CC==11:
            CC="Warlock"
            CT=["Hit Die: d8", "", "Proficiences:", "Armour: Light", "Weapons: Simple", "Tools: None", "Saving Throws: WIS, CHA", "", "Traits:", "Pact Boon", "Mystic Arcanum", "Edritch Master"]
        elif CC==12:
            CC="Wizard"
            CT=["Hit Die: d6", "", "Proficiences:", "Armour: None", "Weapons: Daggers, Darts, Slings, Quarterstaffs, Light Crossbows", "Tools: None", "Saving Throws: INT, WIS", "", "Traits: Arcane Recovery", "Spell Master", "Signature Spells"]
        self.CharacterClass.clear()
        self.CharacterClass.addItem(CC)
        self.CharacterSubclass.clear()
        self.ClassTraits.clear()
        for x in CT:
            self.ClassTraits.addItem(x)

    def SubCGen(self):
        if self.CharacterClass.item(0).text()=="Barbarian":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Berserker"
                CT=["Hit Die: d12", "", "Proficiencies:", "Armour: Light, Medium, Shields", "Weapons: Simple, Martial", "Tools: None", "Saving Throws: STR, CON", "", "Traits:", "Rage", "Unarmoured Defense", "Reckless Attack", "Danger Sense", "Ability Score Imporvement", "Extra Attack", "Fast Movement", "Feral Instinct", "Brutal Critical", "Relentless Rage", "Persistent Rage", "Indomitable Might", "Primal Champion"]
            elif SC==2:
                SC="Totem Warrior"
                CT=["Hit Die: d12", "", "Proficiencies:", "Armour: Light, Medium, Shields", "Weapons: Simple, Martial", "Tools: None", "Saving Throws: STR, CON", "", "Traits:", "Rage", "Unarmoured Defense", "Reckless Attack", "Danger Sense", "Ability Score Imporvement", "Extra Attack", "Fast Movement", "Feral Instinct", "Brutal Critical", "Relentless Rage", "Persistent Rage", "Indomitable Might", "Primal Champion"]
        if self.CharacterClass.item(0).text()=="Bard":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Lore"
                CT=[""]
            elif SC==2:
                SC="Valour"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Cleric":
            SC=random.randint(1, 7)
            if SC==1:
                SC="Knowledge"
                CT=[""]
            elif SC==2:
                SC="Life"
                CT=[""]
            elif SC==3:
                SC="Light"
                CT=[""]
            elif SC==4:
                SC="Nature"
                CT=[""]
            elif SC==5:
                SC="Tempest"
                CT=[""]
            elif SC==6:
                SC="Trickery"
                CT=[""]
            elif SC==7:
                SC="War"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Druid":
            SC=random.randint(1, 2)
            if SC==1:
                L=random.randint(1, 8)
                if L==1:
                    SC="Arctic"
                    CT=[""]
                elif L==2:
                    SC=="Coast"
                    CT=[""]
                elif L==3:
                    SC=="Desert"
                    CT=[""]
                elif L==4:
                    SC=="Forest"
                    CT=[""]
                elif L==5:
                    SC=="Grassland"
                    CT=[""]
                elif L==6:
                    SC="Mountain"
                    CT=[""]
                elif L==7:
                    SC="Swamp"
                    CT=[""]
                elif L==8:
                    SC=="Underdark"
                    CT=[""]
            elif SC==2:
                SC="Moon"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Fighter":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Battle Master"
                CT=[""]
            elif SC==2:
                SC="Champion"
                CT=[""]
            elif SC==3:
                SC="Eldritch Knight"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Monk":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Four Elements"
                CT=[""]
            elif SC==2:
                SC="Open Hand"
                CT=[""]
            elif SC==3:
                SC="Shadow"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Paladin":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Ancients"
                CT=[""]
            elif SC==2:
                SC="Devotion"
                CT=[""]
            elif SC==3:
                SC="Vengeance"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Ranger":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Beast Master"
                CT=[""]
            elif SC==2:
                SC="Hunter"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Rogue":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Arcane Trickster"
                CT=[""]
            elif SC==2:
                SC="Assassin"
                CT=[""]
            elif SC==3:
                SC="Thief"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Sorcerer":
            SC=random.randint(1, 2)
            if SC==1:
                SC="Draconic Bloodline"
                CT=[""]
            elif SC==2:
                SC="Wild Magic"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Warlock":
            SC=random.randint(1, 3)
            if SC==1:
                SC="Archfey"
                CT=[""]
            elif SC==2:
                SC="Fiend"
                CT=[""]
            elif SC==3:
                SC="Great Old One"
                CT=[""]
        if self.CharacterClass.item(0).text()=="Wizard":
            SC=random.randint(1, 8)
            if SC==1:
                SC="Abjuration"
                CT=[""]
            elif SC==2:
                SC="Conjuration"
                CT=[""]
            elif SC==3:
                SC="Divination"
                CT=[""]
            elif SC==4:
                SC="Enchantment"
                CT=[""]
            elif SC==5:
                SC="Evocation"
                CT=[""]
            elif SC==6:
                SC="Illusion"
                CT=[""]
            elif SC==7:
                SC="Necromancy"
                CT=[""]
            elif SC==8:
                SC="Transmutation"
                CT=[""]
        self.CharacterSubclass.clear()
        self.CharacterSubclass.addItem(SC)
        self.ClassTraits.clear()
        for x in CT:
            self.ClassTraits.addItem(x)

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
