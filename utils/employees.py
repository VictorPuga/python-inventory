from .other import dict_from_entries

keys = ('id', 'name', 'last_name', 'position')


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
        employees.append(dict_from_entries(keys, (
            int(id),
            name,
            last_name,
            position.rstrip()
        )))

    file.close()
    return tuple(employees)
