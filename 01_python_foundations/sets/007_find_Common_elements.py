# Problem 007 — Common Elements

'''
Given two lists:
list1 = [4, 7, 2, 9, 5, 7]
list2 = [8, 2, 7, 3, 9, 2]

Write a function that returns the numbers that appear in both lists.
Expected result:
[7, 2, 9]

The order should follow the order in which the numbers appear in list1.

For example, if:
list1 = [5, 2, 8]
list2 = [8, 5, 2]

the result should be:
[5, 2, 8]
'''
list1 = [4, 7, 2, 9, 5, 7]
list2 = [8, 2, 7, 3, 9, 2]

common_list = []
seen = set()

for number in list1:
    if number in list2:
        seen.add(number)

# print(seen)

for number in list1:
    if number in seen:
        common_list.append(number)
        seen.remove(number)

print(common_list)