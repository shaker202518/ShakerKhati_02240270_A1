def is_prime(n):
    "Check if a number is prime."
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    "Calculate sum of prime numbers in given range."
    try:
        start, end = int(start), int(end)
        if start > end:
            start, end = end, start
        primes_sum = sum(num for num in range(start, end + 1) if is_prime(num))
        return f"Sum of primes between {start} and {end}: {primes_sum}"
    except ValueError:
        return "Error: Please enter valid integers"

def length_converter(value, unit):
    "Convert between meters and feet."
    try:
        value = float(value)
        if unit.upper() == 'M':
            return f"{value} meters = {round(value * 3.28084, 2)} feet"
        elif unit.upper() == 'F':
            return f"{value} feet = {round(value / 3.28084, 2)} meters"
        else:
            return "Error: Invalid unit (use 'M' for meters or 'F' for feet)"
    except ValueError:
        return "Error: Please enter a valid number"

def count_consonants(text):
    "Count consonants in a string."
    if not isinstance(text, str):
        return "Error: Please enter a valid string"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = sum(1 for char in text.lower() if char in consonants)
    return f"Number of consonants: {count}"

def min_max_finder():
    "Find minimum and maximum numbers from user input."
    try:
        count = int(input("How many numbers would you like to enter? "))
        if count <= 0:
            return "Error: Please enter a positive number"
        
        numbers = []
        for i in range(count):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        
        return f"Smallest: {min(numbers)}, Largest: {max(numbers)}"
    except ValueError:
        return "Error: Please enter valid numbers"

def palindrome_checker(text):
    "Check if a string is a palindrome."
    if not isinstance(text, str):
        return "Error: Please enter a valid string"
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return f"Is palindrome: {cleaned_text == cleaned_text[::-1]}"

def word_counter(filename):
    "Count specific words in a text file."
    target_words = ["the", "was", "and"]
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            counts = {word: text.split().count(word) for word in target_words}
            return "\n".join(f"'{word}': {count}" for word, count in counts.items())
    except FileNotFoundError:
        return "Error: File not found"

def main():
    while True:
        print("\nSelect a function (1-7):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit program")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            start = input("Enter start range: ")
            end = input("Enter end range: ")
            print(sum_of_primes(start, end))

        elif choice == '2':
            value = input("Enter value: ")
            unit = input("Enter unit (M/F): ")
            print(length_converter(value, unit))

        elif choice == '3':
            text = input("Enter a string: ")
            print(count_consonants(text))

        elif choice == '4':
            print(min_max_finder())

        elif choice == '5':
            text = input("Enter a string: ")
            print(palindrome_checker(text))

        elif choice == '6':
            filename = input("Enter filename: ")
            print(word_counter(filename))

        elif choice == '7':
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        if input("\nWould you like to try another function? (y/n): ").lower() != 'y':
            print("Thank you for using the program!")
            break

if __name__ == "__main__":
    main()