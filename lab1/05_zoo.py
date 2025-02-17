#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print("После добавления медведя:", zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print("После добавления птиц:", zoo)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
print("После удаления слона:", zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark')+ 1
print(f"Лев находится в клетке №{lion_index}")
print(f"Жаворонок находится в клетке №{lark_index}")