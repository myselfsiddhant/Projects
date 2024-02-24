import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    comp = random.choice(['rock', 'paper', 'scissor'])

    if user == comp:
        print(f"Computer's choice was {comp}")
        return "It's a tie"

    if is_win(user, comp):
        print(f"Computer's choice was {comp}")
        return 'You won!'

    return 'You lost!'
    

def is_win(player, opponent):
    if (player == 'r' and opponent == 'scissor') or (player == 's' and opponent == 'paper') \
        or (player == 'p' and opponent == 'rock'):
        return True

print(play())
