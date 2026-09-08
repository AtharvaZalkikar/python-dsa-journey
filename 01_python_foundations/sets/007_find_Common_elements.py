# Problem 007 — Common Elements

'''
Given two lists:
list1 = [4, 7, 2, 9, 5, 7]
list2 = [8, 2, 7, 3, 9, 2]

Write a function that returns the numbers that appear in both lists.
Expected result:
[7, 2, 9]

The order should follow the order in which the numbers appear in list1.

For example, if:
list1 = [5, 2, 8]
list2 = [8, 5, 2]

the result should be:
[5, 2, 8]
'''
list1 = [4, 7, 2, 9, 5, 7]
list2 = [8, 2, 7, 3, 9, 2]

common_list = []
seen = set()

for number in list1:
    if number in list2:
        seen.add(number)

# print(seen)

for number in list1:
    if number in seen:
        common_list.append(number)
        seen.remove(number)

print(common_list)

'''

Yes — this is a good solution, and more importantly, your reasoning is solid. You're starting to think in terms of separating the problem into stages, which is exactly what I want to see.

For your input, you get:

[7, 2, 9]

And your duplicate handling is particularly good:

seen.remove(number)

That ensures the second 7 in list1 doesn't get added again.

One thing I want to challenge

You said:

"I will loop through each number of list1 and check if the number is present in list2"

That's correct, but there's a performance issue hiding there.

You're doing:

if number in list2:

list2 is a list, so Python may have to scan through it to find the number.

Then you do another pass through list1.

For small lists, absolutely fine. But in DSA, we want to start noticing this.

You could make membership checking faster by converting list2 into a set:

list2_set = set(list2)

Then:

if number in list2_set:

Now the conceptual approach becomes:

list2
  ↓
set(list2)
  ↓
fast membership checking

list1 → check → common set
                 ↓
             preserve list1 order
                 ↓
             common_list

Your overall two-pass idea is still perfectly valid.

🧠 More importantly: what did you recognize?

You independently used two different properties:

Set
→ uniqueness / membership

List
→ preserve the required order

That's a very useful distinction.

You didn't just think:

"I know sets, so I'll make everything a set."

You realized:

"I need a set for identifying common values, but I need to iterate list1 to preserve its order."

That's problem-solving. 👏

One small improvement

You don't actually need common_list + seen exactly as you've structured it if we use a set of list2 and a result set, but don't optimize it yet just for the sake of optimization.

I care more about you understanding why your current solution works.

Your current solution:

Correct output ✅
Correct order ✅
Removes duplicates ✅
No prohibited methods ✅
Reasoning matches implementation ✅

I'd mark Problem 007 as independently solved.

'''