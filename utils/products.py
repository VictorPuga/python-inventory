keys = ('id', 'name', 'price', 'quantity',
        'season', 'type', 'syb_type', 'description')


def get_products():
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
        data.append(product)

    file.close()
    return data


def update_products(product_list):
    file = open('products.csv', 'w')
    for p in product_list:
        line = ''
        for k in keys:
            line += p[k]
            if k == keys[-1]:
                line += ','
            else:
                line += '\n'
        file.write(line)

    file.close()
