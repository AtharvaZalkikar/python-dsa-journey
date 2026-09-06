'''Write a function that finds the first number that appears more than once.'''

numbers = [4, 7, 2, 9, 1, 7, 5]

def find_first_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            return number
    
    return None

result = find_first_duplicate(numbers)

print(result)