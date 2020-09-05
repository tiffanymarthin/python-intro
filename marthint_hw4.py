"""
File Name: marthint_hw3p2ext.py
Name: Tiffany Marthin
Last Modified: 5/27/2020
Summary: Individual Programming 4
Goal: Create a multi-players simple game for up to 8 people. The goal is to defeat
the boss who spawn minions to attack the players. Each character has the ability to
attack, charge (increase the damage of next attack) and defense (being protected for the
next 3 attacks).
"""

import math #use the floor method from math library

"""
Part 1 (Super Class)
This Character class is the super class that contains the general character attributes
such as name, level, hp, attack, defense, exp. 
It also has some methods to set and get the attributes, and lastly this class
has basic methods to attack opponents.
Note: the exp default is set as 100 since it's not specified in the instructions.
"""

class Character:
    def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.maxhp = hp
        self.at = at
        self.df = df
        self.exp = exp

    def __repr__(self):
        '''added this for debugging purposes'''
        return '{player: ' + self.name + ', hp: ' + str(self.hp)+ '}'

    def rename(self, name):
        '''renames the character'''
        self.name = name

    def setlvl(self, lvl):
        '''set level to new value or 0 if below 0'''
        if lvl <= 0:
            self.lvl = 0
        else:
            try:
                self.lvl = int(lvl)
            except:
                self.lvl = lvl

    def sethp(self, hp):
        '''set HP to new value or 0 if below 0'''
        if hp <= 0:
            self.hp = 0
        else:
            try:
                self.hp = int(hp)
            except:
                self.hp = hp

    def setat(self, at):
        '''set attack to new value or 0 if below 0'''
        if at <= 0:
            self.at = 0
        else:
            try:
                self.at = int(at)
            except:
                self.at = at

    def setdf(self, df):
        '''set defense to new value or 0 if below 0'''
        if df <= 0:
            self.df = 0
        else:
            try:
                self.df = int(df)
            except:
                self.df = df

    def setexp(self, exp):
        '''set exp to new value or 0 if below 0'''
        if exp <= 0:
            self.exp = 0
        else:
            try:
                self.exp = int(exp)
            except:
                self.exp = exp

    def getname(self):
        '''returns the character\'s name'''
        return self.name

    def getlvl(self):
        '''returns the character\'s level'''
        return self.lvl

    def gethp(self):
        '''returns the character\'s hp'''
        return self.hp

    def getat(self):
        '''returns the character\'s attack'''
        return self.at

    def getdf(self):
        '''returns the character\'s defense'''
        return self.df

    def getexp(self):
        '''returns the character\'s exp'''
        return self.exp

    def attack(self, other):
        '''attack method which will deduct other\'s hp by self attack minus the other\'s defense'''
        other.sethp(other.hp - self.at + other.df)
        '''printout status of attacker and attacked\'s HP.'''
        print(self.name, " attacked ", other.name, sep="", end=". ")
        print(self.name, "'s HP is ", self.hp, "/", self.maxhp, sep="", end=". ")
        print(other.name, "'s HP is ", other.hp, "/", other.maxhp, sep="", end=". \n")

        if other.hp == 0:
            print(other.name, " has been defeated.", sep="")    #notify that opponent is defeated when opponent HP is 0


"""
Part 2 (Inheritance 1)
This class is Character's inheritance, but with different default for attributes. It also has
some additional attributes like charge and shield counts, to track if the character turns on the
charge feature and if the character has shield on. This class also some additional methods to recover
and full heal.
Note: If the player still has shield available, the shield action will not do anything. It only resets to 
3 shields if the player was not on shield.  
"""

class MajorCharacter(Character):
    def __init__(self, name, lvl=1, hp=100, at=10, df=5, exp = 0):      #set the default to match the part 4 of homework instruction (player's default)
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.charged = False
        self.shieldct = 0           #to track the shield counts.

    def sethp(self, hp):
        '''setting the hp of character, taking into account if he/she has a shield on'''
        if self.shieldct == 0:
            if hp <= 0:
                self.hp = 0
            else:
                try:
                    self.hp = int(hp)
                except:
                    self.hp = hp
        else:
            self.shieldct = max(self.shieldct - 1, 0)       #nothing happens if there is shield on, but deduct the shield by 1

    def recover(self, recoverypts):
        '''recover the current character's HP by recovery pts'''
        self.hp = min(self.hp + recoverypts, self.maxhp)
        print(self.name, "'s HP has been restored to ", self.hp, "/", self.maxhp, ".", sep = "")

    def fullheal(self):
        '''recovers the current character's HP to the max HP'''
        self.hp = self.maxhp
        print(self.name, "'s HP has been fully restored (", self.hp, "/", self.maxhp, ").", sep = "")

    def shield(self):
        '''reset the number of protects back to three only if the character has no shield '''
        if self.shieldct == 0:
            self.shieldct = 3
        print(self.name, " is safe from the next ", self.shieldct, " attacks.", sep = "")

    def charge(self):
        '''indicate that the character has charge feature on, and will activate the more powerful attack in the method below'''
        self.charged = True
        print(self.name, " charged.", sep = "")

    def attack(self, other):
        ''' subtract the other's HP, modification of the method in character since it has the charge feature'''
        if self.charged:
            other.sethp(other.hp - self.at * 2.5 + other.df)        #when charged, attack is more powerful
            self.charged = False
        else:
            other.sethp(other.hp - self.at + other.df)

        # game status of the attack aftermath
        print(self.name, " attacked ", other.name, sep="", end=". ")
        print(self.name, "'s HP is ", self.hp, "/", self.maxhp, sep="", end=". ")
        print(other.name, "'s HP is ", other.hp, "/", other.maxhp, sep="", end=". \n")

        if other.hp == 0:
            print(other.name, " has been defeated.", sep="")


"""
Part 3 (Inheritance 2)

The Minion and Boss classes are the inheritance of Character class.
Minion is pretty much the same with Character class, except there is no default values
for its initialization as they will be coming from the boss character. (except for df and 
exp that are both 0 for Minions).
Similarly for boss, it's mostly the same with Character class but has the spawn method
to generate Minion objects. It also has different default values and hp will be a required input based on
number of players
"""

class Minion(Character):
    def __init__(self, name, lvl, hp, at, df=0, exp=0):
        Character.__init__(self, name, lvl, hp, at, df)


class Boss(Character):
    def __init__(self, name, lvl=1, hp, at=100, df=0, exp=0):
        Character.__init__(self, name, lvl, hp, at, df)
        self.maxhp = hp

    def spawn(self):
        '''create Minion object, that has same level with the boss character, but half '''
        m = Minion('Minion', lvl = self.lvl ,hp = math.floor(0.25 * self.maxhp), at = math.floor(0.25 * self.at), df=0, exp=0)
        print("Boss spawned Minion (HP ", m.hp, ", AT ", m.at, ", DF ", m.df, ")", sep = "")
        return m



#User-Defined Exception to catch if user inputs are not as expected
class Error(Exception):
    pass
class ValueNotRight(Error):
    pass


"""
Part 4 (Game Program)
Below is the main program to run the game.
"""

"""
Prompting the player on how many players, will let the player know if input is invalid. 
Valid input is numerical 1-8.
"""
while True:
    try:
        num_players = eval(input("How many players? "))
        if num_players > 8 or num_players < 1:
            raise ValueNotRight
        break
    except (ValueNotRight, NameError):
        print("Invalid input. Value has to be a number between 1-8. ")

players = []        #List of alive players
minions = []        #List of alive minions
game = True         #Indicator when the game should keep going or stop - will stop if the players lose/win

"""
Prompt user to enter players' names
"""
for i in range(num_players):
    player = input("Player "+ str(i+1) + " Name: ")
    players.append(MajorCharacter(player))

"""
Create the Boss character with hp 20 * number of players
Other attributes are set to the Boss character's default.
"""
boss = Boss("Boss", hp = 20 * num_players)

#create a function to print 3 action options for the users, to simplify the code.
def options():
    print('1. Attack')
    print('2. Charge')
    print('3. Shield')

#The game loop
while game:
    minions.append(boss.spawn())        #start each round by creating a minion, and tracking the minions in the list

    for i in range(len(players)):       #another loop to get each player to take action

        while True:                     #ensure the validity of user input, has to be an integer 1,2, or 3
            try:
                options()
                action = eval(input(players[i].name + ", what would you like to do? "))
                if action < 1 or action > 3:
                    raise ValueNotRight
                break
            except (ValueNotRight, NameError) as e :
                print("Invalid input.")

        """
        Attack action. Could only attack the boss if no alive minion.
        """
        if action == 1:
            if len(minions) == 0:
                print("1. ", boss.name, " (HP ", boss.hp, ")", sep = "")
                players[i].attack(boss)
                if boss.hp == 0:
                    print("You win!")
                    game = False
                    break               #exits the loop if the boss hp is 0

            else:                       #the loop if there are still alive minions.
                while True:             #this will ensure user inputs are valid when selecting which minion to attack
                    try:
                        for j in range(len(minions)):
                            print(j + 1, ". ", minions[j].name, "(HP ", minions[j].hp, ")", sep="")
                        attacked = eval(input(players[i].name + ", who would you like to attack? "))
                        if attacked < 1 or attacked > len(minions):
                            raise ValueNotRight
                        break
                    except (ValueNotRight, NameError) as e:
                        print("Invalid input.")

                players[i].attack(minions[attacked-1]) #attack the selected minion

                if minions[attacked-1].hp == 0:         #remove minion if the minion's hp is 0
                    del minions[attacked-1]

        elif action == 2:             #charge action, will turn on the charge indicator for next attack
            players[i].charge()

        elif action == 3:             #defense action, will shield the player for next 3 attacks. Useless if there is still protection.
            players[i].shield()

    if boss.hp == 0:                  #another break to ensure if boss hp is 0 then the game should stop running.
        break

    players.sort(key=lambda x: x.hp, reverse=True)      #sorting the players list according to its HP, from the highest to lowest

    """
    Following loop is the last step of the loop where the minions attack the players
    if there is still an alive minion.
    """
    if len(minions) == 0:
        print("There are no Minions to attack.")
    else:
        for i in range(len(minions)):               #each minion will attack the player with lowest HP
            minions[i].attack(players[-1])

            if players[-1].hp == 0:                 #delete player from the alive player list if player's HP is 0
                del players[-1]

            if len(players) == 0:                   #ends the game if all players are dead
                print("You lose.")
                game = False
                break
