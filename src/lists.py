import random, math, sys, copy
from database_feed import *

#This file will contain all items lists that will be needed for the game

#################################################################################################
#                                         GENERAL LISTS                                         #
#################################################################################################

speciesList = []
mobList = []
mobSpeciesList = []

jobList = []
classList = []

cityList = []
countryList = []
continentList = []
environmentTypeList = []

originHumanList = []
originHumanDict = {
    'City': cityList,
    'Country': countryList,
    'Continent': continentList
}
originMonsterList = []

mobPlainsList = []
modPlainsFrequencyList = []
mobPlainsDict = {}

mobForestList = []
mobForestFrequencyList = []
mobForestDict = {}

mobCaveList = []
mobCaveFrequencyList = []
mobCaveDict = {}

mobDesertList = []
mobDesertFrequencyList = []
mobDesertDict = {}

mobSnowList = []
mobSnowFrequencyList = []
modSnowDict = {}

mobMountainsList = []
mobMountainsFrequencyList = []
mobMountainsDict = {}

mobRiverList = []
mobRiverFrequencyList = []
mobRiverDict = {}

mobLakeList = []
mobLakeFrequencyList = []
mobLakeDict = {}

mobSeaList = []
mobSeaFrequencyList = []
mobSeaDict = {}

mobSkyList = []
mobSkyFrequencyList = []
mobSkyDict = {}

#Append origin sublists in main lists
originHumanList.append(cityList)
originHumanList.append(countryList)
originHumanList.append(continentList)
originMonsterList.append(environmentTypeList)

originMonsterList.append(continentList)

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

#################################################################################################
#                                       GENERAL TEMPLATES                                       #
#################################################################################################

    #Base global NPC Template
baseNPCTemplate = {}
baseNPCTemplate['LivingState'] = "Living"
baseNPCTemplate['Origin'] = "None"
baseNPCTemplate['Hostility'] = "Neutral"
baseNPCTemplate['Species'] = "Default"
baseNPCTemplate['Type'] = "Default"
baseNPCTemplate['Name'] = "Default"
baseNPCTemplate['Rank'] = 0
baseNPCTemplate['Power'] = 0
baseNPCTemplate['Defense'] = 0
baseNPCTemplate['Life'] = 1
baseNPCTemplate['MaxLife'] = 1
baseNPCTemplate['LifeRegeneration'] = 0
baseNPCTemplate['Stamina'] = 1
baseNPCTemplate['MaxStamina'] = 1
baseNPCTemplate['StaminaRegeneration'] = 2
baseNPCTemplate['Mana'] = 0
baseNPCTemplate['MaxMana'] = 0
baseNPCTemplate['ManaRegeneration'] = 1

    #Characters

        #Human NPC Base Template
baseHumanNPCTemplate = copy.deepcopy(baseNPCTemplate)
baseHumanNPCTemplate['Origin'] = originHumanList[0]
baseNPCTemplate['Hostility'] = "Variable"
baseNPCTemplate['Species'] = "Human"
baseNPCTemplate['Type'] = "HumanRaceVarious"

        #Monster Base Template
baseMonsterTemplate = copy.deepcopy(baseNPCTemplate)
baseMonsterTemplate['Origin'] = originMonsterList[0]
baseMonsterTemplate['Hostility'] = "Hostile"
baseMonsterTemplate['Species'] = "Default"
baseMonsterTemplate['Type'] = "Monster"
baseMonsterTemplate['Rank'] = 1
baseMonsterTemplate['XP'] = 0
baseMonsterTemplate['CoinFactor'] = 0

        #Monsters species

            #Humanoids

            #Pseudo Humanoids

        #Monsters types

            #Humanoids
humanoidTemplate = copy.deepcopy(baseMonsterTemplate)
humanoidTemplate['Species'] = "Humanoid"

            #Pseudo Humanoids
pseudoHumanoidTemplate = copy.deepcopy(baseMonsterTemplate)
pseudoHumanoidTemplate['Species'] = "PseudoHumanoid"

                #Goblinoids
goblinTemplate = copy.deepcopy(pseudoHumanoidTemplate)
goblinTemplate['Type'] = "Goblinoid"
goblinTemplate['ManaRegeneration'] = 0

                #Orcoids
orcTemplate = copy.deepcopy(pseudoHumanoidTemplate)
orcTemplate['Type'] = "Orcoid"
orcTemplate['ManaRegeneration'] = 0

                #Ogre likes
ogreTemplate = copy.deepcopy(pseudoHumanoidTemplate)
ogreTemplate['Type'] = "Orcoid"
ogreTemplate['ManaRegeneration'] = 0

            #Undead
undeadTemplate = copy.deepcopy(baseMonsterTemplate)
undeadTemplate['LivingState'] = "Undead"
undeadTemplate['ManaRegeneration'] = 0

                #Vampires
                #Zombies
                #Ghosts
                #Other undead monsters - can be anything for particular situations

            #Slimy
slimyTemplate = copy.deepcopy(baseMonsterTemplate)
slimyTemplate['Species'] = "Slimy"
slimyTemplate['ManaRegeneration'] = 0

                #Slimes
slimeTemplate = copy.deepcopy(slimyTemplate)
slimeTemplate['Type'] = "Slime"

        #Pets

#################################################################################################
#                                         DEFINITIONS                                           #
#################################################################################################

    #Characters

        #Humans

        #Monsters

            #Humanoids

            #Pseudo Humanoids

                #Goblins

goblin = copy.deepcopy(goblinTemplate)
goblin['Name'] = "Goblin"
goblin['Power'] = 12
goblin['Defense'] = 2
goblin['Life'] = 50
goblin['MaxLife'] = 50
goblin['Stamina'] = 10
goblin['MaxStamina'] = 10
goblin['XP'] = 10
goblin['CoinFactor'] = 3

goblinoidList.append(goblin)
mobList.append(goblin)
mobCaveList.append(goblin)
mobForestList.append(goblin)

hobgoblin = copy.deepcopy(goblinTemplate)
hobgoblin['Name'] = "Hobgoblin"
hobgoblin['Rank'] = 2
hobgoblin['Power'] = 16
hobgoblin['Defense'] = 4
hobgoblin['Life'] = 60
hobgoblin['MaxLife'] = 60
hobgoblin['Stamina'] = 15
hobgoblin['MaxStamina'] = 15
hobgoblin['XP'] = 14
hobgoblin['CoinFactor'] = 5

goblinoidList.append(hobgoblin)
mobList.append(hobgoblin)
mobCaveList.append(hobgoblin)
mobForestList.append(hobgoblin)

                #Orcoids

                #Ogres