import random

while True:
    print("=====Rock Paper Scissors: The Python Game=====")
    print("\n")

    name = input("Player please enter you name:\n")
    print("\n")


    myItem = input("Enter Either Rock Paper or Scissors:\n")

    if myItem != "Rock" or myItem != "Paper" or myItem != "Scissors":
        print("Are you Ok!! I said enter rock paper or scissors")
        

    #Computer's Choices
    computerItem = random.randint(1,3)
    if computerItem == 1:
        computerItem = "Rock"
        print(f"Computer chooses {computerItem}...")
    if computerItem == 2:
        computerItem = "Paper"
        print(f"Computer chooses {computerItem}...")
    if computerItem == 3:
        computerItem = "Scissors"
        print(f"Computer chooses {computerItem}...")


    if myItem == computerItem:
        print("Try Again!! You and the CPU picked the same thing")

    #How I can loose to the CPU
    if myItem == "Rock" and computerItem == "Paper":
        print("[Paper covers Rock]")
        print("CPU WINS!!!")
    if myItem == "Paper" and computerItem == "Rock":
        print("[Paper covers Rock]")
        print(f"{name} WINS!!!")

    if myItem == "Scissors" and computerItem == "Rock":
        print("[Rock Smashes Scissors]")
        print("CPU WINS!!!")
    if myItem == "Rock" and computerItem == "Scissors":
        print("[Rock smashes Scissors]")
        print(f"{name} WINS!!!")

    if myItem == "Paper" and computerItem == "Scissors":
        print("[Scissors cut Paper]")
        print("CPU WINS!!!")
    if myItem == "Scissors" and computerItem == "Paper":
        print("[Scissors cut Paper]")
        print(f"{name} WINS!!!")
    exit = input("\nWould you like to play game? Y/N")
    if exit=="N":
        break