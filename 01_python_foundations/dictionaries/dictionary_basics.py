student = {}

student["name"] = 'Atharva'

student["age"] = 25

student["city"] = 'Mumbai'

# print(student["name"])

# print(student["city"])

prices = {
    "apple": 50,
    "banana": 30,
    "mango": 80
}

prices["banana"]=35
prices["orange"]=60
print(prices["banana"])
print(prices["orange"])

'''
if key in dictionary:
    # key exists
'''

if "orange" in prices:
    print("Orange exists")

if "mangoe" not in prices:
    print("Mango does not exist")

# Exercise 4

inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

if "mouse" in inventory:
    print('Mouse found')
else:
    print("mouse does not exist")

if "monitor" in inventory:
    print('monitor exists')
else:
    print("Monitor not found")

'''
You saw that:

inventory["monitor"]

causes a KeyError if "monitor" isn't present.

.get() lets us safely ask for a value.

inventory.get("monitor")

Since "monitor" doesn't exist, this returns:

None

But we can provide a default value:

inventory.get("monitor", 0)

→ 0

'''

# Exercise 5 — .get()

inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

'''
Exercise 5 — .get() - Write code that:

Prints the quantity of "mouse" using .get()
Prints the quantity of "monitor" using .get(), but if it doesn't exist, you want 0.

Expected output:
'''

a = inventory.get("mouse",0)
print(a)

b = inventory.get("monitor",0)
print(b)

# Lesson 5: Incrementing a value

# Exercise 6
'''
Exercise 6
Start with:
counts = {}
Then pretend you receive these numbers one at a time:
7
4
7
2
4
7
Write Python code that updates counts for each number.

At the end, we should have:
{7: 3, 4: 2, 2: 1}
'''
counts = {}
counts[7] = counts.get(7,0) + 1
counts[4] = counts.get(4,0) + 1
counts[7] = counts.get(7,0) + 1
counts[2] = counts.get(2,0) + 1
counts[4] = counts.get(4,0) + 1
counts[7] = counts.get(7,0) + 1

print(counts)


# WHAT WE KNOW ABOUT DICTIONARIES SO FAR:

# Create
counts = {}

# Add / set
counts[7] = 1

# Access
counts[7]

# Update
counts[7] = 3

# Increment
counts[7] += 1

# Check existence
if 7 in counts:
    print('7 exists')

# Safe access with default
counts.get(7, 0)

# And the big frequency pattern:
# number = [4, 7, 2, 7, 9, 4, 7, 2, 5]

# counts[number] = counts.get(number, 0) + 1

# ====================================================================

# now we introduce the loop:


'''
Exercise 7

Given:
numbers = [4, 7, 2, 7, 9, 4, 7, 2, 5]

Create a dictionary containing the frequency of every number.
Use:

a dictionary
a loop
.get()

No Counter, no .count().

Expected:
{4: 2, 7: 3, 2: 2, 9: 1, 5: 1}
'''

numbers = [4, 7, 2, 7, 9, 4, 7, 2, 5]
frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)

# Exercise 8 — Iterating over a dictionary

'''
Write code that prints each student's name and score.

Expected output conceptually:

Atharva 85
Rahul 72
Priya 91
Neha 68
One hint

When you do:

for key in scores:

key will be:

"Atharva"
"Rahul"
"Priya"
"Neha"

So you need to figure out how to get the corresponding value from scores.

This is deliberately simple.

'''

scores = {
    "Atharva": 85,
    "Rahul": 72,
    "Priya": 91,
    "Neha": 68
}

for key in scores:  # noqa: PLC0206
    # scores[key] = scores.get(key, 0)
    print(key, scores[key])
    
# Problem 9 — Highest Score

scores = {
    "Atharva": 85,
    "Rahul": 72,
    "Priya": 91,
    "Neha": 68
}

# Find the student with the highest score.

max_score = float('-inf')
highest_scorer = {}

for key in scores:
    if scores[key]>max_score:  # noqa: PLR1730, RUF100
        max_score = scores[key]
        name = key

highest_scorer[name] = max_score
print(highest_scorer)




