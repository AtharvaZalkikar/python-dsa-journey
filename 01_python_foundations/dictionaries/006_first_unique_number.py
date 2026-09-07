'''
Problem 006 — First Unique Number

Given:
numbers = [4, 7, 2, 7, 9, 4, 5, 2]

Find the first number that occurs only once.

'''

'''
But here's the important part

I'm not telling you which data structure to use.

Before you write any code, answer these two questions:

What information do you need to keep track of?
What data structure would you choose to keep that information, and why?

Don't worry about syntax yet.
'''

# Approach 1:
'''
we need to keep track of what are the numbers we have seen we can use set for that,
then to keep count of how many times they have occured we can use dictionary.
and then loop through the dictionary to find the first element or key whose value is 1
which tells us this is the first unique number
'''

# Counter approach by GPT:
'''
The keys tell us which numbers exist, and the values tell us their frequencies.

So a dictionary alone may be sufficient.

But there's another subtlety in your answer

You said:

"then loop through the dictionary to find the first element or key whose value is 1"

Careful. "First" matters here.

A dictionary's frequency table might be:

4 → 2
7 → 2
2 → 2
9 → 1
5 → 1

Both 9 and 5 are unique, but the answer is 9, because 9 appeared first in the original list.

So I want you to think about this:

Should we find the frequencies first and then iterate through the original numbers list again?

That would preserve the original order.
'''

# My Answer - Explanation:
'''
ok we can iterate through the original numbers list again and use them as keys and find their corresponding values
and for the first key where we get value 1 that is our answer.

but even in my previous approach, wont it still work ? 
because dictionary will also be created in the order we find elemnts in list right like -
first time we see 4 the key is added in dictionary and value set to one then we see 7 in numbers list then its value is set to 1 in dictionary
then we again see 4 then we increment value of 4 to 2 and so on
that is why i thought the previous appraoch would also work
'''

# Yes. You caught an important Python detail, and your original approach can work

# Approach 1 :
'''
for key in frequency:
    if frequency[key] == 1:
        return key
'''

# Approach 2 - more safe explicit: iterate through list numbers:
'''
for number in numbers:
    if frequency[number] == 1:
        return number
'''
# Find First Unique Number

numbers = [4, 7, 2, 7, 9, 4, 5, 2]


def find_first_unique(numbers):
    dict_numbers = {}

    for number in numbers:
        dict_numbers[number] = dict_numbers.get(number,0) + 1

    for key in dict_numbers:  # noqa: PLC0206
        if dict_numbers[key] == 1:
            return key
        
    return None

result = find_first_unique(numbers)
print(result)