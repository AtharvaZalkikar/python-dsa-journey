# Two Sum
'''
We want two different elements whose sum is 9.

numbers = [2, 7, 11, 15]
target = 9
'''

numbers = [2, 8, 11, 15]
target = 9

def two_sum(numbers, target):
    seen = {}

    for i, number in enumerate(numbers):
        needed = target -  number

        if needed in seen:
            return [needed,number]
        else:
            seen[number] = i 
    return None

result = two_sum(numbers, target)
print(result)
