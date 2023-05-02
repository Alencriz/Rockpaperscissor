import random

def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Its a tie !"
    elif player_choice == "rock":
        if computer_choice == 'paper':
            return "you loose!"
        else:
            return "you win!"
    elif player_choice == "paper":
        if computer_choice == 'sicssors':
            return "you loose"
        else:
            return "you win!"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "you loose!"
        else:
            return "You Win!"
    else:
        return "invalid input. Please try again."
    choices = ['rock','papper','scissors']
    
    player_choice = input("Enter your Choice(rock/paper/scissors):").lower()
    computer_choice = random.choice(choices)
    result = play_game(player_choice, computer_choice)
    print(f"you chose{player_choice}, and the computer chose{computer_choice}.{result}")
    play_again = True
    while play_again:
        choice = input("Do you want to play again?(y/n):")
        if choice.lower() == 'n':
            play_again = False
            print("thanks for playing Rock Paper Scissors")