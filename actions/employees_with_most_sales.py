from utils import (
    get_employees,
    get_sales,
    dict_from_entries,
    find_by_key
)


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
