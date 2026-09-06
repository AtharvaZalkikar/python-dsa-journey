'''
Problem 5 — Most Frequent Number
Write a function that returns the number that appears most frequently
'''

numbers = [4, 7, 2, 7, 9, 7, 1, 4, 2, 7]

def most_frequent(numbers):
    counts = {}
    seen = set()
    
    for number in numbers:
        if number not in seen:
            seen.add(number)
            counts[number] = 1
        else:
            counts[number] += 1

    highest_count = 0
    most_frequent_number = None


    for key in counts:  # noqa: PLC0206
        if counts[key]>highest_count:
            highest_count = counts[key]        
            most_frequent_number = key

    return most_frequent_number, highest_count

result = most_frequent(numbers)
print(result)