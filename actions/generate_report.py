from random import randint

from utils import (
    get_employees,
    get_sales,
    get_products,
    select_by_id_or_name,
    today,
    find_by_key
)


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
