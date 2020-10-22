from utils import (
    get_products,
    select_by_id_or_name,
    safe_input,
    update_products
)


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
