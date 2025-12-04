import time 
import os
import random
class Enimy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def attack(self):
        attack_streanght = random.randint(10, 20)
        player1.heath = player1.heath - attack_streanght     
        print(f"the enimy attacks you with {attack_streanght}  power")
        
class Player:
    def __init__(self, name, health, attack, hunger, game_over):
        self.name = name
        self.heath = health
        self.attack = attack
        self.hunger = hunger
        self.game_over = game_over
def clear():  
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("")


def typewriter_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True) 
        time.sleep(delay)
    print() 
def bar():
    print(f"your health is {player1.heath}")
def win():
    clear()
    print(f"you won with {player1.heath} health")
def lose():
    clear()
    print("you lost and died")

name = input("What is your name?")
player1 = Player(name, 20, 12, 12, False)
enimy1 = Enimy("bird", 1)
enimy2 = Enimy("fuse layer", 1)

Diolague = [f"Hello {player1.name}, welcome to your new backyard. Your backyard is full of a couple things, a big shed that looks a bit creepy, a random lever sticking out of the ground near the shed, and a big tree that looks very old."]
options = [F"{player1.name} you have three options.", "1: you could climb the tree", "2: you could pull the lever", "3: you could go into the shed,." ]
choice_Diolague = ["you climb up the tree and see a bird who instantly attacks", "Your health is dwindling do you want to fight back y/n"]
time.sleep(1)
print(f"Hello {player1.name} have fun playing my game!")
time.sleep(1)

import time
typewriter_print(Diolague[0], delay=0.005)
print(options[0])
print(options[1])
print(options[2])
print(options[3])
choice = input("Pick 1, 2 or 3 ")
if choice == ("1"):
    clear()
    bar()
    typewriter_print(choice_Diolague[0], delay=0.005)
    enimy1.attack()
    bar()
    typewriter_print(choice_Diolague[1], delay=0.005)
    a = input()
    if a ==("y"):
        print("you attack and win")
        time.sleep(1)
        win()
    else:
        print("you die")
        lose()
        player1.heath = 0
elif choice == ("2"):
    print("you pull the lever and the shed blows you up. You are hit by the the wall of the shed.")
    time.sleep(1)
    player1.heath = 0
    lose()
elif choice == ("3"):
    print("you explore the shed and find it filled full of explosives do you want to invenstigate y/n")
    a = input()
    if a ==("y"):
        print("you find that they all go to a common fuse witch goes underground. You find a man putting the last of the fuse down")
        enimy2.attack()
        bar()
        a = input("would you like to fight back")
        if a ==("y"):
            print("you attatack and defeat this man")
            time.sleep(1)
            win()
        else:
            enimy2.attack()
            time.sleep(1)
            player1.heath = 0
            lose()

        
    else:
        print("you go inside and cower the man comes in")
        enimy2.attack()
        bar()
        enimy2.attack()
        time.sleep(1)
        player1.heath = 0
        lose()
else:
    print("pick a vailid answer")
