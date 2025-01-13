import random, math, sys, sqlite3

try:
    #Connection to database
    connection = sqlite3.connect('database/RPG_Database.db')
    cursor = connection.cursor()

    #Database tables creation functions
    def databaseSaves():
        
        #Create saves table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS saves(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                characterName TEXT,
                characterLevel INTEGER,
                characterXP INTEGER
            )
        """)
        connection.commit()
    
    def databaseItems():
        pass

    def databaseWeapons():
        
        #Create weapons table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weapons(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                weaponName TEXT,
                weaponType TEXT,
                weaponRank TEXT,
                weaponLevel INTEGER,
                weaponPrice INTEGER
            )
        """)
        connection.commit()
        
    def databaseArmors():
        
        #Create armors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS armors(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                armorName TEXT,
                armorType TEXT,
                armorRank TEXT,
                armorLevel INTEGER,
                armorPrice INTEGER
            )
        """)
        connection.commit()

    def databasePotions():
        pass

    def databaseIngredients():
        pass

    def databaseMonsters():
        pass

    #Database tables update functions
    def databaseSaveCreation():
        pass

    #Global check variable
    combatCheck = False
    playCheck = True
    villageCheck = True
    dungeonCheck = True

    #Player character
    player = {}
    player['Name'] = str(input("Enter your name\n"))

    print("So you are called ", player['Name'])

    player['Inventory'] = []

    player['Coins'] = 0
    player['XP'] = 0
    player['Level'] = 1
    player['Power'] = 1
    player['Defense'] = 0
    player['Armor'] = ""
    player['ArmorDefense'] = 0
    player['Avoid'] = 0
    player['Life'] = 100
    player['MaxLife'] = 100
    player['Mana'] = 0
    player['MaxMana'] = 0
    player['Stamina'] = 50
    player['MaxStamina'] = 50
    player['XP'] = 0
    player['Level'] = 1
    player['Weapon'] = ""
    player['WeaponDamage'] = 0
    player['DamageBonus'] = 0
    player['DefenseBonus'] = 0
    player['ClassChoice'] = int(input("Choose your class : 1 for Swordmaster, 2 for Warrior, 3 for Knight, 4 for Archer\n"))

    #Weapon choice
    if player['ClassChoice'] == 1:
        player['Weapon'] = "Sword"
        player['Armor'] = "Leather Armor"
        player['WeaponDamage'] = 8
        player['ArmorDefense'] = 8
        player['Avoid'] = 10
        print("You have equipped a sword and a leather armor, you have 10% chance to avoid\n")
    elif player['ClassChoice'] == 2:
        player['Weapon'] = "Axe"
        player['Armor'] = "Iron Armor"
        player['WeaponDamage'] = 16
        player['ArmorDefense'] = 16
        print("You have equipped an axe and an iron armor\n")
    elif player['ClassChoice'] == 3:
        player['Weapon'] = "Spear"
        player['Armor'] = "Boiled Leather Armor"
        player['WeaponDamage'] = 12
        player['ArmorDefense'] = 12
        print("You have equipped a spear and a boiled leather armor\n")
    elif player['ClassChoice'] == 4:
        player['Weapon'] = "Bow"
        player['Armor'] = "Cloth Armor"
        player['WeaponDamage'] = 6
        player['Avoid'] = 30
        print("You have equipped a bow and a cloth armor, you have 0 armor but 30% chance to avoid\n")
    else:
        print("Pass here") #Debug
        pass

    #Define monsters
    mobList = []

    goblin = {}
    goblin['Type'] = "Goblinoid"
    goblin['Name'] = "Goblin"
    goblin['Power'] = 12
    goblin['Defense'] = 2
    goblin['Life'] = 50
    goblin['MaxLife'] = 50
    goblin['XP'] = 10
    goblin['CoinFactor'] = 3

    mobList.append(goblin)

    hobgoblin = {}
    hobgoblin['Type'] = "Goblinoid"
    hobgoblin['Name'] = "Hobgoblin"
    hobgoblin['Power'] = 16
    hobgoblin['Defense'] = 4
    hobgoblin['Life'] = 60
    hobgoblin['MaxLife'] = 60
    hobgoblin['XP'] = 14
    hobgoblin['CoinFactor'] = 5

    mobList.append(hobgoblin)

    slime = {}
    slime['Type'] = "Slimy"
    slime['Name'] = "Slime"
    slime['Power'] = 1
    slime['Defense'] = 0
    slime['Life'] = 4
    slime['MaxLife'] = 4
    slime['XP'] = 1
    slime['CoinFactor'] = 0.5

    mobList.append(slime)

    #Level up function
    def levelUp():
        pass # stats up

    #Level up function end

    #Death function
    def death():
        print("You died...")
        choice = int(input("Wiuld you like to resurrect in the village church ? 1 for yes, 0 for no"))
        if choice == 1:
            pass #resurrect
        elif choice == 2:
            print("You died for good... the character will be deleted...")
            #call delete function for char db
            sys.exit()
        else:
            print("Not a good choice")
    #Death function end

    #Combat function
    def combatLoop(monster):

        #Initializing enemy variable
        monster = random.choice(mobList)
        enemy = monster.copy()

        #Combat checker variable
        global combatCheck

        #Storage variable for save purpose
        basePower = player['Power']
        baseDefense = player['Defense']

        #Anouncing monster
        print("A wild " + str(monster['Name']) + " appears !")

        while enemy['Life'] > 0 and combatCheck == False:
            
            #Giving values for heads up
            print("Your health : ", int(player['Life']), "\nMob health : ", int(enemy['Life']))
            
            #Each turn reinitialize values
            player['Power'] = basePower
            player['Defense'] = baseDefense
            player['DefenseBonus'] = 0
            playerDamage = player['Power'] + player['WeaponDamage']
            playerDealtDamage = playerDamage - enemy['Defense']
            playerProtection = player['Defense'] + player['ArmorDefense']
        
            #Declare variables for choice and combat
            choice = 0
            monsterDamage = 0
            gainedCoins = 0
            fleeRandom = random.randint(0, 99)
            avoidRandom = random.randint(0, 99)
            coinsRandom = random.randint(0, 49)

            #If player died then anounce it
            if player['Life'] <= 0:
                death()

            #Indicating player turn
            print("\nPlayer turn :")
            choice = int(input("What do you want to do ?\nAttack : 1\nHeal : 2\nDefend : 3\nFlee : 4\n"))

            #Decision tree for player turn
            if choice == 1: #attack
                enemy['Life'] = max((enemy['Life'] - playerDealtDamage), 0)
                print("Inflicted ", playerDealtDamage, " damage")
            elif choice == 2: #heal
                #Condition = player have lost health or not
                if player['Life'] < player['MaxLife']:
                    healthReceived = min((player['MaxLife'] - player['Life']), playerDamage)
                    player['Life'] = min((player['Life'] + healthReceived), player['MaxLife'])
                    print("You healed yourself for ", healthReceived, " points")
                else:
                    print("You cannot heal yourself if you have taken no damage !")
                    continue
            elif choice == 3: #defend
                player['DefenseBonus'] = (player['ArmorDefense'] / 2)
                playerProtection = playerProtection + player['DefenseBonus']
                print("You chose defense, gained + 50% defense for one turn")
                print("debug defense :", playerProtection)
            elif choice == 4: #flee
                print("Try to flee !")
                combatCheck = True
                break
            
            #Indicating mob turn
            print("\nEnemy turn :")

            #Mob decision tree
            if enemy['Life'] > (round(enemy['MaxLife']/2)):
                #If mob has more than 50% life then it attacks
                if avoidRandom > player['Avoid']:
                    monsterDamage = max(enemy['Power'] - playerProtection, 0)
                    print("Mob attacks for ", monsterDamage ," !")
                    player['Life'] = max((player['Life'] - monsterDamage), 0)
                else:
                    monsterDamage = 0
                    print("You avoided the attack")
            else:
                #If mob has less than 50%, it has a chance to try and flee combat
                if enemy['Life'] > (round(enemy['MaxLife']/4)):
                    #Between 25% and 50% life it has a small chance
                    if fleeRandom > 25:
                        if avoidRandom > player['Avoid']:
                            monsterDamage = max(enemy['Power'] - playerProtection, 0)
                            print("Mob attacks for ", monsterDamage ," !")
                            player['Life'] = max((player['Life'] - monsterDamage), 0)
                        else:
                            monsterDamage = 0
                            print("You avoided the attack")
                    else:
                        #Mob successfully flees, combat ends
                        print("The ", enemy['Name'], " flees !")
                        combatCheck = True
                        break
                elif enemy['Life'] < (round(enemy['MaxLife']/4)) and enemy['Life'] > 0:
                    #Between 1 point and 25% life it has double the chance
                    if fleeRandom > 50:
                        if avoidRandom > player['Avoid']:
                            monsterDamage = max(enemy['Power'] - playerProtection, 0)
                            print("Mob attacks for ", monsterDamage ," !")
                            player['Life'] = max((player['Life'] - monsterDamage), 0)
                        else:
                            monsterDamage = 0
                            print("You avoided the attack")
                    else:
                        #Mob successfully flees, combat ends
                        print("The ", enemy['Name'], " flees !")
                        combatCheck = True
                        break
                else:
                    #If enemy dies exit system and indicate to player
                    print("You have vanquished the enemy")
                    combatCheck = True
                    player['XP'] += goblin['XP']
                    print("You have gained ", int(enemy['XP']), " XP points, and have ", int(player['XP']), " XP points")
                    gainedCoins = 1 + round(coinsRandom * enemy['CoinFactor'])
                    player['Coins'] += gainedCoins
                    print("You also gained ", gainedCoins, " coins !" )
                    
            #Loop resumes

        #Loop end

    #Combat function end

    #Village function
    def village():
        
        #Village checker variable
        global villageCheck

        #Choice variable
        choice = 0

        while villageCheck == True:
            choice = int(input("What do you want to do in the village ? 1 to shop, 2 to go to the tavern, 3 to go to the guild, 4 to go to the church, 0 to quit"))

            #Village - player decision tree
            if choice == 1:
                #Chose shopping
                shops()
            elif choice == 2:
                #Chose tavern
                print("Welcome to the tavern, what can I do for you ?")
                tavern()
            elif choice == 3:
                #Chose guild
                print("Welcome to the Guild of Adventurers ! What can we do for you ?")
                guild()
            elif choice == 4:
                #Chose church
                church()
            elif choice == 0:
                #Chose to quit village
                print("Exciting village...")
                villageCheck = False
                
    #Village function end

    #Village shops function
    def shops():
        print("What shop do you want to visit ?")
        choice = int(input("Available shops are : Armory (1), Jewelry (2), Alchemist (3), General store (4), Exit (0)"))
        if choice == 1:
            #Visit armory
            armory()
        elif choice == 2:
            #Visit jewelry
            jewelry()
        elif choice == 3:
            #Visit alchemist
            alchemist()
        elif choice == 4:
            #Visit general store
            generalStore()
        elif choice == 0:
            #Quit shopping
            print("Returning to town center...")
            village()
        else:
            print("Wrong choice but quitting to village...")
            village()
        
    #Global function for all shops end

    #Function for armory
    def armory():
        choice = int(input("Do you want to buy (1) or sell (2) ? 0 to quit"))
        if choice == 1:
            pass #buy
        elif choice == 2:
            pass #sell
        elif choice == 0:
            print("Exiting armory...")
            shops()
        
    #Armory end

    #Function for jewelry
    def jewelry():
        choice = int(input("Do you want to buy (1) or sell (2) ? 0 to quit"))
        if choice == 1:
            pass #buy
        elif choice == 2:
            pass #sell
        elif choice == 0:
            print("Exiting jewelry...")
            shops()
        
    #Jewelry end

    #Function for alchemist
    def alchemist():
        choice = int(input("Do you want to heal (1), buy (2) or sell (3) ? 0 to quit"))
        if choice == 1:
            pass #heal
        elif choice == 2:
            pass #buy
        elif choice == 3:
            pass #sell
        elif choice == 0:
            print("Exiting alchemist...")
            shops()
        
    #Alchemist end

    #Function for general store
    def generalStore():
        choice = int(input("Do you want to buy (1) or sell (2) ? 0 to quit"))
        if choice == 1:
            pass #buy
        elif choice == 2:
            pass #sell
        elif choice == 0:
            print("Exiting store...")
            shops()
        
    #General store end

    #Function for tavern
    def tavern():
        choice = int(input("You can : Listen to rumors (1), Shop for food (2), Rent a room (3), Exit (0)"))
        if choice == 1:
            #Chose rumors
            rumors()
        elif choice == 2:
            #Chose food shopping
            foodShop()
        elif choice == 3:
            #Chose rest - all stats are regen to max 75%
            choice = int(input("Rest effectivness is 75% max, do you want to rent the room (1 yes or 0 no) ?"))
            if choice == 1:
                rest()
            elif choice == 0:
                tavern()
            else:
                print("Wrong choice but staying in tavern...")
                tavern()
        elif choice == 0:
            #Chose quitting
            print("Exiting tavern...")
            village()
        else:
            print("Wrong choice but exiting to village...")
            village()
        
    #Tavern end

    #Function for food shopping
    def foodShop():
        choice = int(input("Do you want to buy (1) or sell (2) ? Exit (0)"))
        if choice == 1:
            pass #buy food
        elif choice == 2:
            pass #sell food
        elif choice == 0:
            pass #quit tavern
            
        
    #Food shopping end

    #Function for the guild
    def guild():
        choice = int(input("Available services are : Look for quests (1), Shop for food (2), Go to your room (3), Talk with people (4), Exit (0)"))
        if choice == 1:
            #Chose quests
            print("What quests are available... ?")
            pass #make quests available via random gen and dictionary + db
        elif choice == 2:
            #Chose food shopping
            foodShop()
        elif choice == 3:
            #Chose hidden stash and rest to 50%
            pass #go to room for hidden stash in db call guildRoom()
        elif choice == 0:
            pass #quit shopping
            village()
        else:
            print("Wrong choice but exiting to village...")
            village()
    #Guild end

    #Function for church
    def church():
        print("Welcome to the church, what do you want to do ?")
        choice = int(input("We offer those services : 1 to pray a god, 2 to receive a boon, 3 to remove a curse, 4 to buy holy water, 5 to save, 0 to quit"))
        if choice == 1:
            #Chose prayer
            print("What god to pray... ?")
            pass #choose god from db
        elif choice == 2:
            #Chose boon from priest
            pass #call boon()
        elif choice == 3:
            #Chose curse removal
            pass #call curseRemoval()
        elif choice == 0:
            pass #quit shopping
            village()
        else:
            print("Wrong choice but exiting to village...")
            village()
    #Church end

    #Function for rumors
    def rumors():
        pass
    #Rumors end

    #Function for stories
    def stories():
        pass
    #Stories end

    #Function for rest
    def rest():
        pass
    #Rest end

    #Dungeon function
    def dungeon():
        while player['Life'] > 0 and combatCheck == False:
            combatLoop(mobList)


    #Dongeon function end

    #Options function
    def options():
        pass #call delete or other db functions
    #Options end

    def game():
        
        #Call database functions
        databaseSaves()
        databaseWeapons()
        databaseArmors()
        
        #Play checker variable
        global playCheck

        #Choice variable
        choice = 0

        #Game loop
        while playCheck == True:
            print("What do you want to do ?")
            choice = int(input("Enter village (1), Explore surroundings (2), Explore dungeon (3), Additional options (4), Quit game (0)\n"))
            if choice == 1:
                while villageCheck == True:
                    village()
            elif choice == 2:
                pass
            elif choice == 3:
                dungeon()
            elif choice == 4:
                pass #delete save, modify settings, other things
                options()
            elif choice == 0:
                print("Quitting game...\n")
                playCheck = False
                sys.exit()
            else:
                #Dev mode
                print("You typed something and you can now access developer mode\n")

    #Call global game function
    game()

except Exception as error:
    print("Error ", error)
    connection.rollback()

finally:
    connection.close()