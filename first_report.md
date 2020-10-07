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
        draggable="false"
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

## Data Models

### Products

| **id** | **name** | **price** | **quantity** | **season** |
| ------ | :------: | :-------: | :----------: | :--------: |
| `int`  | `string` |  `float`  |    `int`     |  `string`  |

```python
product = {
    "id": 0,
    "name": "Coffee",
    "price": 20.00,
}
```

### Employees

| **id** | **name** | **position** |
| ------ | :------: | :----------: |
| `int`  | `string` |   `string`   |

```python
employee = {
    "id": 0,
    "name": "Johny",
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

| **Seasons** |     | **Rating** |     | **Positions** |
| :---------- | --- | :--------- | --- | :------------ |
| `"ALL"`     |     | `1`        |     | `"REGISTER"`  |
| `"SPRING"`  |     | `2`        |     | `"MANAGER"`   |
| `"SUMMER"`  |     | `3`        |     | `"WAITER"`    |
| `"FALL"`    |     | `4`        |     | `"BARISTA"`   |
| `"WINTER"`  |     | `5`        |     |               |
