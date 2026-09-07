# Python DSA Journey — Progress Tracker

This is a chronological record of my problem-solving journey.

The problem number is **global** and represents the order in which problems were attempted.

Topics may change at any point, but numbering will always continue sequentially.

---

## Current Focus

**Phase:** Python Problem-Solving Foundations

**Current Topic:** Dictionaries

**Current Problem:** 006

**Goal:** Build strong problem-solving ability, not just interview survival.

---

## Problem Tracker

| # | Problem | Topic | Concept / Pattern | Difficulty | Independent? | Help Needed | Main Struggle / Learning |
|---|---|---|---|---|---|---|---|
| 001 | Find Maximum | Arrays | Iteration / State Tracking | Easy | Yes* | Initial guidance | Python syntax and implementation |
| 002 | Second Largest | Arrays | State Tracking | Easy | With guidance | Yes | Recognizing the correct approach |
| 003 | Count Occurrences | Arrays | Iteration | Easy | Yes | No | — |
| 004 | First Duplicate | Sets | Seen Elements | Easy | Yes | No | Edge-case handling |
| 005 | Most Frequent Number | Dictionaries | Frequency Counting | Easy | With guidance | Syntax refresher | Dictionary mechanics |
| 006 | First Unique Number | Dictionaries | Frequency Counting | Easy | Yes | No | Two-pass frequency approach; dictionary insertion order |

\* Problem 001 was solved independently during the later reconstruction.

---

## Skills Checkpoints

### Python Fundamentals

- [x] Basic loops
- [x] Conditionals
- [x] List iteration
- [x] Maintaining state
- [x] Dictionary fundamentals
- [x] Dictionary frequency counting
- [ ] Dictionary fluency
- [ ] Set fluency
- [ ] String manipulation
- [ ] Functions
- [ ] Recursion basics
- [ ] Searching
- [ ] Sorting concepts
- [ ] Big-O basics

### Problem-Solving

- [x] Understand a simple problem
- [x] Translate a simple idea into code
- [ ] Choose the right data structure consistently
- [ ] Recognize common patterns
- [ ] Handle unfamiliar problems confidently
- [ ] Solve under time pressure
- [ ] Explain approach while coding
- [ ] Debug under interview pressure

---

## Revision Queue

Problems that should be revisited:

- 002 — Second Largest
- 005 — Most Frequent Number
- 006 — First Unique Number

---

## Key Lessons So Far

### Problem 001 — Find Maximum

A simple one-pass state-tracking pattern:

keep the best value seen so far and update it when a larger value appears.

### Problem 002 — Second Largest

The main challenge was not the final algorithm but recognizing that maintaining

`largest` and `second_largest` was simpler than trying to manipulate/sort the list.

### Problem 003 — Count Occurrences

Straightforward iteration and conditional counting.

### Problem 004 — First Duplicate

A set is useful when the important question is:

**"Have I already seen this value?"**

### Problem 005 — Most Frequent Number

A dictionary can map:

`number → number of occurrences`

The main challenge was applying dictionary syntax and mechanics.

### Problem 006 — First Unique Number

Built a frequency dictionary and then iterated through its keys to find the first key whose value was `1`.

Important observation:

Python dictionaries preserve insertion order, so the order of first appearance is retained.

### Dictionary Application Checkpoint

**Mini Challenge — All Numbers Occurring Once**

Given a list of numbers, find all numbers that occur exactly once.

Approach:

- Build a frequency dictionary.
- Create a result list.
- Iterate through the dictionary.
- Add keys whose frequency is `1`.

Result: **Solved independently.**

Key learning:

Frequency counting can be reused for different problems by changing what we do with the frequency information after building the dictionary.

---

## Milestones

- [x] First problem solved
- [x] First 5 problems completed
- [ ] First 10 problems completed
- [ ] Python Foundations completed
- [ ] First problem solved without any hints
- [ ] First Medium problem solved independently
- [ ] First timed problem completed
- [ ] First mock interview completed
- [ ] 50 problems completed
- [ ] 100 problems completed

---

## Daily Consistency

A contribution counts when I genuinely show up and do meaningful work.

The GitHub contribution graph is a **record of consistency, not the goal itself**.

Even one meaningful problem or focused practice session counts as showing up.

---

## Notes

This tracker is intentionally chronological.

The purpose is not to collect solutions.

The purpose is to document the development of problem-solving ability over time.