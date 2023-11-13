# Задача №13. Решение в группах
# 1)Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.

# 2)Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 10). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# 1
import random
n = int(input("Введите натуральное число 1 ≤ n ≤ 10: "))
counter = 0
maximus = 0
for i in range(n): 
    # num = int(input("Введите число от -50 до 50: "))
    num = random.randint(-50, 50)
    print(num, end='; ')
    
    if num > 0:
        counter += 1
        # maximus = max(maximus, counter)
        if maximus < counter:
            maximus = counter
    else:
        counter = 0
print()
print(maximus)
   
   
# 2

import random
n = int(input("Введите натуральное число 1 ≤ n ≤ 10: "))
counter = 0
maximus = 0
for i in range(n): 
    # num = int(input("Введите число от -50 до 50: "))
    num = random.randint(-50, 50)
    print(num, end='; ')
    
    if num > 0:
        counter += 1
        # maximus = max(maximus, counter)
        if maximus < counter:
            maximus = counter
    else:
        counter = 0
print()
print(maximus)