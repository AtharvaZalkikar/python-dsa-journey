# Write a function that returns a list containing only the unique numbers, while preserving the order of their first appearance.

numbers = [4, 7, 2, 4, 9, 7, 5]

seen = set()
temp_list = []

for number in numbers:
    if not number in seen:
        seen.add(number)
        temp_list.append(number)

print(temp_list)

