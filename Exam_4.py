import random

lst1 = [random.randint(1, 100) for i in range(10)]
lst2 = []

for i in lst1:
    if i % 2 == 0:
        lst2.append(i)

print(f"{lst1} \n{lst2}")
