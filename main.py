# functions
def wolf():
    user_choice_wolf = input(f"""while you were casually going through the game, a wild wolf decided to ruin your day!
    The wolf sure does look angry and ready to attack, what do you want to do? Escape or attack?
    Please enter escape if you want to run or attack if you want to face the wolf: """)
    while user_choice_wolf not in ["escape", "attack"]:
        print("Invalid value, please enter a relevant one.")
        user_choice_wolf = input("while you were casually going through the game, "
                                 "a wild wolf decided to ruin your day!"
                                 "The wolf sure does look angry and ready to attack, what do you want to do? Escape "
                                 "or attack? "
                                 "Please enter escape if you want to run or attack if you want to face the wolf: ")

    if user_choice_wolf == "attack":
        return print(f"You killed the wolf, you have gotten quite stronger")
    elif user_choice_wolf == "escape":
        return print("You successfully got away from the wolf, you got significantly faster!")
    else:
        print("Invalid value, please enter a relevant one.")


def goblin():
    user_choice_goblin = input(f"""You have encountered a random goblin!, Its not here for your money, its here for 
    your life! I don't think you have more options rather than escape and attack, make your move {user_name}! Please 
    enter a valid option 
     escape or attack: """)
    while user_choice_goblin not in ["escape", "attack"]:
        print("Invalid value, please enter a relevant one.")
        user_choice_goblin = input(f"""You have encountered a random goblin!, Its not here for your money, its here 
        for your life! I don't think you have more options rather than escape and attack, make your move {user_name}! 
        Please enter a valid option 
     escape or attack: """)
    if user_choice_goblin == "attack":
        return print("You have successfully killed a goblin. You have gotten stronger and faster!")
    elif user_choice_goblin == "escape":
        return print("You successfully outran that goblin! You have gotten faster!")
    else:
        return print("Invalid value, please enter a relevant one.")


def ogre():
    user_choice_ogre = input(f"""You have stumbled upon an ogre! this beast is tall and vicious, but lucky you, 
    its sleeping right now, you have a choice to kill it silently or evade it slowly? what will you do? kill or evade? 
    Please enter a valid choice:  """)
    while user_choice_ogre not in ["evade", "kill"]:
        print("Invalid value, please enter a relevant one.")
        user_choice_ogre = input(f"""You have stumbled upon an ogre! this beast is tall and vicious, but lucky you, 
        its sleeping right now, you have a choice to kill it silently or evade it slowly? what will you do? kill or 
        evade? Please enter a valid choice:  """)
    if user_choice_ogre == "kill":
        return print("You silently killed the ogre with your sword, you have gotten stronger!")
    elif user_choice_ogre == "evade":
        return print("You successfully evaded the ogre! Your intellect has risen!")
    else:
        return print("Invalid value, please enter a relevant one.")


def orc():
    user_choice_orc = input(f"""You ran into an orc! These beasts are strong but quite dumb, if you wish to fight it, 
    you should fight it with with intelligence. Or you could wish to evade it too. What's your choice? attack or 
    evade?: """)
    while user_choice_orc not in ["attack", "evade"]:
        print("Invalid value, please enter a relevant one.")
        user_choice_orc = input(f"""You ran into an orc! These beasts are strong but quite dumb, if you wish to fight 
        it, you should fight it with with intelligence. Or you could wish to evade it too. What's your choice? attack 
        or evade?: """)
    if user_choice_orc == "attack":
        return print("You barely defeated the orc! Your intellect and strength have risen")
    elif user_choice_orc == "evade":
        return print("You barely outran the orc! that beast sure was fast! Your agility has risen.")
    else:
        print("Invalid value, please enter a relevant one.")


def mini_orc():
    user_choice_mini_orc = input(f"""You ran into an orc! But this one is a bit small comparing to an orc. Orcs are 
    strong but dumb, If you wish to fight it, fight it with intelligence! Or you could choose to evade it as well. 
    attack or evade?: """)
    while user_choice_mini_orc not in ["attack", "evade"]:
        print("Invalid value, please enter a relevant one.")
        user_choice_mini_orc = input(f"""You ran into an orc! But this one is a bit small comparing to an orc. Orcs 
        are strong but dumb, If you wish to fight it, fight it with intelligence! Or you could choose to evade it 
        as well. attack or evade?: """)
    if user_choice_mini_orc == "attack":
        return print(
            "You fought the mini orc, it was pretty strong but you came out on top. Your strength and intellect have "
            "risen.")
    elif user_choice_mini_orc == "evade":
        return print("You successfully  outran the mini orc! It was fast but i suppose you were faster")
    else:
        return print("Invalid value, please enter a relevant one.")


def royal_guard_1():
    guess_count1 = 1
    user_choice_guard1 = input(f"""You encountered the first guard, good luck fighting him!
    Im tall when im young, and im short when im old. What am I? 
     """)
    while user_choice_guard1 not in ["Candle", "candle", "a candle"]:
        guess_count1 += 1
        print(f"Wrong answer! {guess_count1} try gone. You have 5 in total")
        user_choice_guard1 = input("Try again. ")
        if guess_count1 == 5:
            return print("You have died trying to defeat a royal guard. Game Over.")
        exit()
    else:
        return print("You killed a royal guardian orc in your ", guess_count1, "th try!")


def royal_guard_2():
    guess_count2 = 1
    user_choice_guard2 = input(f"""Now you have to kill the 2nd orc guardian. Good luck {user_name}!
    I’m where yesterday follows today and tomorrow is in the middle. What am I?  
     """)
    while user_choice_guard2 not in ["dictionary", "Dictionary", "a dictionary"]:
        guess_count2 += 1
        print(f"Wrong answer! {guess_count2} try gone. You have 5 in total.")
        user_choice_guard2 = input("Try again. ")
    if guess_count2 == 5:
        return print("You have died trying to defeat a royal guard. Game over.")
    else:
        return print("You killed the 2nd royal guardian orc in your", guess_count2, "th try!")


def royal_guard_3():
    guess_count3 = 1
    user_choice_guard3 = input(f"""The third guardian orc is coming running towards you! good luck fighting this orc!
    I’m a god, a planet, and I measure heat. What am I? 
    """)
    while user_choice_guard3 not in ["Mercury" "mercury"]:
        guess_count3 += 1
        print(f"Wrong answer! {guess_count3} try gone, you have 5 in total.")
        user_choice_guard3 = input("Try again. ")
    if guess_count3 == 5:
        return print("You died trying to defeat a royal guard. Game over.")
    else:
        return print("You kill the 3rd royal guardian orc in your", guess_count3, "th try!")


def royal_guard_4():
    guess_count4 = 1
    user_choice_guard4 = input(f"""The fourth guardian orc is ready to fight you with all his strength. Good luck! 
    The more you take, the more you leave behind. What am I? 
    """)
    while user_choice_guard4 not in ["footsteps", "Footsteps", "Your footsteps"]:
        guess_count4 += 1
        print(f"""Wrong answer! {guess_count4} try gone. You have 5 in total.""")
        user_choice_guard4 = input("Try again. ")
    if user_choice_guard4 == 5:
        print("You died trying to fight a royal guard. Game over.")
        exit()
    else:
        print(f"You defeated the 4th royal guardian orc in your {guess_count4}th try!")


def royal_guard_5():
    guess_count5 = 1
    user_choice_guard5 = input(f"""Prepare to take on the 5th royal guard! I am the beginning of everything, the end 
    of everywhere. I’m the beginning of eternity, the end of time and space. What am I? """)
    while user_choice_guard5 not in ["e", "letter e", "the letter e"]:
        guess_count5 += 1
        print(f"Wrong answer! {guess_count5} try gone. You have 5 in total.")
        user_choice_guard5 = input("Try again. ")
    if guess_count5 == 5:
        return print("You died trying to defeat a royal guard. Game over.")
    else:
        return print(f"You killed the 5th royal guard in your {guess_count5}th try!")


def royal_guard_6():
    guess_count6 = 1
    user_choice_guard6 = input(
        f"""One last guard left, then you can reach the orc lord. I pray for your victory {user_name}! 
    If you have me, you want to share me. If you share me, you haven’t got me. What am I? 
    """)
    while user_choice_guard6 not in ["Secret", "secret", "a secret"]:
        guess_count6 += 1
        print(f"Wrong answer! {guess_count6} try gone. You have 5 in total.")
        user_choice_guard6 = input("Try again. ")
    if guess_count6 == 5:
        return print("You died trying to defeat a royal guard. Game over.")
    else:
        return print(f"You killed the last royal guard in your{guess_count6}th try! Now you have to face the Orc lord!")


def orc_lord():
    # missing guess counter
    guesses = 0
    user_choice_lord = input(f"""The Orc lord accepts your duel request. He is known as the most powerful being in 
    the the terminal word. May you be victorious {user_name} 
    If you have me, you want to share me. If you share me, you haven’t got me. What am I? 
     """)
    while user_choice_lord not in ["map", "Map", "A map"]:
        print(f"Wrong answer! {guesses} try gone. You only have 3 total tries.")
        user_choice_lord = input("Try again. ")
    if guesses == 3:
        return print("You have failed to get out of the terminal world. Game over.")
    else:
        return print(f"Congratulations {user_name}!You have completed the game. Thank you for playing <3")


# functions end

# story start
user_name = (input("""Hello user, Welcome to Command Line Chronicles, What is your name? """))

user_role = (input(f"""Welcome {user_name} to the world of the Terminal! Here you will have to choose a role between 
a warrior, an adventurer, and a researcher.what role do you want? a warrior? an adventurer? or a researcher? Enter a 
valid role: """))

while user_role not in ["warrior", "adventurer", "researcher"]:
    print("You entered an invalid role, please enter a valid role")
    user_role = str(input(f"""Welcome {user_name} to the world of the Terminal! Here you will have to choose a role
between a warrior, an adventurer, and a researcher. The role u pick will effect your player stats. What player stats
you ask? now enough talk, what role do you want? a warrior? an adventurer? or a researcher? Enter a valid role: """))

# role pick
if user_role == "warrior".lower():
    print(f"You picked the warrior role!")
elif user_role == "adventurer".lower():
    print(f"You picked the adventurer role!")
elif user_role == "researcher".lower():
    print(f"You picked the researcher role!")
else:
    while user_role not in ["warrior", "adventurer", "researcher"]:
        print("You entered an invalid role, please enter a valid role")

print(f"Very well {user_name}, your ready to start your journey in the terminal world. Good luck getting out of it!")

goblin()

wolf()

print("""It has been a month since you have been in the terminal world, you have mostly fought wolves and goblins. 
you stayed as a traveler in villages and while you conversed with villagers, you found out other people have also 
gotten randomly summoned in the terminal world. The villagers call them 'fallen heroes' and they still pray that one 
day they will get freed.""")

print("""

You have gotten a sword as a gift from the villagers!

 """)

print("""3 months have passed, you have been traveling and traveling trying to free the terminal world.

""")

print("""6 months have passed, you still haven't found anything useful, you are slowly starting to loose hope

 """)

print("""It has been a whole year, yet you failed to find anything meaningful, you clueless on why you're still trying 
to free this world 

""")

print(f"""Jackpot! while you were traveling you found an orc castle! This might just be your ticket out of the 
terminal world. 

""")

print(f"""You see a lot of mini orcs, wolves, goblins and ogres defending the castle. Get ready for a massive fight 

""")

ogre()
wolf()
wolf()
goblin()
mini_orc()
wolf()
mini_orc()

print(f"""You cleared the the defenders. You head inside the orc castle to the throne room, and then you see 6 big 
orcs and then another orc wearing a crown. Your mission is to kill the orc in the crown. To get to him, you need to 
fight his royal guards """)

royal_guard_1()
royal_guard_2()
royal_guard_3()
royal_guard_4()
royal_guard_5()
royal_guard_6()
orc_lord()
