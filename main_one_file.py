import datetime
from random import randint

"""

UTILITY FUNCTIONS

"""


def dict_from_entries(keys, values):
    """
    Generate a dictonary from keys and values iterables.

    Parameters:
        - keys (list or tuple): keys for the dictionary
        - values (list or tuple): values for the dictionary

    Returns:
        - new_dict (dictionary)
    """

    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict


def safe_input(input_type, message):
    """
    Ask for input.

    Parameters: 
        - input_type (string): data type for the input. One of:
            - "string"
            - "int_positive"
            - "float_positive"

    Returns:
        - value (depends on input_type)
    """

    while True:
        value = input(message).strip()
        if value:
            if input_type == 'string':
                return value
            elif input_type == 'int_positive' and value.isnumeric():
                return int(value)
            elif input_type == 'float_positive' and value.replace('.', '').isnumeric():
                return float(value)


def find_by_key(dict_list, key, value):
    """
    Find the first dictionary in an iterable with a key-value pair

    Parameters: 
        - dict_list (list or tuple): iterable to search
        - key (string): key to compare
        - value (any): value to search in key

    Returns: 
        - element (dictionary): element of dict_list
        or
        - None: if no item was found
    """

    for el in dict_list:
        if str(el[key]).upper() == str(value).upper():
            return el


def select_by_id_or_name(dict_list, name):
    """
    Find an element in an iterable with user input. 
    Asks for a name or an id, and automatically searches the list.
    Automatically validates user input.

    Parameters: 
        - dict_list (list or tuple): iterable to search
        - name (string): name of the entities in dict_list. Used to provide feedback to the user

    Returns: 
        - element (dictionary): element of dict_list
    """

    while True:
        selected = None
        name_or_id = safe_input('string', 'Name or Id: ')
        print()

        if name_or_id.isdecimal():
            selected = find_by_key(dict_list, 'id', int(name_or_id))
        else:
            selected = find_by_key(dict_list, 'name', name_or_id)

        # Make sure an element was selected,
        # otherwise, ask again
        if selected:
            return selected
        else:
            print("No %s with that criteria." % name)
            print("Try again")


def today():
    """
    Get today's date.

    Returns: 
        - date (string): date formated as "MM/DD/YY"
    """

    date = datetime.datetime.now()
    return date.strftime("%x")


def dict_to_csv_line(dictionary, keys):
    """
    Transform dictionary into a string to be written in a csv file

    Parameters:
        - dictionary: object to transform
        - keys (list or tuple): keys of the dictionary

    Returns:
        - line (string): csv line
    """

    line = ''
    for k in keys:
        line += str(dictionary[k])
        if k != keys[-1]:
            line += ','
        else:
            line += '\n'
    return line


employee_keys = ('id', 'name', 'last_name', 'position')


def get_employees():
    """
    Read all the employees from employees.csv, and return them.

    Returns:
        - employees (tuple): dictionary tuple with employee data

    Sample dictionary:
    ```
    employee = {
        "id": 0,
        "name": "John",
        "last_name": "Appleseed",
        "position": "REGISTER"
    }
    ```
    """

    employees = []

    file = open('employees.csv')

    for line in file:
        # using unpacking syntax
        id, name, last_name, position = line.split(',')

        # use the dict_from_entries function to generate each employee dictionary
        employees.append(dict_from_entries(employee_keys, (
            int(id),
            name,
            last_name,
            position.rstrip()
        )))

    file.close()
    return tuple(employees)


feedback_keys = ('id', 'date', 'sale_id', 'rating')


def get_feedbacks():
    """
    Read and return the feedback from feedbacks.csv.

    Returns:
        - feedbacks (tuple): dictionary tuple with feedback data

    Sample dictionary:
    ```
    feedback = {
        "id": 0,
        "date": "01/02/20",
        "sale_id": 0,
        "rating": 5
    }
    """

    feedbacks = []

    file = open('feedbacks.csv')
    for line in file:
        # using unpacking syntax
        id, date, sale_id, rating = line.split(',')

        feedbacks.append(dict_from_entries(feedback_keys, (
            int(id),
            date,
            int(sale_id),
            int(rating.rstrip()),
        )))

    file.close()
    return tuple(feedbacks)


def add_feedback(feedback):
    """
    Append a single feedback to feedbacks.csv

    Parameters: 
        - feedback (dictionary): feedback data

    Sample dictionary:
    ```
    feedback = {
        "id": 0,
        "date": "01/02/20",
        "sale_id": 0,
        "rating": 5
    }
    """
    # append, not destructive write
    file = open('feedbacks.csv', 'a')
    line = dict_to_csv_line(feedback, feedback_keys)
    file.write(line)
    file.close()


product_keys = ('id', 'name', 'price', 'quantity',
                'season', 'type', 'sub_type', 'description')


def get_products():
    """
    Get all products from products.csv

    Returns: 
        - products (list): dictionary list with product data

    Sample dictionary:
    ```
    product = {
        "id": 0,
        "name": "Frappe",
        "price": 20.00,
        "quantity": 234567,
        "season": "ALL",
        "type": "DRINK",
        "sub_type": "COLD_COFFEE",
        "description": "What else could you ask for?"
    }
    """

    products = []
    file = open('products.csv')

    for line in file:
        spacing = line.split(',')
        product = {
            "id": int(spacing[0]),
            "name": spacing[1],
            "price": float(spacing[2]),
            "quantity": int(spacing[3]),
            "season": spacing[4],
            "type": spacing[5],
            "sub_type": spacing[6],
            # remove newline
            "description": spacing[7].replace('\n', '')
        }
        products.append(product)
    # always close the file
    file.close()
    return products


def update_products(product_list):
    """
    Update products.csv. This will override the whole file.

    Parameters: 
        - product_list (list or tuple): new product data
    """

    # delete everything and write
    file = open('products.csv', 'w')
    for p in product_list:
        line = dict_to_csv_line(p, product_keys)
        file.write(line)

    file.close()


sales_keys = (
    'id',
    'date',
    'total_price',
    'num_products',
    'product_id',
    'employee_id'
)


def get_sales():
    """
    Get all the sales from sales.csv

    Returns:
        - sales (tuple): dictionary tuple with sale data

    Sample dictionary:
    ```
    sale = {
        "id": 0,
        "date": "01/02/20",
        "total_price": 20.0,
        "num_products": 4,
        "product_id": 0,
        "employee_id": 0
    }
    """
    sales = []
    file = open('sales.csv')
    for line in file:
        # using unpacking syntax
        id, date, total_price, num_products, product_id, employee_id = line.split(
            ',')

        sales.append(dict_from_entries(sales_keys, (
            int(id),
            date,
            float(total_price),
            int(num_products),
            int(product_id),
            int(employee_id.rstrip()),
        )))

    file.close()
    return tuple(sales)


def add_sale(sale):
    """
    Write a new sale to sales.csv

    Parameters: 
        - sale (dictionary): sale data

    Sample dictionary:
    ```
    sale = {
        "id": 0,
        "date": "01/02/20",
        "total_price": 20.0,
        "num_products": 4,
        "product_id": 0,
        "employee_id": 0
    }
    """
    file = open('sales.csv', 'a')
    line = dict_to_csv_line(sale, sales_keys)

    file.write(line)
    file.close()


"""

ACTIONS FUNCTIONS

"""


def customer_satisfaction_form():
    """
    Ask a customer for their rating. 
    Writes a review to feedback.csv
    """

    feedback = {
        "date": today()
    }
    print("--- Customer satisfaction form ---\n")
    print('Which is your sale id (it is found on your receipt)?')

    total_sales = len(get_sales())

    sale_id = 0

    while True:
        sale_id = safe_input('int_positive', 'Sale id: ')
        # check if id exists
        if sale_id > -1 and sale_id < total_sales:
            break
        else:
            print('That sale id is invalid')

    print('\nHow was our service? (1, 2, 3, 4, 5)')
    rating = 0
    while True:
        rating = safe_input('int_positive', 'Rating: ')
        if rating > 0 and rating < 6:
            break
        else:
            print('Please select a number from 1 to 5')

    feedback['sale_id'] = sale_id
    feedback['rating'] = rating
    # last available id
    feedback['id'] = len(get_feedbacks())

    add_feedback(feedback)

    print('\nCool. Thanks for giving us your feedback.')
    print('We hope to see you again')


def employees_with_most_sales():
    """
    Get the top 3 employees with most sales. 
    Functionality is similar to most_sold_items()
    """

    print('--- Show employees with most items sold ---\n')

    employees = get_employees()
    sales = get_sales()

    products_by_employee = {}

    # fill the dictionary with initial values
    for e in employees:
        products_by_employee[e['id']] = 0

    # add the number of products sold by each employee
    for s in sales:
        employee_id = s['employee_id']
        products_by_employee[employee_id] += s['num_products']

    top_employees = []

    # get the top 3
    for i in range(3):
        top_employee = {"employee_id": -1, "products": -1}

        for k in products_by_employee:
            total_products = products_by_employee[k]
            # if the current employee has more sales, replace top_employee
            if total_products > top_employee['products']:
                top_employee = {
                    "employee_id": k,
                    "products": total_products
                }
        # add to podium
        top_employees.append(top_employee)
        # delete from list to calculate other placees
        del products_by_employee[top_employee['employee_id']]

    print('Top 3 employees:')
    place = 0
    for el in top_employees:
        place += 1
        employee = find_by_key(employees, 'id', el['employee_id'])
        print("%s) %s %s with %s items sold" % (
            place,
            employee['name'],
            employee['last_name'],
            el['products']
        ))


def generate_report():
    """
    Generate a report for an employee

    This will write to a .txt file

    Sample file:

    ```
    EMPLOYYEE NAME - POSITION 

    |  ID  | NAME                | QUANTITY |
    | ---- | ------------------- | -------- |
    | ...  | ...                 | ...      |
    | ...  | ...                 | ...      |
    ```
    """

    print("--- Generate employee's sales report ---")
    print("\nSelect an employee:")

    employees = get_employees()
    products = get_products()
    sales = get_sales()

    # display employees to the user
    for e in employees:
        print("- %s (%s)" % (e['name'], e['id']))
    print()

    employee = select_by_id_or_name(employees, 'employee')

    print("Creating file...")

    product_quantities = {}

    # will be used for the output file
    largest_name = 0

    # add initial values
    for product in products:
        product_quantities[product['id']] = 0
        length = len(product['name'])

        if length > largest_name:
            largest_name = length

    # update the products sold by the employee
    for sale in sales:
        if sale['employee_id'] == employee['id']:
            product_quantities[sale['product_id']] += sale['num_products']

    filename = "sales_report_%s_%s_%s_%s.txt" % (
        employee['name'],
        employee['last_name'],
        # change to valid filename format
        today().replace('/', '-'),
        # apply some randomness to the filename
        randint(100, 999)
    )
    file = open(filename, 'w')

    file.write('%s %s - %s \n\n' % (
        employee['name'],
        employee['last_name'],
        employee['position'].title()
    ))
    file.write('|  ID  | NAME' + (' ' * (largest_name - 4)) + ' | QUANTITY |\n')
    file.write('| ---- | ' + ('-' * largest_name) + ' | -------- |\n')

    for k in product_quantities:
        product = find_by_key(products, 'id', k)
        line = '| %s | %s | %s |\n' % (
            str(k).ljust(4),
            product['name'].ljust(largest_name),
            str(product_quantities[k]).ljust(8)
        )
        file.write(line)

    file.close()

    print('File saved as "%s"' % filename)


def most_sold_items():
    """
    Get the top 3 most sold items-
    """

    print("--- Most sold items ---\n")
    print("Top 3 most sold product until now:")

    products = get_products()
    sales_file = get_sales()

    products_sold = {}

    # add initial values
    for product in products:
        products_sold[product["id"]] = 0

    # update the product quantities
    for sold_item in sales_file:
        product_id = sold_item["product_id"]
        products_sold[product_id] += sold_item["num_products"]

    top_products = []

    # top 3
    for _i in range(3):
        top_product = {"product_id": -1, "products": -1}

        for k in products_sold:
            total = products_sold[k]
            # update the curent top value
            if total > top_product['products']:
                top_product = {
                    "product_id": k,
                    "products": total
                }
        # add to the podium
        top_products.append(top_product)
        #  delete from list to calculate other placees
        del products_sold[top_product['product_id']]

    place = 0
    for el in top_products:
        place += 1
        product = find_by_key(products, 'id', el['product_id'])
        print(" %s) %s with %s units sold" % (
            place,
            product['name'],
            el['products']
        ))


def query_inventory_data():
    """
    Get information of a given product.
    """

    print("--- Query inventory data ---\n")
    print("Which product is it?")

    list_products = get_products()

    # display products to the user
    for products in list_products:
        print("- %s (%s)" % (
            products['name'], products['id']
        ))
    print()

    this_product = select_by_id_or_name(list_products, 'product')

    print("Selected: %s (%s)\n" % (this_product['name'], this_product['id']))

    # display info
    print("Description:", this_product["description"])
    print("Id:", this_product["id"])
    print("Price per unit:", this_product["price"])
    print("Quantity in stock:", this_product["quantity"])
    print("Season:", this_product["season"])
    print("Categories:", this_product["type"], "-", this_product["sub_type"])


def register_product_arrival():
    """
    Register when a product has arrived. 
    This will update products.csv
    """

    print("--- Register product arrival ---\n")
    print("Which product is it?\n")

    menu = get_products()

    # display products to the user
    for thing in menu:
        print("- %s (%s)" % (
            thing['name'], thing['id']
        ))
    print()

    chooosen_product = select_by_id_or_name(menu, 'product')

    print("Selected: %s (%s)\n" % (
        chooosen_product['name'], chooosen_product['id']
    ))

    arrival_quantity = safe_input('int_positive', 'Recent arrival quantity:')
    print()

    chooosen_product['quantity'] += arrival_quantity

    # show feedback to the users
    print('OKAY. You\'ve registered %s items of %s' % (
        arrival_quantity,
        chooosen_product['name']
    ))
    print('Now there are %s in stock' % chooosen_product['quantity'])

    update_products(menu)


def register_sale():
    """
    Register a new sale.

    This will update products.csv and sales.csv
    """

    sale = {
        "date": today()
    }

    print("--- Register sale ---\n")
    print("Who is selling the product?")

    # display employees to the user
    employees = get_employees()
    for e in employees:
        print("- %s (%s)" % (e['name'], e['id']))
    print()

    employee = select_by_id_or_name(employees, 'employee')
    sale['employee_id'] = employee['id']

    print("Selected: %s (%s)\n" % (employee['name'], employee['id']))
    print("Which product is it?")
    products = get_products()

    # display products to the user
    for p in products:
        print("- %s (%s) (%s in stock)" %
              (p['name'], p['id'], p['quantity']))
    print()

    product = select_by_id_or_name(products, 'product')

    sale['product_id'] = product['id']

    print("Selected: %s (%s) (%s in stock)\n" %
          (product['name'], product['id'], (product['quantity'])))

    quantity = 0
    while True:
        quantity = safe_input("int_positive", "How many items? ")
        # check if there are enough items in stock
        if quantity > 0 and quantity <= product['quantity']:
            print("The order is valid. Calculating total price...")
            break
        else:
            print(
                "The order is invalid. Please choose a number that is not greater than the quantity in stock")

    # we are updating the reference, so this dictionary is also modified
    # on the products list
    product['quantity'] -= quantity
    sale['num_products'] = quantity
    sale['total_price'] = quantity * product['price']

    print("\nTotal price: $%s (+ $%s tax)" % (
        sale['total_price'],
        sale['total_price'] * 0.16
    ))

    sale['id'] = len(get_sales())

    print("\nThis order's id is", sale['id'])

    update_products(products)
    add_sale(sale)


def show_only_seasonal_products():
    """
    Ask for the user to select a season. Then, display the products to 
    the user that match the selected season.
    """

    print("--- Show only seasonal products ---\n")

    menu = get_products()

    seasons = [
        {"id": 1, "name": "ALL"},
        {"id": 2, "name": "SPRING"},
        {"id": 3, "name": "SUMMER"},
        {"id": 4, "name": "FALL"},
        {"id": 5, "name": "WINTER"},
    ]

    print('Select a season:')
    for sea in seasons:
        print(sea['name'].title(), '(' + str(sea['id']) + ')')
    print()

    this_season = select_by_id_or_name(seasons, 'season')

    print("Products available only in %s season:" %
          this_season["name"].title())
    for product in menu:
        if product["season"] == this_season["name"]:
            print("-", product["name"])


"""

MAIN PROGRAM

"""


def main():
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
        action = safe_input('int_positive', 'Action: ')

        if action > 0 and action < 9:
            break

        print("Oops! Try again with an action from 1 to 8")

    # action can only be from 1 to 8
    if action == 1:
        register_sale()
    elif action == 2:
        register_product_arrival()
    elif action == 3:
        query_inventory_data()
    elif action == 4:
        most_sold_items()
    elif action == 5:
        employees_with_most_sales()
    elif action == 6:
        generate_report()
    elif action == 7:
        show_only_seasonal_products()
    else:
        customer_satisfaction_form()

    print("\nThanks for using python_inventory. Have a great day\n")


print(" ★ Welcome to Starbucks ★ ")

while True:
    main()

    again = input("Do you want to start again? (y/n) ").lower()

    if 'y' in again:
        continue
    else:
        print("Cool. See you later ;)\n")
        break
