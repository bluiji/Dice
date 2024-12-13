import random

def roll_dice(num_dice=1):
    """Simulates rolling dice. Accepts the number of dice to roll."""
    if num_dice not in [1, 2]:
        raise ValueError("You can only roll 1 or 2 dice.")
    
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Simulator!")
    
    while True:
        try:
            num_dice = int(input("Would you like to roll 1 or 2 dice? (Enter 1 or 2): "))
            results = roll_dice(num_dice)
            print(f"You rolled: {', '.join(map(str, results))}")
            
            if num_dice == 2:
                print(f"Total: {sum(results)}")
            
            play_again = input("Would you like to roll again? (yes/no): ").strip().lower()
            if play_again not in ["yes", "y"]:
                print("Thanks for playing! Goodbye!")
                break
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
