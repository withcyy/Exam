def capital(input_list):
    new_list = []
    for item in input_list:
        if item[0].isupper():
            new_list.append(item)
    return new_list

num_lines = int(input("Num of lines: "))
input_list = []

for i in range(num_lines):
    line = input(f"Line {i+1}: ")
    input_list.append(line)

result = capital(input_list)
print("Result:", result)