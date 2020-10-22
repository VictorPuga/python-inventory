from utils import (
    get_products,
    select_by_id_or_name,
    safe_input
)


def query_inventory_data():
    """
    Get information of a given product.
    """

    print("--- Query inventory data ---\n")
    print("Which product is it?")

    list_products = get_products()

    # display products to the user
    for products in list_products:
        print("- %s (%s)" % (
            products['name'], products['id']
        ))
    print()

    this_product = select_by_id_or_name(list_products, 'product')

    print("Selected: %s (%s)\n" % (this_product['name'], this_product['id']))

    # display info
    print("Description:", this_product["description"])
    print("Id:", this_product["id"])
    print("Price per unit:", this_product["price"])
    print("Quantity in stock:", this_product["quantity"])
    print("Season:", this_product["season"])
    print("Categories:", this_product["type"], "-", this_product["sub_type"])
