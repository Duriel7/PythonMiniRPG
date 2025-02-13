import random, math, sys, copy
from database_feed import *

#This file will contain all items lists that will be needed for the game

#General lists
mobList = []
jobList = []
classList = []


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

#Pseudhumanoids
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
undeadList.append(vampireList)
undeadList.append(zombieList)
undeadList.append(ghostList)

            #Individual monsters
#Goblins and Goblinoids

goblinTemplate = {}
goblinTemplate['Type'] = "Goblinoid"
goblinTemplate['Name'] = "Default"
goblinTemplate['Power'] = 0
goblinTemplate['Defense'] = 0
goblinTemplate['Life'] = 1
goblinTemplate['MaxLife'] = 1
goblinTemplate['XP'] = 10
goblinTemplate['CoinFactor'] = 3

goblin = copy.deepcopy(goblinTemplate)
goblin['Name'] = "Goblin"
goblin['Power'] = 12
goblin['Defense'] = 2
goblin['Life'] = 50
goblin['MaxLife'] = 50

print(goblinTemplate, " ", goblin)

        #Pets

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
