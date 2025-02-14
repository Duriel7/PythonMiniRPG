import random, math, sys, copy
from database_feed import *

#This file will contain all items lists that will be needed for the game

#General lists
speciesList = []
mobList = []
mobSpeciesList = []
jobList = []
classList = []
originHumanList = []
originMonsterList = []
cityList = []
countryList = []
continentList = []
environmentTypeList = []

#Append origin sublists in main lists
originHumanList.append(cityList)
originHumanList.append(countryList)
originHumanList.append(continentList)
originMonsterList.append(environmentTypeList)

    #Characters

        #NPC human
humanList = []

        #Monsters
            #Species and Races
            #Humanoids
humanoidList = []
corruptedHumanList = []
corruptedElfList = []
corruptedDwarfList = []
#Append in humanoids list
humanoidList.append(corruptedHumanList)
humanoidList.append(corruptedElfList)
humanoidList.append(corruptedDwarfList)

            #Pseudohumanoids
pseudoHumanoidList = []
goblinoidList = []
orcoidList = []
ogreList = []
#Append in pseudohumanoids list
pseudoHumanoidList.append(goblinoidList)
pseudoHumanoidList.append(orcoidList)
pseudoHumanoidList.append(ogreList)

            #Undead
undeadList = []
vampireList = []
zombieList = []
ghostList = []
#Append in undead list
humanoidList.append(undeadList)
undeadList.append(vampireList)
undeadList.append(zombieList)
undeadList.append(ghostList)

            #Demons
#Append in demons list

            #Slimy
slimyList = []
slimelist = []
mudList = []
gelList = []
#Append in slimy list
slimyList.append(slimelist)
slimyList.append(mudList)
slimyList.append(gelList)

    #Inhabited places hardcoded

        #Villages

        #Main cities

    #Dungeons

        #Subterranean

        #Overworld

        #Air placed

        #Other dimensions

    #Items

        #General items
itemList = []

        #General categories
aidList = []
weaponList = []
armorList = []

        #Precise categories

            #Weapons
swordList = []
axeList = []
spearList = []
polearmList = []
bowList = []
crossbowList = []


            #Armors

            #Potions

#General Templates

    #Base global NPC Template
baseNPCTemplate = {}
baseNPCTemplate['Hostility'] = "Neutral"
baseNPCTemplate['Species'] = "Default"
baseNPCTemplate['Type'] = "Default"
baseNPCTemplate['Name'] = "Default"
baseNPCTemplate['Rank'] = 0
baseNPCTemplate['Power'] = 0
baseNPCTemplate['Defense'] = 0
baseNPCTemplate['Life'] = 1
baseNPCTemplate['MaxLife'] = 1

    #Characters

        #Human NPC Template
baseHumanNPCTemplate = {}
baseHumanNPCTemplate[''] = 0

        #Monster Template
baseMonsterTemplate = copy.deepcopy(baseNPCTemplate)
baseMonsterTemplate['Hostility'] = "Hostile"
baseMonsterTemplate['Species'] = "Default"
baseMonsterTemplate['Type'] = "Monster"
baseMonsterTemplate['Name'] = "Default"
baseMonsterTemplate['Rank'] = 1
baseMonsterTemplate['Power'] = 0
baseMonsterTemplate['Defense'] = 0
baseMonsterTemplate['Life'] = 1
baseMonsterTemplate['MaxLife'] = 1
baseMonsterTemplate['XP'] = 0
baseMonsterTemplate['CoinFactor'] = 0

        #Monsters species

            #Humanoids

            #Pseudo Humanoids

        #Monsters types

            #Humanoids

            #Pseudo Humanoids

                #Goblins and Goblinoids

goblinTemplate = copy.deepcopy(baseMonsterTemplate)
goblinTemplate['Species'] = "PseudoHumanoid"
goblinTemplate['Type'] = "Goblinoid"
goblinTemplate['Name'] = "Default"
goblinTemplate['XP'] = 10
goblinTemplate['CoinFactor'] = 3

goblin = copy.deepcopy(goblinTemplate)
goblin['Name'] = "Goblin"
goblin['Power'] = 12
goblin['Defense'] = 2
goblin['Life'] = 50
goblin['MaxLife'] = 50

goblinoidList.append(goblin)
mobList.append(goblin)

hobgoblin = copy.deepcopy(goblinTemplate)
hobgoblin['Name'] = "Hobgoblin"
hobgoblin['Rank'] = 2
hobgoblin['Power'] = 16
hobgoblin['Defense'] = 4
hobgoblin['Life'] = 60
hobgoblin['MaxLife'] = 60
hobgoblin['XP'] = 14
hobgoblin['CoinFactor'] = 5

goblinoidList.append(hobgoblin)
mobList.append(hobgoblin)

print("base NPC : ", baseNPCTemplate)
print("base monster : ", baseMonsterTemplate)
print("goblin template : ", goblinTemplate)
print("goblin : ", goblin)
print("hob : ", hobgoblin)

#Undead

        #Pets

#Definitions

    #Characters