from .other import dict_to_csv_line, dict_from_entries

columns = (
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

        sales.append(dict_from_entries(columns, (
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
    line = dict_to_csv_line(sale, columns)

    file.write(line)
    file.close()
