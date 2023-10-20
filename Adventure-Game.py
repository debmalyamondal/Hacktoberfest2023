# Hello I am Debmalya, created this small text based adventure game, hope you will like it.

import time

def display_intro():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest.")
    time.sleep(2)
    print("You can go left or right.")

def choose_path():
    choice = input("Which path will you choose? (left/right): ").lower()
    if choice == "left":
        return "cave"
    elif choice == "right":
        return "river"
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        return choose_path()

def explore_cave():
    print("You enter a spooky cave.")
    time.sleep(2)
    print("Inside the cave, you find a treasure chest.")
    time.sleep(2)
    print("Do you want to open it? (yes/no): ")
    choice = input().lower()
    if choice == "yes":
        print("Congratulations! You found a hidden treasure.")
    else:
        print("You leave the cave.")

def cross_river():
    print("You come across a fast-flowing river.")
    time.sleep(2)
    print("You need to cross it to continue your adventure.")
    time.sleep(2)
    print("Do you swim across or look for a bridge? (swim/bridge): ")
    choice = input().lower()
    if choice == "swim":
        print("You swim across the river and reach the other side safely.")
    elif choice == "bridge":
        print("You find a sturdy bridge and cross the river without any problems.")
    else:
        print("Invalid choice. Please enter 'swim' or 'bridge'.")
        return cross_river()

def deep_cave():
    print("While exploring the forest, you find a hidden path leading to a deep cave.")
    time.sleep(2)
    print("Inside the cave, you discover a labyrinth of tunnels.")
    time.sleep(2)
    print("You can choose to go deeper into the cave or head back to the forest. (deeper/forest): ")
    choice = input().lower()
    if choice == "deeper":
        print("You venture deeper into the cave and find a chamber filled with glowing crystals.")
    else:
        print("You return to the forest.")
        
def meet_wizard():
    print("As you continue your journey, you encounter a wise old wizard.")
    time.sleep(2)
    print("The wizard offers you a choice: he can reveal your future or grant you a magical item. (future/item): ")
    choice = input().lower()
    if choice == "future":
        print("The wizard tells you about your adventurous future.")
    elif choice == "item":
        print("The wizard gives you a magical amulet that will protect you on your journey.")

def main():
    display_intro()
    path = choose_path()
    
    if path == "cave":
        explore_cave()
    elif path == "river":
        cross_river()
    
    # Add more scenarios and choices
    deep_cave()
    meet_wizard()

if __name__ == "__main__":
    main()
