def roll_dice():
    import random
    mini=1
    maxi=6

    roll_again="yes"
    while roll_again == "yes" or roll_again=="y":
        print("Rolling the dice..")
        print("The value is: ",random.randint(mini,maxi))
        roll_again=input("Do you want to roll again? ")
        
print("      VIRTUAL DICE      ")
a=input("Do you want to roll the dice? Y/N: ")
if a=="Y":
    roll_dice()

    
