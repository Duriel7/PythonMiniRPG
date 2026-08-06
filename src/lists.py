import random, copy
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

continentNamesList = []
countryNamesList = []
allCitiesNamesList = []
majorCitiesNamesList = []
cityNamesList = []
villageNamesList = []

continentList = []
countryList = []
allCitiesList = []
majorCitiesList = []
cityList = []
villageList = []

environmentTypeList = []

#Assigning major cities to their country
cityDict = {}
#for of loop

#Assigning countries to their continent
countryDict = {}
#for of loop

originHumanList = []
originMonsterList = []

mobPlainsList = []
modPlainsFrequencyList = []
mobPlainsDict = {}

mobSavannaList = []
modSavannaFrequencyList = []
mobSavannaDict = {}

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

#Append origin sublists in main lists and dictionaries
originHumanList.append(allCitiesList)
originHumanList.append(countryList)
originHumanList.append(continentList)
originMonsterList.append(environmentTypeList)

allCitiesList.append(majorCitiesList)
allCitiesList.append(cityList)
allCitiesList.append(villageNamesList)

originMonsterList.append(continentList)

originHumanDict = {
    'City': cityList[0],
    'Country': countryList[0],
    'Continent': continentList[0]
}

#Idea for the corresponding country and continent for each preceding entity
#make major cities correspond to a country, each country to a continent, then
#make the random choice catch the corresponding value and pass it to the dictionary

originHumanRandomDict = { #make it so the country is corresponding
    'City': random.choice(allCitiesList),
    'Country': random.choice(countryList),
    'Continent': random.choice(continentList)
}

    #Characters

        #NPC human - major defined NPC only
humanList = []

        #Monsters
            #Species and Races

            #Humanoids
humanoidList = []
corruptedHumanList = []
corruptedElfList = []
corruptedDwarfList = []
beastMenList = []
homonculiiList = []
#Append in humanoids list
humanoidList.append(corruptedHumanList)
humanoidList.append(corruptedElfList)
humanoidList.append(corruptedDwarfList)
humanoidList.append(beastMenList)
humanoidList.append(homonculiiList)

            #Pseudohumanoids
pseudoHumanoidList = []
goblinoidList = []
orcoidList = []
ogreList = []
#Append in pseudohumanoids list
pseudoHumanoidList.append(goblinoidList)
pseudoHumanoidList.append(orcoidList)
pseudoHumanoidList.append(ogreList)

            #Undead - Humanoid
undeadHumanoidList = []
vampireList = []
zombieList = []
skeletonList = []
ghostList = []
#Append in humanoid undead list
humanoidList.append(undeadHumanoidList)
undeadHumanoidList.append(vampireList)
undeadHumanoidList.append(zombieList)
undeadHumanoidList.append(skeletonList)
undeadHumanoidList.append(ghostList)

            #Undead - Non Humanoid
undeadList = []
specterList = []
#Append in non humanoid undead list
undeadList.append(specterList)

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

    #Inhabited places - hardcoded => do procedurally generated ones later in definitions ?

        #Villages
villageNamesList.append("Slenia")

        #Cities and Towns

        #Main cities
majorCitiesNamesList.append("Otoria")

    #Dungeons - hardcoded base

        #Subterranean

        #Overworld

        #Air placed

        #Other dimensions

    #Dungeons - procedurally generated + procedural algorithm => TO DO later in definitions ?

    #Environement List
environmentTypeList.append("Plains")
environmentTypeList.append("Savanna")
environmentTypeList.append("Forest")
environmentTypeList.append("Cave")
environmentTypeList.append("Desert")
environmentTypeList.append("Snow")
environmentTypeList.append("Mountains")
environmentTypeList.append("River")
environmentTypeList.append("Lake")
environmentTypeList.append("Sea")
environmentTypeList.append("Sky")

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

#Variables for XP and coins
valueFactorHuman = 20
valueFactorMonster = 30

    #Characters

        #Human NPC Base Template
baseHumanNPCTemplate = copy.deepcopy(baseNPCTemplate)
baseHumanNPCTemplate['Origin'] = originHumanList[0]
baseHumanNPCTemplate['Hostility'] = "Variable"
baseHumanNPCTemplate['Species'] = "Human"
baseHumanNPCTemplate['Type'] = "HumanRaceVarious"
baseHumanNPCTemplate['CoinFactorHuman'] = valueFactorHuman * 1.5 * baseHumanNPCTemplate['Rank']
baseHumanNPCTemplate['CoinFactorArena'] = valueFactorHuman * 2.5 * (1 + baseHumanNPCTemplate['Rank'])
baseHumanNPCTemplate['CoinFactor'] = 0
baseHumanNPCTemplate['XPHuman'] = valueFactorHuman * 1.2 * (1 + baseHumanNPCTemplate['Rank'])

            #Human in general context
generalHumanNPCTemplate = copy.deepcopy(baseHumanNPCTemplate)
generalHumanNPCTemplate['CoinFactor'] = generalHumanNPCTemplate['CoinFactorHuman']

            #Human in arena context
arenaHumanNPCTemplate = copy.deepcopy(baseHumanNPCTemplate)
arenaHumanNPCTemplate['CoinFactor'] = arenaHumanNPCTemplate['CoinFactorArena']


        #Monster Base Template
baseMonsterTemplate = copy.deepcopy(baseNPCTemplate)
baseMonsterTemplate['Origin'] = originMonsterList[0]
baseMonsterTemplate['Hostility'] = "Hostile"
baseMonsterTemplate['Species'] = "Default"
baseMonsterTemplate['Type'] = "Monster"
baseMonsterTemplate['Rank'] = 1
baseMonsterTemplate['CoinFactorSpecies'] = valueFactorMonster * 1.2 * baseMonsterTemplate['Rank']
baseMonsterTemplate['CoinFactorType'] = valueFactorMonster * 1.4 * baseMonsterTemplate['Rank']
baseMonsterTemplate['CoinFactor'] = 0
baseMonsterTemplate['XP'] = valueFactorMonster * 1.3 * baseMonsterTemplate['Rank']

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
ogreTemplate['Type'] = "OgreLike"
ogreTemplate['ManaRegeneration'] = 0

            #Undead
undeadTemplate = copy.deepcopy(baseMonsterTemplate)
undeadTemplate['LivingState'] = "Undead"
undeadTemplate['ManaRegeneration'] = 0

                #Vampires
                #Zombies
                #Skeletons
                #Ghosts
                #Other undead monsters - can be anything for particular situations

            #Slimy
slimyTemplate = copy.deepcopy(baseMonsterTemplate)
slimyTemplate['Species'] = "Slimy"
slimyTemplate['ManaRegeneration'] = 0

                #Slimes
slimeTemplate = copy.deepcopy(slimyTemplate)
slimeTemplate['Type'] = "Slime"

                #Muddies - Muds
mudTemplate = copy.deepcopy(slimyTemplate)
mudTemplate['Type'] = "Mud"

                #Gels
gelTemplate = copy.deepcopy(slimyTemplate)
gelTemplate['Type'] = "Gel"

        #Pets

    #Base global inhabited places Template

    #Inhabited places - hardcoded
inhabitedPlaceTemplate = {}

        #Villages - Listing
villageTemplate = copy.deepcopy(inhabitedPlaceTemplate)

        #Cities and Towns - Listing

        #Main cities - Listing
majorCityTemplate = copy.deepcopy(inhabitedPlaceTemplate)

    #Dungeons - hardcoded base

        #Subterranean

        #Overworld

        #Air placed

        #Other dimensions

    #Dungeons - procedurally generated + procedural algorithm => TO DO later

    #Environment Types

        #General Template
environmentBaseTemplate = {}
environmentBaseTemplate['Type'] = "Default"
environmentBaseTemplate['WorldLocation'] = "CardinalPoint"
environmentBaseTemplate['Fauna'] = "CorrespondingList"
environmentBaseTemplate['DifficultyFactor'] = 0

        #Plains

        #Savanna

        #Forest

        #Cave

        #Desert

        #Snow

        #Mountains

        #River

        #Lake

        #Sea

        #Sky


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
goblin['CoinFactorSpecies'] = 3

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
hobgoblin['CoinFactorSpecies'] = 5

goblinoidList.append(hobgoblin)
mobList.append(hobgoblin)
mobCaveList.append(hobgoblin)
mobForestList.append(hobgoblin)

                #Orcoids

                #Ogre likes

            #Undead

                #Vampires
                #Zombies
                #Skeletons
                #Ghosts
ghost = copy.deepcopy(undeadTemplate)

undeadHumanoidList.append(ghost)
mobList.append(ghost) #continue to append to other lists

                #Other undead monsters - can be anything for particular situations
specter = copy.deepcopy(undeadTemplate)

undeadList.append(specter)
mobList.append(specter) #continue to append in other lists

            #Slimy

                #Slimes

slime = copy.deepcopy(slimeTemplate)
slime['Name'] = "Slime"
slime['Power'] = 1
slime['Defense'] = 0
slime['Life'] = 4
slime['MaxLife'] = 4
slime['Stamina'] = 4
slime['MaxStamina'] = 4
slime['XP'] = 1
slime['CoinFactorSpecies'] = 0.5

slimelist.append(slime)
mobList.append(slime)
mobCaveList.append(slime)
mobPlainsList.append(slime)

                #Muddies - Muds
                #Gels

        #Pets

    #Base global inhabited places Template

    #Inhabited places - hardcoded

        #Villages - Listing
villageSlenia = copy.deepcopy(villageTemplate)

        #Cities and Towns - Listing

        #Main cities - Listing
majorCitiesOtoria = copy.deepcopy(majorCityTemplate)

    #Dungeons - hardcoded base

        #Subterranean

        #Overworld

        #Air placed

        #Other dimensions

    #Dungeons - procedurally generated + procedural algorithm => TO DO later

    #Environment Names - Example : "Plains of Skaria" can be Plains or other type

        #Plains

        #Savanna

        #Forest

        #Cave

        #Desert

        #Snow

        #Mountains

        #River

        #Lake

        #Sea

        #Sky

#################################################################################################
#                                   DICTIONARIES REFORMING                                      #
#################################################################################################

