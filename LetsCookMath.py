print("Congratulations. You have found a new job and recieved a few pa checks. You now have 3 options. 1, 2, or 3. Choose wisely...")
print("")

game_loop = True 

def start_text_printer():
    print("1. Spend it to buy math")
    print("")
    
    print("2. Use money to make a math lab")
    print("")
    
    print("3. Use money to buy math lab")
    print("")
pass

def start_text_choice_getter():
    return int(input("What do you pick? "))
pass


start_text_printer()
x = int(start_text_choice_getter())


if (x == int(1)):
    print("")
    print("You bought math, and used it which made your boss get mad since you are late to work. He demotes you, steals your money and kills all of your loved ones. What will you do next? ")
    print("")
    print("4. Pull out your pistol and attempt to kill the boss right then ")
    print("")
    print("5. Accept your defeat and plan out your revenge ")
    if (int(input()) == int(4)):
        print("Before you were able to pull our your gun, your Boss had slight of hand and shot you with his gun. You die. ")
    else:
        print("You leave the boss be and plan out your revenge. You hire henchmen so that they can help take revenge on the boss. ")
        print("You decide to purchase a bomb that will blow the building that your boss resides at. You have two final choices. ")
        print("")
        print("6. Overcome with grief, you decide to take your life along with the boss. You will step into the building and choose to go with boss. ")
        print("")
        print("7. You are overcome with grief, but still decide to stay outside of the building to see for yourself that the building and your boss goes out. ")
          
        if (int(input()) == int(6)):
          print("")
          print("You did it. Your henchmen successfully trap your boss inside and the bomb detonates. You die along with the boss but at least that piece of shit is dead, right? ")
        else:
          print("")
          print("Your boss figures out about your plan when you don't come into the building. He sneakily maneuevers his way out of the building and shoots you right in the head before you can say anything. You die. ")
elif(x == int(2)):
    print("")
    print("Using your money, you made a math lab and the Boss approved. He promoted you and have you a salary bonus. What will you do next? ")
    print("")
    print("8. Celebrate with boss and have a dinner party ")
    print("")
    print("9. Use money to buy henchmen. ")
    print()
    if (int(input()) == int(8)):
        print("While at the party, your boss poisoned the food that you ate. You collapsed on the ground and died. GAME OVER")
    else:
        print("Using money to hire henchmen, your boss finds out you have done this behind his back and he gets mad and demotes you. ")

        print("")
        print("10. Choose - Using your henchmen, you trap your boss in the building. You them bomb it which kills you and your boss ")
        print("")
        print("11. Choose - You fire your henchmen  ")
          
        if (int(input()) == int(10)):
          print("")
          print("GAME OVER")
        else:
          print("")
          print("Boss accepts your apology and re-promotes you. You both continue to build a math empire and conquer. THE END ")
elif (x == int(3)):
    print("")
    print("You used the money to buy a math lab. It was very successful because it's state-of-the-art equipment. What will you do next? ")
    print("")
    print("12. You find a partner to help you cook. ")
    print("")
    print("13. you cook pure math that sells at $65,000 per pound. ")
    if (int(input()) == int(12)):
        print("Your partner betrays you and steals all of the equipment. He then shoots you in the head. You die. ")
    else:
        print(" You sell 17 pounds of math and get $1,105,000. ")
        print("")
        print("14. Split this money with your boss and continue to cook more math")
        print("")
        print("15. Take all the money and run away. You flee the country. ")
          
        if (int(input()) == int(14)):
          print("")
          print(" Your boss is very proud of your hard work and upgrades all of your equipment. You both succeed in your Math Empire ")
        else:
          print("")
          print("You fled the country and went to Morocco. You live there for the rest of your life and enjoy the people, the food, and the girls.")
pass
