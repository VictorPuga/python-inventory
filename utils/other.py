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
