import math, random

class Character:
    
    #Main Class for specifying character types
    kind = "character";

    #Name placeholder
    name = "";
    weapon = "";

    #Define character
    def __init__(self):
        pass;
    
    def stats (self, levelFixed, healthMax, healthCurrent, stamina, mana, power, defense, block, xpPoints):
        self.levelFixed = self.stats['levelFixed'];
        self.healthMax = healthMax;
        self.healthCurrent = healthCurrent;
        self.stamina = stamina;
        self.mana = mana;
        self.power = power;
        self.defense = defense;
        self.block = block;
        self.xpPoints = xpPoints;
    
class PlayerCharacter(Character):
    
    #Player character type
    kind = "player character";

    #Initialize level and experience
    xp = 0;
    level = 1;

    #Initialize player
    def __init__(self, name, weapon):
        self.name = name;
        self.weapon = weapon;
        self.inventory = [];

    def levelup(self):
        self.level += 1;
        print("\n**~~~~**\nLEVEL UP ! Welcome to level {}\n**~~~~**\n".format(self.level));

        
    
class NonPlayerCharacter(Character):
    
    #Non player character type
    kind = "non player character";

    def __init__(self):
        pass;

class Villager(NonPlayerCharacter):
    
    #Villager type for non mob example
    kind = "villager";

    def __init__(self):
        pass;

class Mob(NonPlayerCharacter):
    
    #Mob type
    kind = "Mob";

    def __init__(self):
        pass;

class PassiveMob(Mob):
    
    #Passive mob type = animal
    kind = "animal";

    def __init__(self):
        pass;

class NeutralMob(Mob):
    
    #Passive mob type = beast
    kind = "beast";

    def __init__(self):
        pass;
    
class HostileMob(Mob):
    
    #Hostile mob type = monster
    kind = "hostile";

    #Define monster
    def __init__(self):
        pass;
        
#Define a player variable to initialize
def player():
    PlayerCharacter(str(input("Choose name")), 1, 100, 100, 100, 100, 1, 1, 0, 0);

#Initialize few mobs for combat
goblin = HostileMob('Goblin', 'Goblinoid', 1, 10, 10, 5, 0, 1, 1, 0, 3);
slime = HostileMob('Slime', 'Slimy', 1, 1, 1, 0, 0, 1, 0, 0, 1);
orc = HostileMob('Orc', 'Goblinoid', 1, 20, 20, 10, 0, 3, 1, 0, 7);

#List for storing hostile mob and randomly choose in combat
mobList = [];

#Pushing mobs into list
mobList.append(goblin, slime, orc);

class GameElements:

    #Combat Loop function
    def combatLoop(self, player, mob):
    
        #Global Class variables
        player = playerGlobal;
        mob = random.choice(mobList);
        xp = 0;
        
        #Declare monster randomly chosen
        mob = random.choice(mobList);
        
        #Declare variables for choice and combat check
        choice = 0;
        combatCheck = False;
        damage = 0;

        #Random number to decide monster flee
        fleeRandom = random.randint(0, 99);

        #Storage variable for save purpose
        basePower = player.power;
        baseDefense = player.defense;
        baseBlock = player.block;

        while combatCheck == False and mob.healthCurrent > 0 and player.healthCurrent > 0:
            
            #Giving values for heads up
            print("Your health : {player.healthCurrent}\nMob health : {mob.healthCurrent}");
            print("Your stamina : {player.stamina}\nYour mana : {player.mana}")

            #Indicating player turn
            print("Player turn :");
            int(input("What do you want to do ?\nAttack : 1\nHeal : 2\nDefend : 3\nFlee : 4"));

            #Each turn reinitialize values
            player.power = basePower;
            player.defense = baseDefense;
            player.block = baseBlock;

            #Decision tree for player turn
            if choice == 1: #attack
                mob.healthCurrent -= player.power;
                print("Inflicted {player.power} damage");
                print(mob.healthCurrent);
            elif choice == 2: #heal
                #Condition = player have lost health or not
                if player.healthCurrent < player.healthMax:
                    healthReceived = min((player.healthCurrent + player.power - player.healthMax), player.power);
                    player.healthCurrent = min((player.healthCurrent + player.power), player.healthMax);
                    print("You healed yourself for {healthReceived} points");
                else:
                    print("You cannot heal yourself if you have taken no damage !");
            elif choice == 3: #defend
                print("You chose defense, gained + 50% defense for one turn");
                player.defense *= 1.5;
            elif choice == 4: #flee
                print("Try to flee !");
                combatCheck = True;
                break;
            else:
                print("Not a suitable choice");
                continue;
            
            #Indicating mob turn
            print("Enemy turn :");

            #Mob decision tree
            if mob.healthCurrent > (round(mob.healthMax/2)):
                print("Mob attacks !");
                damage = mob.power - player.defense;
                player.healthCurrent = max((player.healthCurrent - damage), 1);
            else:
                if mob.healthCurrent > (mob.healthMax/4):
                    if fleeRandom > 50:
                        print("Mob attacks !");
                        damage = mob.power - player.defense;
                        player.healthCurrent = max((player.healthCurrent - damage), 1);
                    else:
                        print("Monster flees !");
                        combatCheck = True;
                        break;
                elif mob.healthCurrent < (mob.healthMax/4):
                    if fleeRandom > 75:
                        print("Mob attacks !");
                        damage = mob.power - player.defense;
                        player.healthCurrent = max((player.healthCurrent - damage), 1);
                    else:
                        print("Monster flees !");
                        combatCheck = True;
                        break;
        #Loop resumes
                        

    def drop(self):

        #Item list
        items = [];

    def inventory(self):
        #Inventory table
        inventory = [];
    
class Master:

    #Master function in Master Class
    def master(self):
    
        #Global Class variables
        player = playerGlobal;
        mob = random.choice(mobList);

        #Call function
        GameElements.combatLoop(player, mob);
    
    master();