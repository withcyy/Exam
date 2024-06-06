dict = {}

while True:
    print("Menu:")
    print("1. Append word")
    print("2. Delete word")
    print("3. Watch meaning")
    print("4. Exit")
    user_choice = input("(1-4): ")

    if user_choice == '1':
        word = input("Word: ")
        meaning = input("Meaning: ")
        dict[word] = meaning
    elif user_choice == '2':
        word = input("Word: ")
        if word in dict:
            del dict[word]
        else:
            print("Error!!!")
    elif user_choice == '3':
        word = input("Word: ")
        if word in dict:
            print(f"{word} - {dict[word]}")
        else:
            print("Error!!!")
    elif user_choice == '4':
        print("Exiting...")
        break
    else:
        print("Error")