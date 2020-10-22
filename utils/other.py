import datetime


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
