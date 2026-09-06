# Find largest number


numbers = [4, 7, 2, 9, 1, 7, 5]


def find_max_val(numbers):
    max_val = float('-inf')

    for i in numbers:
        if i > max_val:  # noqa: PLR1730
            max_val = i

    return max_val

result = find_max_val(numbers)
print(result)