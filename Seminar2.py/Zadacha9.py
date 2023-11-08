# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

n = int(input("Введите натуральное число: "))
count = 1
result = 1
while count <= n:
    result *= count  #result = result * count
    count += 1  #count = count + 1
print(result)


# 2
n = int(input("Введите натуральное число: "))
result = 1
while n > 1:
    result *= count  
    n -= 1  
print(result)