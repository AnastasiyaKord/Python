# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


n = 123
n1 = n // 100
n2 = (n % 100) // 10
n3 = n % 10
res = n1 + n2 + n3
print(res)
