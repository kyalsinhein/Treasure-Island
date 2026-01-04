print(r'''
████████╗██████╗ ███████╗ █████╗ ███████╗██╗   ██╗██████╗ ███████╗
╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║██╔══██╗██╔════╝
   ██║   ██████╔╝█████╗  ███████║███████╗██║   ██║██████╔╝█████╗  
   ██║   ██╔══██╗██╔══╝  ██╔══██║╚════██║██║   ██║██╔══██╗██╔══╝  
   ██║   ██║  ██║███████╗██║  ██║███████║╚██████╔╝██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
-----------------------------------------------------------------
                    🏝️  TREASURE ISLAND  🏝️
-----------------------------------------------------------------
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

choice1 = input(
    'You\'re at a crossroad.\n'
    'Type "left" or "right":\n> '
).lower()

if choice1 == "left":
    choice2 = input(
        '\nYou\'ve come to a lake.\n'
        'There is an island in the middle of the lake.\n'
        'Type "wait" to wait for a boat.\n'
        'Type "swim" to swim across:\n> '
    ).lower()

    if choice2 == "wait":
        choice3 = input(
            '\nYou arrive at the island unharmed.\n'
            'There is a house with 3 doors:\n'
            'Red, Yellow, and Blue.\n'
            'Which colour do you choose?\n> '
        ).lower()

        if choice3 == "red":
            print("\n🔥 It\'s a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("\n💰 You found the treasure. You Win! 🎉")
        elif choice3 == "blue":
            print("\n🐺 You enter a room of beasts. Game Over.")
        else:
            print("\n🚪 You chose a door that doesn\'t exist. Game Over.")
    else:
        print("\n🐟 You got attacked by an angry trout. Game Over.")
else:
    print("\n🕳️ You fell into a hole. Game Over.")
