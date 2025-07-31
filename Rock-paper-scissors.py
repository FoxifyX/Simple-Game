import random
a = True

while a:
    print("#---Rule---#\nRock = r\nPaper = p\nScissors = s\n------------")

    computer = random.randint(1,3)
    user = input("What u want to select?[r/p/s]: ")

    # rock = 1
    # paper = 2
    # sessior = 3


    dict = {"r" : 1, "p" : 2, "s" : 3}
    rev_dect = {1 : "rock", 2 : "paper", 3 : "scissors"}
    you = dict[user]

    print("-------------------")
    print(f"Computer has selected {rev_dect[computer]}")
    print(f"You have selected {rev_dect[you]}")
    print("-------------------")

    if(computer == you):
        print("⚠️ Match Draw !\n")
    else:
        if(computer == 1 and you == 2):
            print("✅ You Win!\n")
        elif(computer == 1 and you == 3):
            print("❌ You Lose!\n")
        elif(computer == 2 and you == 1):
            print("❌ You Lose!\n")
        elif(computer == 2 and you == 3):
            print("✅ You Win!\n")
        elif(computer == 3 and you == 1):
            print("✅ You Win!\n")
        elif(computer == 3 and you == 2):
            print("❌ You Lose!\n")
        else:
            print("Something went wrong\nTry Again!")


    x = True

    while x:
        
        again = input("Do you want to play again?[Yes/No]: ").strip().lower()

        if again == "yes":
            print("🔄 Continuing...\n")
            x = False
            
        elif again == "no":
            print("✅ Game has exited successfully..")
           
            x = False
            a = False
            break

        else:
            print("⚠️ Select Yes or No")
                