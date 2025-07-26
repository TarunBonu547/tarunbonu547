import random
player=0
comp=0
print("Welcome to the Rock-Paper-Scissor game developed by Tarun")
name = input(("Enter your name : "))
print("Welcome to the game,",name)

while True:
    option = ["Rock","Paper","Scissor"]
    print("If you want to exit then type (exit) in the choice ")
    human = input(f"Enter {name} choice : ").capitalize()
    if(human == "Exit"):
        print("Thank you for playing the game !!🤝")
        break
    while human not in option:
        print(("Invalid Choice : Enter Rock-Paper-Scissor 🪨 📄 ✂"))
        human = input("Enter the choice of human : ").capitalize()
    computer = random.choice(option)
    print("Your choice is ",human)
    print("Choice of computer is",computer)
    if(human == computer):
        print("Game Tie")
    elif((human == "Rock" and computer == "Paper") or (human == "Paper" and computer == "Scissor") or (human == "Scissor" and computer == "Rock")):
        print("Computer Wins")
        comp+=1
    else:
        print(f"{name} wins")
        player+=1
    print(f"Score of {name} is ",player)
    print(f"Score of computer is ",comp)

total_rounds = player + comp
print(f"\nTotal Rounds Played: {total_rounds}")
print(f"Final Score -> {name}: {player}, Computer: {comp}")
if player > comp:
    print(f"🏆 {name} is the overall winner!")
elif comp > player:
    print("🤖 Computer is the overall winner!")
else:
    print("🤝 It's a tie overall!")