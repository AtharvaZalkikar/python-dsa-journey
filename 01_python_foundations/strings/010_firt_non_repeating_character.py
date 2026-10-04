# Problem 010 — First Non-Repeating Character

# text = "swiss"
# text = "aabbcdd"
text = "aabb"

def find_non_rep_char(text):
    seen = {}

    for char in text:
        seen[char] = seen.get(char,0) + 1

    for key in seen:  # noqa: PLC0206
        if seen[key]==1:
            return key
    
    return None
        
result = find_non_rep_char(text)

print(result)