import random

def guess_number_game():
    print("\n=== Guess the Number Game ===")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            if guess == secret_number:
                print(f"\nCongratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
            print(f"Attempts remaining: {max_attempts - attempts}")
            
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nGame Over! The number was {secret_number}")

def rock_paper_scissors():
    print("WELCOME TO - Rock Paper Scissors Game" )
    choices = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors',
        'rock': 'rock',
        'paper': 'paper',
        'scissors': 'scissors'
    }
    player_score = 0
    computer_score = 0
    
    while True:
        print(f"\nScore - You: {player_score} Computer: {computer_score}")
        print("\nChoose: rock(r), paper(p), or scissors(s)")
        player_input = input("Your choice: ").lower()
        
        if player_input not in choices:
            print("Invalid choice! Please use 'r', 'p', 's' or 'rock', 'paper', 'scissors'")
            continue
        
        player_choice = choices[player_input]
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"\nComputer chose: {computer_choice}")
        print(f"You chose: {player_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
            
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print(f"\nFinal Score - You: {player_score} Computer: {computer_score}")
            if player_score > computer_score:
                print("Congratulations! You won the series!")
            elif player_score < computer_score:
                print("Computer won the series!")
            else:
                print("The series was a tie!")
            break

def main():
    while True:
        print("\n" + "="*40)
        print("Welcome to the Game Center!")
        print("="*40)
        print("\nSelect a game:")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors")
        print("3. Exit")
        print("="*40)
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
        if input("\nWould you like to try another game? (y/n): ").lower() != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()