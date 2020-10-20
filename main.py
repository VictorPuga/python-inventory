from utils import (
    safe_input,
    get_products,
    get_employees,
    get_sales
)

from actions import (
    register_sale,
    register_product_arrival
)


def main():
    print("\n\n[LOGO]\n\n")
    print("Welcome to Starbucks")
    print("""
Select an action

1. Register sale
2. Register product arrival
3. Query inventory data
4. Most sold items
5. Employees with most sales
6. Generate sales report
7. Show only seasonal products
8. Customer satisfaction form
""")

    while True:
        # action = input("Action: ")
        action = safe_input('int_positive', 'Action: ')

        if action > 0 and action < 9:
            break

        print("Oops! Try again with an action from 1 to 8")

    # action can only be from 1 to 6
    if action == 1:
        register_sale()
    elif action == 2:
        register_product_arrival()
    elif action == 3:
        print("--- Query inventory data ---")
    elif action == 4:
        print(4)
        print("--- Most sold items ---")
    elif action == 5:
        print(5)
        print("--- Show employees with most items sold ---")
    elif action == 6:
        print(6)
        print("--- Generate employee's sales report ---")
    elif action == 7:
        print(7)
        print("--- Show only seasonal products ---")
    else:
        print(8)
        print("--- Customer satisfaction form ---")

    print("Thanks for using python_inventory. Have a great day\n")


while True:
    main()

    again = input("Do you want to start again? (y/n) ").strip()[0].lower()

    if (again == 'y'):
        continue
    else:
        print("Cool. See you later ;)\n")
        break
