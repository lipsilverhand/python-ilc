import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
         (_______ 
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player >= 3 or player < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game[player])

    bot = random.randint(0, 2)
    print("Bot chose:")
    print(game[bot])


    if player == 0 and bot == 2:
        print("You win!")
    elif bot == 0 and player == 2:
        print("You lose")
    elif bot > player:
        print("You lose")
    elif player > bot:
        print("You win!")
    elif bot == player:
        print("It's a draw")


