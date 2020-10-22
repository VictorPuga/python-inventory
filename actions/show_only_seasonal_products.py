from utils import (
    select_by_id_or_name,
    get_products
)


def show_only_seasonal_products():
    """
    Ask for the user to select a season. Then, display the products to 
    the user that match the selected season.
    """

    print("--- Show only seasonal products ---\n")

    menu = get_products()

    seasons = [
        {"id": 1, "name": "ALL"},
        {"id": 2, "name": "SPRING"},
        {"id": 3, "name": "SUMMER"},
        {"id": 4, "name": "FALL"},
        {"id": 5, "name": "WINTER"},
    ]

    print('Select a season:')
    for sea in seasons:
        print(sea['name'].title(), '(' + str(sea['id']) + ')')
    print()

    this_season = select_by_id_or_name(seasons, 'season')

    print("Products available only in %s season:" %
          this_season["name"].title())
    for product in menu:
        if product["season"] == this_season["name"]:
            print("-", product["name"])
