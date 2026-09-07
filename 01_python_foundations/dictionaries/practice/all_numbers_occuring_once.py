numbers = [3, 5, 3, 2, 5, 7, 2, 8]

# Mini challenge

# Find all numbers that occur exactly once.

dict_numbers = {}

for number in numbers:
    dict_numbers[number] = dict_numbers.get(number, 0) + 1

list_of_singles = []

for key in dict_numbers:  # noqa: PLC0206
    if dict_numbers[key] == 1:
        list_of_singles.append(key)
    
print(list_of_singles)