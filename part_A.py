def is_prime(n):
    """Check if a number is prime."""
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def sum_of_primes(start, end):
    """Calculate sum of prime numbers in given range."""
    try:
        start, end = sorted(map(int, [start, end]))
        return f"Sum of primes between {start} and {end}: {sum(n for n in range(start, end+1) if is_prime(n))}"
    except ValueError:
        return "Error: Please enter valid integers"

def length_converter(value, unit):
    """Convert between meters and feet."""
    try:
        value = float(value)
        return f"{value} {unit.upper()} = {round(value * (3.28084 if unit.upper() == 'M' else 1/3.28084), 2)} {'feet' if unit.upper() == 'M' else 'meters'}"
    except ValueError:
        return "Error: Please enter a valid number"

def count_consonants(text):
    """Count consonants in a string."""
    return f"Number of consonants: {sum(1 for c in text.lower() if c in 'bcdfghjklmnpqrstvwxyz')}" if isinstance(text, str) else "Error: Enter a valid string"

def min_max_finder():
    """Find min and max from user input."""
    try:
        numbers = [float(input(f"Enter number {i+1}: ")) for i in range(int(input("How many numbers? ")))]
        return f"Smallest: {min(numbers)}, Largest: {max(numbers)}"
    except ValueError:
        return "Error: Please enter valid numbers"

def palindrome_checker(text):
    """Check if a string is a palindrome."""
    if isinstance(text, str):
        text = ''.join(c.lower() for c in text if c.isalnum())
        return "Great Job! It's a palindrome." if text == text[::-1] else "No, it's not a palindrome."
    return "Error: Please enter a valid string"

def word_counter(filename):
    """Count specific words in a text file."""
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            return "\n".join(f"'{word}': {text.split().count(word)}" for word in ["the", "was", "and"])
    except FileNotFoundError:
        return "Error: File not found"

def main():
    options = {
        '1': ("Calculate sum of prime numbers", lambda: print(sum_of_primes(input("Start: "), input("End: ")))),
        '2': ("Convert length units", lambda: print(length_converter(input("Value: "), input("Unit (M/F): ")))),
        '3': ("Count consonants", lambda: print(count_consonants(input("Enter text: ")))),
        '4': ("Find min & max numbers", lambda: print(min_max_finder())),
        '5': ("Check palindrome", lambda: print(palindrome_checker(input("Enter text: ")))),
        '6': ("Word Counter", lambda: print(word_counter(input("Enter filename: ")))),
        '7': ("Exit", exit)
    }

    while True:
        print("\n".join([f"{k}. {v[0]}" for k, v in options.items()]))
        options.get(input("\nEnter choice: "), (None, lambda: print("Invalid choice")))[1]()

if __name__ == "__main__":
    main()
