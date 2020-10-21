from utils import (
    get_sales,
    get_products,
    find_by_key
)


def most_sold_items():
    print("--- Most sold items ---")
    print("Top 3 most sold product until now:")

    products = get_products()
    sales_file = get_sales()

    products_sold = {}

    for product in products:
        products_sold[product["id"]] = 0

    for sold_item in sales_file:
        product_id = sold_item["product_id"]
        products_sold[product_id] += sold_item["num_products"]

    top_products = []

    for i in range(3):
        top_product = {"product_id": -1, "products": -1}

        for k in products_sold:
            total = products_sold[k]
            if total > top_product['products']:
                top_product = {
                    "product_id": k,
                    "products": total
                }
        top_products.append(top_product)
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
