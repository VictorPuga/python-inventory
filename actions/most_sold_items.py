from utils import (
    get_sales,
    get_products,
    find_by_key
)


def most_sold_items():
    """
    Get the top 3 most sold items-
    """

    print("--- Most sold items ---\n")
    print("Top 3 most sold product until now:")

    products = get_products()
    sales_file = get_sales()

    products_sold = {}

    # add initial values
    for product in products:
        products_sold[product["id"]] = 0

    # update the product quantities
    for sold_item in sales_file:
        product_id = sold_item["product_id"]
        products_sold[product_id] += sold_item["num_products"]

    top_products = []

    # top 3
    for _i in range(3):
        top_product = {"product_id": -1, "products": -1}

        for k in products_sold:
            total = products_sold[k]
            # update the curent top value
            if total > top_product['products']:
                top_product = {
                    "product_id": k,
                    "products": total
                }
        # add to the podium
        top_products.append(top_product)
        #  delete from list to calculate other placees
        del products_sold[top_product['product_id']]

    place = 0
    for el in top_products:
        place += 1
        product = find_by_key(products, 'id', el['product_id'])
        print(" %s) %s with %s units sold" % (

            place,
            product['name'],
            el['products']
        ))
