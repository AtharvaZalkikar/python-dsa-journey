# Problem 3 — Count Occurrences

numbers = [4, 7, 2, 7, 9, 7, 1, 4]

def count_occurrences(numbers, n):
    count = 0

    for i in numbers:
        if i == n:
            count+=1

    return count

result = count_occurrences(numbers,7)
print(result)