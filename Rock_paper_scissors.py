import random as rd
play=input("Do you want to play 'Rock/Paper/Scissors? ")
if play != "yes":
    quit()
computer_wins=0
user_wins=0
option=["rock","paper","scissors"]
while True:
    option_inp=input("Choose one of them option 'Rock/paper/scissors' or 'Q' to quit: ").lower()
    if option_inp=="q":
        print("Ok thanks for your time!")
        break
    elif option_inp not in option : 
        print("Kindly Choose appropiate option!")
        continue
    computer_pick=rd.choice(option)
    print(F"Computer chose '{computer_pick}'")
    if option_inp == "rock" and computer_pick == "scissors":
        print("You won this time!")
        user_wins = user_wins + 1
        continue
    elif option_inp=="paper" and computer_pick == "rock" :
        print("You won this time!")
        user_wins = user_wins + 1
        continue
    elif option_inp == "scissors" and computer_pick == "paper":
        print("You won this time!")
        user_wins = user_wins + 1
        continue
    elif option_inp == computer_pick :
        print("Game is Draw")
        continue
    else:
        print("You lost Computer won!!")
        computer_wins = computer_wins+1
        continue
print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")
print("Thank you for playing this game")
print("Good Byy")
