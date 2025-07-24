import random

choices = ('r', 'p', 's')
emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
wanna_continue = ('y', 'n')

while True:
    user_choice = input("Rock, Paper, Scissors ('r','p','s') : ").lower()

    if user_choice not in choices:
        print("choose from above")
        continue

    computer_choice = random.choice(choices)

    print(f"you chose {emojis[user_choice]}")
    print(f'computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("Tie!")

    elif ((user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p')):
        print("You Win")
    else:
        print("You Lose")

    should_continue = input("continue (y/n)?").lower()
    if should_continue == 'n':
        break
