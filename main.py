import time
import random

rock = "r"
paper = "p"
scisors = "s"
rpc_all = [rock, paper, scisors]

def main():
    print("Welcome to Rock, Paper and Scizors game")
    select = input("Select your option: ")
    rpc = random.choice(rpc_all)

    if select == rock:
        print("You choose Rock")
        time.sleep(1)
        if rpc == scisors:
            print("I choose Scisors, You Win!")
        elif rpc == paper:
            print("I choose Paper, I Win")
        elif rpc == rock:
            print("I choose Rock too, It's draw let's battle again!")
            time.sleep(2)
            main()

    elif select == paper:
        print("You choose Paper")
        time.sleep(1)
        if rpc == scisors:
            print("I choose Scisors, You Lost")
        elif rpc == paper:
            print("I choose Paper too, It's draw let's battle again!")
            time.sleep(2)
            main()
        elif rpc == rock:
            print("I choose Rock, You Win")

    elif select == scisors:
        print("You choose Rock")
        time.sleep(1)
        if rpc == scisors:
            print("I choose Scisors too, It's draw let's battle again!")
            time.sleep(2)
            main()
        elif rpc == rock:
            print("I choose Rock, You Lost")
        elif rpc == paper:
            print("I choose Paper, You Win")

    elif select == "exit".lower():
        print("Game Stopped!")
        exit()

    else:
        print("Invaild Option!")
        main()

main()