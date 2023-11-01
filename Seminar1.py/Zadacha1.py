# Задача №1. Общее обсуждение
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

import math

speed = int(input('Введите скорость: '))
distance = int(input('Введите расстояние: '))
time = math.ceil(distance/speed)
print(time)

# 2
time = (distance - 1) // speed + 1

# 3
time = (distance + (speed - 1)) // speed
time = (750 + (700 - 1)) // 700