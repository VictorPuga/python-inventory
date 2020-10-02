

def main():
    print("""
Select an action

1. SOMETHING...
2. SOMETHING...
3. SOMETHING...
4. SOMETHING...
5. SOMETHING...
6. SOMETHING...
""")

    while True:
        action = input("Action: ")

        # avoid int parsing error
        if action.isnumeric():
            action = int(action)
            if action > 0 and action < 7:
                break

        print("Oops! Try again with an action from 1 to 6")

    # action can only be from 1 to 6
    if action == 1:
        print(1)
        print("You selected SOMETHING")
    elif action == 2:
        print(2)
        print("You selected SOMETHING")
    elif action == 3:
        print(3)
        print("You selected SOMETHING")
    elif action == 4:
        print(4)
        print("You selected SOMETHING")
    elif action == 5:
        print(5)
        print("You selected SOMETHING")
    else:
        print(6)
        print("You selected SOMETHING")

    print("Thanks for using python_inventory. Have a great day\n")


while True:
    main()

    again = input("Do you want to start again? (y/n) ").strip()[0].lower()

    if (again == 'y'):
        continue
    else:
        print("Cool. See you later ;)\n")
        break
