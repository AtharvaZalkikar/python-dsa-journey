numbers = [1, 2, 3, 4, 5]

test_case = [9, 7, 7, 5] #replace test_case with numbers and run program

test_case = [10, 3]

test_case = [5, 5, 5, 5]



def find_second_largest(numbers):
    largest = numbers[0]
    second_largest = None
    
    if numbers[1]>largest:
        second_largest = largest
        largest = numbers[1]
    else:
        second_largest = numbers[1]
        
    for i in range(2,len(numbers)):
        if numbers[i]>largest:
            second_largest = largest
            largest = numbers[i]
        
        elif numbers[i]>second_largest:
            second_largest = numbers[i]
            
    return largest, second_largest
        
        
a = find_second_largest(numbers)

print(a)
