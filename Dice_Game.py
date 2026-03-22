# Fun to code Project_1 for Kaito
# 1.1 Make your own nickname generator!

import random


print("*********************************************")
print("🐶 Kaito-Kun, Welcome to Fun Code With Dad !")
print("*********************************************")
print()
print("Let's make your cool nickname first!")
real_name = input("What's your name? ")
fav_animal = input("Favorite animal? ")

nickname = real_name[:3] + " " + fav_animal
print("Your cool nickname is: " + nickname + "!")

def print_win_art():
    """Print a fun victory graphic with ASCII art"""
    print("\n🎉🎉🎉  YOU WIN!  🎉🎉🎉")
    print("┏━━━━━━━━━━━━━━━━━━┓")
    print("┃  ┌─────────────┐  ┃")
    print("┃  │ 🏆 VICTORY 🏆 │  ┃")
    print("┃  └─────────────┘  ┃")
    print("┃                    ┃")
    print("┃  🎊🥳🎊  GREAT JOB  🎊🥳🎊  ┃")
    print("┗━━━━━━━━━━━━━━━━━━┛\n")

def play_dice_game():
    """Core logic of the dice game (single round)"""
    print("\n🎲 Welcome to the Dice Game!")
    # First dice roll: generate a random integer between 1 and 6
    first_roll = random.randint(1, 6)
    print(f"You rolled: {first_roll} on your first try\n")

    # Flag to check if the player lost (for replay prompt)
    is_lost = False

    # Judge the result of the first dice roll (updated rules)
    if 1 <= first_roll <= 2:  # 1-2: lose
        print("❌ You lose! Better luck next time!\n")
        is_lost = True
    elif 3 <= first_roll <= 4:  # 3-4: roll again
        print(f"🎲 You rolled a {first_roll}, need to roll again!")
        # Second dice roll
        second_roll = random.randint(1, 6)
        print(f"You rolled: {second_roll} on your second try\n")
        # Judge the result of the second dice roll
        if 1 <= second_roll <= 2:
            print("❌ You lose! Better luck next time!\n")
            is_lost = True
        elif 5 <= second_roll <= 6:
            print_win_art()  # Call victory graphic
        elif 3 <= second_roll <= 4:
            # Additional handling: if rolling 3/4 again, keep rolling until non-3/4
            print(f"Rolled a {second_roll} again, keep rolling!\n")
            while True:
                extra_roll = random.randint(1, 6)
                print(f"You rolled again: {extra_roll}")
                if extra_roll not in [3, 4]:  # Stop when roll 1/2 or 5/6
                    break
            if 1 <= extra_roll <= 2:
                print("❌ You lose! Better luck next time!\n")
                is_lost = True
            else:
                print_win_art()  # Call victory graphic
    elif 5 <= first_roll <= 6:  # 5-6: win
        print_win_art()  # Call victory graphic

    return is_lost

def main():
    """Main game loop with replay prompt"""
    while True:
        # Play a single round and check if player lost
        lost = play_dice_game()
        
        # Only ask for replay if player lost
        if lost:
            while True:
                # Get player's choice (case-insensitive)
                replay = input("Do you want to play again? (Y/N): ").strip().upper()
                if replay in ["Y", "N"]:
                    break
                else:
                    print("Invalid input! Please enter Y (Yes) or N (No).")
            
            if replay == "N":
                print("\n👋 Thanks for playing! See you next time!\n")
                break  # Exit the game loop
            # If replay == "Y", loop continues (play again)
        else:
            # If player won, end the game directly
            print("👋 Hope you had fun! Come back soon!\n")
            break

# Run the game when the script is executed directly
if __name__ == "__main__":
    main()