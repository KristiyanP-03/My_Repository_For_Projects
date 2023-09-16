print("Check if you have already tried those numbers.")
print("If you put unwanted number by accident use '/GoBack'")
print("to rewrite the wrong number.")
list_of_your_numbers = []
number_counter = 0
print("First, how many combos do you have?")
input_counts = int(input())
for each_count in range(input_counts):
    while number_counter != 6:
        print(f"Enter a number. There are {number_counter} number/s entered.")
        six_of_fortysix = input()
        if six_of_fortysix == "/GoBack":
            del list_of_your_numbers[-1]
            number_counter -= 1
            continue
        elif six_of_fortysix.isdigit() and 0 < int(six_of_fortysix) <= 47 and \
                int(six_of_fortysix) not in list_of_your_numbers:
            six_of_fortysix = int(six_of_fortysix)
            list_of_your_numbers.append(six_of_fortysix)
        else:
            print(f"Error! Please rewrite number {number_counter + 1}.")
            continue
        number_counter += 1
    else:
        print("Your numbers are: ", end="")
        print(list_of_your_numbers)

    stringed_list_of_numbers = ' '.join(map(str, list_of_your_numbers))
    with open('C:/Users/royal/Desktop/Python Projects/TotoComboChecker_PY/combos.txt', 'r') as r:
        r_content = r.read()
        for line in r_content:
            if stringed_list_of_numbers in r_content:
                print("Combo already used!")
                break
            else:
                print("Printing ...")
                with open('C:/Users/royal/Desktop/Python Projects/TotoComboChecker_PY/combos.txt', 'w') as w:
                    w.write(r_content + '\n' + stringed_list_of_numbers)
                break
    number_counter = 0
    list_of_your_numbers = []