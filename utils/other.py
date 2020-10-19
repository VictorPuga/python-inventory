import datetime


def dict_from_entries(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict


def safe_input(input_type, message):
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
    for el in dict_list:
        if el[key] == value:
            return el


def select_by_id_or_name(dict_list, name):
    while True:
        selected = None
        name_or_id = safe_input('string', 'Name or Id: ')
        print()

        if name_or_id.isdecimal():
            selected = find_by_key(dict_list, 'id', int(name_or_id))
        else:
            selected = find_by_key(dict_list, 'name', name_or_id)

        if selected:
            return selected
        else:
            print("No %s with that criteria." % name)
            print("Try again")


def today():
    date = datetime.datetime.now()
    return date.strftime("%x")
