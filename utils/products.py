from .other import dict_to_csv_line

keys = ('id', 'name', 'price', 'quantity',
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
        line = dict_to_csv_line(p, keys)
        file.write(line)

    file.close()
