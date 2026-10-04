# Problem 011 — Two Sum

## Problem Information

| Attribute | Details |
|---|---|
| Problem Number | 011 |
| Topic | Problem-Solving Patterns |
| Data Structure | Dictionary / Hash Map |
| Pattern | Complement Lookup |
| Difficulty | Easy |
| Learning Status | Completed with Guidance |
| Language | Python |

---

## 1. Problem Statement

Given a list of integers `numbers` and an integer `target`, find two different elements whose sum equals the target.

Assume exactly one valid pair exists.

### Example 1

```python
numbers = [2, 7, 11, 15]
target = 9
```

Expected output:

```python
[2, 7]
```

### Example 2

```python
numbers = [3, 2, 4]
target = 6
```

Expected output:

```python
[2, 4]
```

---

## 2. Initial Thought Process

My initial approach was to calculate the difference between the target and the current number.

For every number:

```python
needed = target - number
```

Then check whether `needed` exists in the list.

Initially, I considered using a set to store previously encountered numbers.

However, this introduced an important realization:

- A set helps determine whether a value has already appeared.
- A dictionary can additionally store the index where that value appeared.

This led to using a dictionary for the final approach.

---

## 3. Key Concept — Complement Lookup

Instead of checking every possible pair, we calculate the number required to complete the target.

The formula is:

```python
needed = target - number
```

For example:

```python
target = 9
number = 2

needed = 9 - 2  # 7
```

We now need to determine whether `7` has already been encountered.

We maintain a dictionary named `seen`.

Example:

```python
seen = {
    2: 0
}
```

This represents:

- Key `2`: the number encountered.
- Value `0`: its index in the original list.

If the required number is already present in `seen`, we have found our pair.

Otherwise, we store the current number and continue.

---

## 4. Final Solution

```python
def two_sum(numbers, target):
    seen = {}

    for i, number in enumerate(numbers):
        needed = target - number

        if needed in seen:
            return [needed, number]

        seen[number] = i

    return None


numbers = [2, 7, 11, 15]
target = 9

result = two_sum(numbers, target)
print(result)
```

Output:

```text
[2, 7]
```

---

## 5. Understanding `enumerate()`

The function `enumerate()` allows us to access both the index and value during iteration.

```python
numbers = [2, 7, 11, 15]

for i, number in enumerate(numbers):
    print(i, number)
```

Output:

```text
0 2
1 7
2 11
3 15
```

This is useful when a problem requires information about the position of an element.

---

## 6. Dry Run

Input:

```python
numbers = [2, 7, 11, 15]
target = 9
```

Initially:

```python
seen = {}
```

| Iteration | Current Number | Needed | Dictionary Before Check | Action |
|---|---:|---:|---|---|
| 1 | 2 | 7 | `{}` | 7 not found; store `2: 0` |
| 2 | 7 | 2 | `{2: 0}` | 2 found; return `[2, 7]` |

The function terminates as soon as the valid pair is found.

---

## 7. Important Edge Case — Duplicate Values

Consider:

```python
numbers = [3, 3]
target = 6
```

The first occurrence of `3` cannot pair with itself.

After the first iteration:

```python
seen = {3: 0}
```

During the second iteration, the required value `3` is already present.

We can now return `[3, 3]`, because the two occurrences are at different indices.

### Key Learning

Check whether the complement exists before storing the current number.

This ensures that the current element cannot match itself.

---

## 8. Complexity Analysis

### Time Complexity: O(n)

We iterate through the list once.

Dictionary membership checks and insertions take O(1) average time.

Therefore, the overall average time complexity is O(n).

### Space Complexity: O(n)

In the worst case, the dictionary stores almost every element.

Therefore, auxiliary space complexity is O(n).

---

## 9. What I Learned

- How to calculate a complement using `target - number`.
- How to use a dictionary as a lookup structure.
- How to store values along with their indices.
- How to use `enumerate()` to obtain index and value together.
- Why checking before inserting prevents an element from matching itself.
- How a hash map can replace nested loops.
- Why returning immediately is useful once the answer is found.

### My Main Learning

The important lesson was not just learning the Two Sum solution.

It was understanding how to translate a problem requirement into the information a data structure needs to store.

---

## 10. Revision Plan

- [x] Complete the problem with guided learning.
- [x] Understand the complement calculation.
- [x] Explain the approach verbally.
- [ ] Reimplement without looking at the solution.
- [ ] Solve a variation independently.
- [ ] Explain time and space complexity confidently.

**Status:** Learned with guidance — independent recall pending.
