
def python_search(input_list):
    new_list = []
    for l in input_list:
        if "Python" in l:
            new_list.append(l)
    return new_list

num_lines = int(input("Num of lines: "))
input_list = []

for i in range(num_lines):
    line = input(f"Line {i+1}: ")
    input_list.append(line)

result = python_search(input_list)
print("Result:", result)