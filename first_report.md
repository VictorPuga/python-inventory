```
Eva Pérez     A01568830
Víctor Puga   A01568636
```

# First Report

## Theme

<div align="center" >
    <h3>Starbucks Inventory Program</h3>
    <img 
        height="100" 
        width="100" 
        src="https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png"/>
</div>

## Tasks

- Register sales `(Víctor)`
- Register storage products `(Eva)`
- Query sales data `(Víctor)`
- Query inventory data `(Eva)`
- Show sales by employee `(Víctor)`
- Show sales by product `(Eva)`

---

- Show only seasonal products `(Eva)`
- Customer satisfaction form `(Víctor)`

## Screens

### 0. Main Menu

```
Select an action

1. Register sale
2. Register storage products
3. Query sales data
4. Query inventory data
5. Show sales by employee
6. Show sales by product
7. Show only seasonal products
8. Customer satisfaction form

Action: #    ⇢    Action: 2
```

---

### 1. Register Sales

```
Action: 1

--- Register sale ---

Who is selling the product?:
- Juan (1)
- Pedro (2)

Name or Id: #                                   ⇢   Name or Id: Pedro    or     Name or Id: 2

What product is it?:
- Coffee (1) (3 in stock)
- Tea (2) (10 in stock)

Name or Id: #                                   ⇢   Name or Id: Cofee    or     Name or Id: 1

How many items? #                               ⇢   How many items? 4

The order is valid. Calculating total price...

Total price: $80 + ($12.8 tax)

This order's id is 7

Press enter to finish

```

---

### 2. Register Storage Products

### 3. Query Sales Data

### 4. Query Inventory Data

### 5. Show Sales by Employee

### 6. Show Sales by Product

### 7. Show Only Seasonal Products

### 8. Customer Satisfaction Form

## Data Models

### Products

| **id** | **name** | **price** | **quantity** | **season** | **type** | **syb_type** |
| ------ | :------: | :-------: | :----------: | :--------: | :------: | :----------: |
| `int`  | `string` |  `float`  |    `int`     |  `string`  | `string` |   `string`   |

```python
product = {
    "id": 0,
    "name": "Frappe",
    "price": 20.00,
    "type": "DRINK",
    "sub_type": "COLD_COFFEE",
}
```

### Employees

| **id** | **name** | **last_name** | **position** |
| ------ | :------: | :-----------: | :----------: |
| `int`  | `string` |   `string`    |   `string`   |

```python
employee = {
    "id": 0,
    "name": "John",
    "last_name": "Appleseed",
    "position": "MANAGER",
}
```

### Sale

| **id** | **date** | **total_price** | **num_products** | **product_id** | **employee_id** |
| :----: | :------: | :-------------: | :--------------: | :------------: | :-------------: |
| `int`  | `string` |     `float`     |      `int`       |     `int`      |      `int`      |

```python
sale = {
    "id": 0,
    "date": "18/01/2020",
    "total_price": 300.00,
    "num_products": 15,
    "product_id": 0,
    "employee_id": 0,
}
```

### Feedback (Beta)

| **id** | **date** | **sale_id** | **rating** |
| ------ | :------: | :---------: | :--------: |
| `int`  | `float`  |    `int`    |   `int`    |

```python
feedback = {
    "id": 0,
    "date": "18/01/2020",
    "sale_id": 0,
    "rating": 5,
}
```

## Enumerations

| **Seasons** |     | **Rating** |     | **Positions** |     | **Types** |     | **Sub Types**   |
| :---------- | --- | :--------- | --- | :------------ | --- | :-------- | --- | :-------------- |
| `"ALL"`     |     | `1`        |     | `"REGISTER"`  |     | `"DRINK"` |     | `"HOT_COFFEE"`  |
| `"SPRING"`  |     | `2`        |     | `"MANAGER"`   |     | `"FOOD"`  |     | `"HOT_DRINK"`   |
| `"SUMMER"`  |     | `3`        |     | `"WAITER"`    |     |           |     | `"HOT_DRINK"`   |
| `"FALL"`    |     | `4`        |     | `"BARISTA"`   |     |           |     | `"COLD_COFFEE"` |
| `"WINTER"`  |     | `5`        |     |               |     |           |     | `"COLD_DRINK"`  |
|             |     |            |     |               |     |           |     | `"COLD_DRINK"`  |
|             |     |            |     |               |     |           |     | `"BREAKFAST"`   |
|             |     |            |     |               |     |           |     | `"LUNCH"`       |
|             |     |            |     |               |     |           |     | `"SNACK"`       |
