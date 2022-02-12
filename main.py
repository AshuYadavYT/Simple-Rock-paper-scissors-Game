# A Simple RPC Game Made in Python
import time, random

rock = "r"
paper = "p"
scissors = "s"
rpc_all = [rock, paper, scissors]

def main():
    print("Welcome to Rock, Paper and Scizors game")
    select = input("Select your option: ")
    rpc = random.choice(rpc_all)

    if select == rock:
        print("You choose Rock")
        time.sleep(1)
        if rpc == scissors:
            print("I choose Scissors, You Win!")
        elif rpc == paper:
            print("I choose Paper, I Win")
        elif rpc == rock:
            print("I choose Rock too, It's draw let's battle again!")
            time.sleep(2)
            main()

    elif select == paper:
        print("You choose Paper")
        time.sleep(1)
        if rpc == scissors:
            print("I choose Scissors, You Lost")
        elif rpc == paper:
            print("I choose Paper too, It's draw let's battle again!")
            time.sleep(2)
            main()
        elif rpc == rock:
            print("I choose Rock, You Win")

    elif select == scissors:
        print("You choose Scissors")
        time.sleep(1)
        if rpc == scissors:
            print("I choose Scissors too, It's draw let's battle again!")
            time.sleep(2)
            main()
        elif rpc == rock:
            print("I choose Rock, You Lost")
        elif rpc == paper:
            print("I choose Paper, You Win")

    elif select == "exit": #for Stopping Game
        print("Game Stopped!")
        exit() 

    else:
        print("Invaild Option!")
        time.sleep(2)
        main()

main()