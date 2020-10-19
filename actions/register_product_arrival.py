from utils import (
    get_products,
    select_by_id_or_name,
    safe_input,
)


def register_product_arrival():
    print("--- Register product arrival ---\n")
    print("Which product is it?")

    menu = get_products()

    for thing in menu:
        print(thing['name'], thing['id'])

    chooosen_product = select_by_id_or_name(menu, 'product')

    arrival_quantity = safe_input('int_positive', 'Recent arrival quantity:')

    chooosen_product['quantity'] += arrival_quantity
    print(chooosen_product)
