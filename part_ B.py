import random

def guess_number_game():
    """Play the number guessing game."""
    secret, attempts, max_attempts = random.randint(1, 100), 0, 10
    print(f"\n=== Guess the Number (1-100) ===\nYou have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            if not (1 <= guess <= 100): raise ValueError
            attempts += 1
            if guess == secret: return print(f"🎉 Correct! Guessed in {attempts} tries.")
            print(f"{'Too low' if guess < secret else 'Too high'}! Attempts left: {max_attempts - attempts}")
        except ValueError:
            print("Enter a valid number between 1 - 100.")

    print(f"\nGame Over! The number was {secret}.")

def rock_paper_scissors():
    """Play Rock, Paper, Scissors."""
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    player_score = computer_score = 0

    while True:
        print(f"\nScore - You: {player_score} | Computer: {computer_score}")
        player = input("Choose (rock/r, paper/p, scissors/s): ").lower()
        if player not in choices: print("Invalid choice!"); continue

        player, computer = choices[player], random.choice(list(choices.values()))
        print(f"Computer: {computer} | You: {player}")

        if player == computer:
            print("It's a DRAW!")
        elif (player, computer) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
            print("You WIN!"); player_score += 1
        else:
            print("Computer WINS!"); computer_score += 1

        if input("Play again? (y/n): ").lower() != 'y':
            print(f"\nFinal Score - You: {player_score} | Computer: {computer_score}")
            print("🎉 You WON the series!" if player_score > computer_score else "Computer won the series!" if player_score < computer_score else "It's a tie!")
            break

def main():
    """Main menu for game selection."""
    games = {'1': ("Guess Number Game", guess_number_game), '2': ("Rock Paper Scissors", rock_paper_scissors), '3': ("Exit", exit)}
    
    while True:
        print("\n" + "="*30 + "\nWelcome to Game Center!\n" + "="*30)
        print("\n".join(f"{k}. {v[0]}" for k, v in games.items()))
        games.get(input("\nEnter choice: "), (None, lambda: print("Invalid choice")))[1]()

if __name__ == "__main__":
    main()
