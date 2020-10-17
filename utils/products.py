def get_products():
    values = ('id', 'name', 'price', 'quantity',
              'season', 'type', 'syb_type', 'description')
    data = []
    file = open('products.csv')

  #  search = input('ID or name of the product?: ')
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
            "description": spacing[7].replace('\n', '')
        }

        # print(line)
        print(product)

    file.close()
    return data
