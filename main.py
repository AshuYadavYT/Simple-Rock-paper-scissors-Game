# A Simple RPC Game Made in Python ^_^
import time, random

rock = "r"
paper = "p"
scissors = "s"
rpc_all = [rock, paper, scissors]

emo_rock = "🗻"
emo_paper = "📃"
emo_scissors = "✂"
emo_win = "🎊"

def main():
    print("Welcome to Rock, Paper and Scissors game")
    time.sleep(2)
    select = input("Select your option: ")
    rpc = random.choice(rpc_all)
    
    if select == ".exit": #for Stopping Game
        print("👍| Game Stopped!")
        exit() 

    elif select == rock:
        print(f"You choose Rock {emo_rock}")
        time.sleep(1)
        if rpc == scissors:
            print(f"I choose Scissors {emo_scissors} , You Win! {emo_win}")
        elif rpc == paper:
            print(f"I choose Paper {emo_paper}, You Lost!")
        elif rpc == rock:
            print("I choose Rock too, It's draw let's battle again!✨")
            time.sleep(2)
            main()

    elif select == paper:
        print(f"You choose Paper {emo_paper}")
        time.sleep(1)
        if rpc == scissors:
            print(f"I choose Scissors {emo_scissors} , You Lost")
        elif rpc == paper:
            print(f"I choose Paper too, It's draw let's battle again!")
            time.sleep(2)
            main()
        elif rpc == rock:
            print(f"I choose Rock {emo_rock}, You Win {emo_win}")

    elif select == scissors:
        print("You choose Scissors")
        time.sleep(1)
        if rpc == scissors:
            print("I choose Scissors too, It's draw let's battle again!")
            time.sleep(2)
            main()
        elif rpc == rock:
            print(f"I choose Rock {emo_rock}, You Lost")
        elif rpc == paper:
            print(f"I choose Paper {emo_paper}, You Win {emo_win}")

    else:
        print("❌| Invaild Option!")
        time.sleep(2)
        main()

main()