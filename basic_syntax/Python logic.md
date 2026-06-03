

---

Markdown

\# The Master Logic Blueprint: From Zero to LeetCode

To succeed in competitive programming (HackerRank/LeetCode), you must bridge the gap between knowing Python syntax and understanding algorithmic efficiency. 

This document trains the exact mental models required to break down complex problems, choose optimal data structures, and write highly efficient code.

\---

\#\# 1\. The Enhanced LeetCode Problem-Solving Formula

For every single problem, do not touch your keyboard until you have written out the **\*\*IOSSEC-T\*\*** framework on paper or in a notebook.

\* **\*\*I\*\***nput: What exactly is being given? (Types, constraints, sorted/unsorted?)  
\* **\*\*O\*\***utput: What must be returned?  
\* **\*\*S\*\***torage: What variables, arrays, or maps do I need?  
\* **\*\*S\*\***teps: Step-by-step English logic (Pseudocode).  
\* **\*\*E\*\***dge Cases: Empty arrays, negative numbers, extreme values (e.g., \`n \= 0\`, duplicates).  
\* **\*\*C\*\***ode: Translate the steps into Python syntax.  
\* **\*\*T\*\***ime & Space (Big O): How fast will this run? Will it cause a Time Limit Exceeded (TLE) error?

\---

\#\# 2\. The 4 Essential Data Structures for CP

You already know Lists and Dictionaries. To ace LeetCode, you must master these four heavily optimized structures.

\#\#\# 1\. Sets (\`set()\`)  
\* **\*\*Why:\*\*** Checking if an item exists in a List takes $O(N)$ time. Checking if an item exists in a Set takes **\*\*$O(1)$\*\*** (instant) time.  
\* **\*\*Use Case:\*\*** Removing duplicates, finding intersections, lightning-fast lookups.  
\`\`\`python  
seen \= set()  
seen.add(5)  
if 5 in seen:  \# This is instant O(1)  
    print("Found")

### **2\. Hash Maps (Dictionaries {})**

* **Why:** Stores key-value pairs with $O(1)$ lookup time.  
* **Use Case:** Frequency counting, mapping values to indices (e.g., Two Sum).

### **3\. Stacks (Using Lists \[\])**

* **Why:** Last-In-First-Out (LIFO) logic.  
* **Use Case:** Valid parentheses, reversing operations, tracking previous states.  
* **Operations:** stack.append() to push, stack.pop() to remove the top.

### **4\. Queues (collections.deque)**

* **Why:** First-In-First-Out (FIFO) logic. Standard lists are slow $O(N)$ at removing the first item. Deques do it in $O(1)$.  
* **Use Case:** Processing items in order, Breadth-First Search (BFS).  
* **Operations:** queue.append() to add, queue.popleft() to remove the front.

## ---

**3\. The 5 Core LeetCode Meta-Patterns**

Once you know the beginner loops (Accumulator, Counter, Search), you must learn these Elite Patterns. They solve 80% of LeetCode Easy/Medium array and string problems.

### **Pattern 1: The Hash Map / Dictionary Lookup (The "Two Sum" Pattern)**

Used when you need to find pairs of numbers or track elements you've seen previously without using slow nested loops.

Python

\# Problem: Find two numbers that add up to target  
def two\_sum(nums, target):  
    seen \= {} \# value : index  
    for i, num in enumerate(nums):  
        diff \= target \- num  
        if diff in seen:  
            return \[seen\[diff\], i\]  
        seen\[num\] \= i

### **Pattern 2: Two Pointers**

Used on **sorted arrays** or strings to find pairs, reverse items, or compare elements from both ends moving inward.

Python

\# Problem: Check if a string is a palindrome  
left \= 0  
right \= len(s) \- 1

while left \< right:  
    if s\[left\] \!= s\[right\]:  
        return False  
    left \+= 1  
    right \-= 1  
return True

### **Pattern 3: Sliding Window**

Used when looking for a continuous sub-array or substring (e.g., "maximum sum of 3 consecutive elements").

Python

\# Problem: Max sum of sub-array of size K  
current\_sum \= sum(arr\[:k\])  
max\_sum \= current\_sum

for i in range(k, len(arr)):  
    \# Slide the window: add next element, subtract first element of previous window  
    current\_sum \= current\_sum \+ arr\[i\] \- arr\[i-k\]  
    max\_sum \= max(max\_sum, current\_sum)

### **Pattern 4: Fast & Slow Pointers**

Used primarily in Linked Lists or cyclic arrays to detect cycles or find the middle element.

Python

slow \= head  
fast \= head  
while fast and fast.next:  
    slow \= slow.next  
    fast \= fast.next.next  
    if slow \== fast:  
        return True \# Cycle detected

### **Pattern 5: Prefix Sum**

Used when you need to repeatedly calculate the sum of elements in different ranges of an array.

Python

\# Build a running total array  
prefix \= \[0\] \* (len(nums) \+ 1)  
for i in range(len(nums)):  
    prefix\[i+1\] \= prefix\[i\] \+ nums\[i\]

\# Sum from index L to R is instant: prefix\[R+1\] \- prefix\[L\]

## ---

**4\. Big O Notation: The Speed Test**

LeetCode will reject correct logic if it is too slow. You must understand Time Complexity.

* **$O(1)$ Constant Time:** The holy grail. (e.g., Dictionary lookups, Set lookups, Math formulas).  
* **$O(N)$ Linear Time:** Acceptable for most arrays. You loop through the data exactly once or sequentially.  
* **$O(N \\log N)$ Log-Linear Time:** The standard time for sorting an array (nums.sort()).  
* **$O(N^2)$ Quadratic Time:** DANGER. This happens when you use nested loops (a loop inside a loop). It will cause Time Limit Exceeded (TLE) on large inputs. **Always try to replace a nested loop with a Hash Map.**

## ---

**5\. The 14-Day Zero-to-LeetCode Bootcamp**

Do not skip steps. Solve these in order to build the muscle memory required for advanced algorithms.

### **Phase 1: Logic Fundamentals (Days 1-7)**

*Focus on correctness, not speed.*

* **Day 1 (Conditionals):** Even/Odd, Largest of 3, Leap Year.  
* **Day 2 (Accumulators & Loops):** Sum 1 to N, Factorial, Print Multiplication Table.  
* **Day 3 (Number Math):** Reverse integer using % 10 and // 10, Sum of Digits, Check Prime.  
* **Day 4 (Strings):** Reverse String, Count Vowels, Check Palindrome (basic way).  
* **Day 5 (Arrays/Lists):** Find Max, Second Largest, Reverse List manually.  
* **Day 6 (Hash Maps):** Character Frequency, Word Count, Find Most Frequent Item.  
* **Day 7 (Integration):** Turn Days 1-6 into reusable def functions().

### **Phase 2: LeetCode Readiness (Days 8-14)**

*Focus on efficiency and Big O.*

* **Day 8 (Sets & O(1) Lookups):** Remove duplicates from an array, Find the missing number in an array.  
* **Day 9 (Two Pointers \- Basic):** Reverse array in place, Valid Palindrome (ignoring spaces/punctuation).  
* **Day 10 (Two Pointers \- Advanced):** Two Sum II (sorted array), Move Zeroes to end.  
* **Day 11 (Hash Map Mastery):** Two Sum (unsorted), Valid Anagram, First Unique Character.  
* **Day 12 (Sliding Window):** Maximum Average Subarray I, Longest Substring Without Repeating Characters.  
* **Day 13 (Stacks):** Valid Parentheses, Evaluate Reverse Polish Notation.  
* **Day 14 (Prefix Sum):** Running Sum of 1d Array, Find Pivot Index.

## ---

**6\. The "Anti-Stuck" Protocol for CP**

When you open a HackerRank or LeetCode problem and your mind goes blank, execute this protocol exactly:

1. **Read the constraints first.** Are the numbers huge? An $O(N^2)$ nested loop won't work. Is the array sorted? You should immediately think of *Two Pointers* or *Binary Search*.  
2. **Write down a small manual example.** Trace it step-by-step with a pen. How does a human solve it?  
3. **Identify the bottleneck.** Are you searching a list repeatedly? Convert it to a Set or Dictionary to make it $O(1)$.  
4. **The 30-Minute Rule:** \* Stuck for 15 mins? Re-read the constraints and try a different pattern.  
   * Stuck for 30 mins? Look at the **Discussion/Solutions tab**.  
   * **CRITICAL:** Do *not* copy-paste the solution. Read the logic, close the tab, and write the code from your own memory.