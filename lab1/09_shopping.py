shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создаем пустой словарь для сладостей
sweets = {}

# Перебираем товары
for sweet in ['печенье', 'конфеты', 'карамель', 'пирожное']:
    prices = []  # Список цен в магазинах
    for shop, items in shops.items():
        for item in items:
            if item['name'] == sweet:
                prices.append({'shop': shop, 'price': item['price']})

    # Оставляем только два магазина с минимальными ценами
    min_prices = sorted(prices, key=lambda x: x['price'])[:2]

    # Добавляем в словарь
    sweets[sweet] = min_prices

# Вывод результата
print(sweets)