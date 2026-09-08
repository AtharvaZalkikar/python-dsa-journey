text1 = "programming"
text2 = "algorithm"


def find_common_character(text1,text2):
    common_text = ""
    set_text2 = set(text2)

    for char in text1:
        if char in set_text2:
            common_text += char

    # print(common_text)

    for char in text1:
        if char in common_text:
            return char
            
    return None

result = find_common_character(text1,text2)
print(result)



#  EASIER MORE OPTIMISED APPROACH

def find_common_character(text1, text2):
    set_text2 = set(text2)

    for char in text1:
        if char in set_text2:
            return char

    return None

# Main learning: Using a set for membership checks; recognizing when an intermediate collection is unnecessary; early return.


'''
Your solution vs improved solution

Your solution:

Correct ✅
Preserves text1 order ✅
Handles no match with None ✅
Uses concepts you know ✅
But does unnecessary work ⚠️

Improved Approach:

Same result ✅
One pass through text1 ✅
No intermediate common_text needed ✅
Uses a set specifically for membership ✅
Returns as soon as the answer is known ✅

This is exactly the kind of optimization I want you to start noticing.

And importantly, I wouldn't call your original solution "wrong." You solved the problem. We're now learning to make your solutions cleaner and more efficient.
'''