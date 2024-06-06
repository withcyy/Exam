first_num = int(input("Num: "))
second_num = int(input("Num: "))
res = 0

if second_num < first_num:
    second_num, first_num = first_num, second_num

for i in range(first_num, second_num + 1):
    res += i

print(res)

