# Algorithms, Explained Simply

An **algorithm** is just a precise recipe for solving a problem: steps a computer can follow.
A **data structure** is the way you organize data so those steps are fast.

Every algorithm in this guide is explained the same way:
> **In one line** · **Everyday picture** · **Where it's really used** · **How it works (worked by hand)** · **Speed** · **Your exercise**

**How to study an algorithm (no AI, ever, for these):**
1. Read the explanation. Close this file.
2. **Do the worked example by hand on paper** with *different* numbers.
3. Write the code from a blank file. Stuck? Go back to paper, not to Google.
4. Test it on tricky inputs: empty list, one item, duplicates, already sorted.
5. Explain it out loud in 60 seconds: what it does, how, how fast, when you'd use it.

If you can do step 5 without notes, you own it.

---

## Part 1: The foundation

### Big-O: how we measure speed
**In one line:** Big-O describes how the work grows when the input grows.

**Everyday picture:** Finding a name in a phone book.
- Read every page from the start → twice the book = twice the work. That's **O(n)**.
- Open the middle, then go left or right, and repeat → twice the book = **one** extra step. That's **O(log n)**.
- Use a contacts app that jumps straight to the name → same work for any size. That's **O(1)**.

**What it looks like with 1,000,000 items:**

| Big-O | Name | Steps for n = 1,000,000 | Example |
|---|---|---|---|
| O(1) | constant | 1 | dict lookup, `list[5]` |
| O(log n) | logarithmic | ~20 | binary search |
| O(n) | linear | 1,000,000 | loop over a list, `x in list` |
| O(n log n) | "n log n" | ~20,000,000 | good sorting (merge sort, `sorted()`) |
| O(n²) | quadratic | 1,000,000,000,000 | loop inside a loop (bubble sort) |

**Why it matters:** O(n²) on a million rows doesn't finish. Knowing this is the difference between code that works on your laptop and code that works in production.

**Quick rules:**
- One loop over the data → O(n). A loop inside a loop → O(n²).
- Halving the problem each step → O(log n).
- Drop constants: O(2n) is just O(n).

**Exercise:** For each function you wrote in week01/week02, write its Big-O in a comment.

---

### Recursion: a function that calls itself
**In one line:** Solve a big problem by solving a smaller copy of the same problem, until it's so small the answer is obvious.

**Everyday picture:** Russian nesting dolls. To count the dolls: open one, then "count the dolls inside" (same problem, smaller). When a doll has nothing inside, the answer is obvious: 1. That's the **base case**.

**Where it's used:** walking folders inside folders, trees (HTML pages, file systems, decision trees in ML), merge sort, quick sort, DFS.

**How it works:** `factorial(4) = 4 × factorial(3)`
```
factorial(4)
 └─ 4 × factorial(3)
        └─ 3 × factorial(2)
               └─ 2 × factorial(1)
                      └─ 1          ← base case: stop here
               = 2 × 1 = 2
        = 3 × 2 = 6
 = 4 × 6 = 24
```
Each call waits on a **stack** (see Stacks below) until the call below it returns.

**Two rules, always:**
1. A **base case** that stops.
2. Each call moves **closer** to the base case.
Forget either → `RecursionError: maximum recursion depth exceeded`.

**Speed:** depends on the problem. Factorial is O(n).

**Exercise:** week02 `factorial`, `flatten`. Bonus: `sum_list(nums)` and `count_down(n)` recursively.

---

### Hash tables (Python `dict` and `set`)
**In one line:** Turn a key into a storage-slot number instantly, so you can find it without searching.

**Everyday picture:** A wall of numbered lockers. A machine (the **hash function**) turns any name into a locker number: "sara" → locker 7. To find Sara's stuff you don't open every locker, you ask the machine "where's sara?" → 7 → done.

**Where it's used:** Every Python dict and set. Database indexes, caches (Redis), counting words, removing duplicates, "have I seen this before?" checks. **This is the most used data structure in real-world coding.**

**How it works:**
1. `hash("sara")` → a big number → `% number_of_slots` → slot 7.
2. Store ("sara", value) in slot 7.
3. Lookup: compute the same slot → go straight there.
4. Two keys in the same slot is a "collision". Python handles it by probing for another slot.

**Speed:** lookup, insert and delete are **O(1)** on average. `x in my_list` is O(n); `x in my_set` is O(1).

**Why keys must be immutable:** if a key could change after being stored, its hash would change, and you'd look in the wrong locker forever. That's why a list can't be a dict key but a tuple can.

**Exercise:** `word_frequency`, `remove_duplicates_keep_order`. Then the classic interview problem **Two Sum**: given numbers and a target, return the indexes of two numbers that add to the target, in **one pass** using a dict. (Hint: for each number, ask "have I already seen `target - number`?")

---

## Part 2: Searching

### Linear search
**In one line:** Check every item, one by one, until you find it.
**Everyday picture:** Looking for your keys by checking every pocket.
**Used:** small or unsorted data, `x in list`, `list.index()`.
**Speed:** O(n).
**Exercise:** `linear_search(items, target)` → index or -1.

### Binary search ⭐
**In one line:** In a **sorted** list, check the middle; throw away the half that can't contain the answer; repeat.

**Everyday picture:** The guessing game. "I'm thinking of a number between 1 and 100." The smart guess is always the middle: 50 → "higher" → 75 → "lower" → 62... At most **7 guesses** for 100 numbers, and **20** for a million.

**Where it's used:** searching sorted data, database indexes (B-trees are a cousin), `git bisect` (find which commit broke the code), Python's `bisect` module, and finding the best threshold or learning-rate range in ML.

**Worked example:** find **57** in `[3, 8, 15, 21, 34, 42, 57, 63, 77, 90]` (indexes 0–9)
```
step 1: lo=0, hi=9 → mid=4 → 34 < 57 → answer is to the RIGHT → lo=5
step 2: lo=5, hi=9 → mid=7 → 63 > 57 → answer is to the LEFT  → hi=6
step 3: lo=5, hi=6 → mid=5 → 42 < 57 → RIGHT                    → lo=6
step 4: lo=6, hi=6 → mid=6 → 57 == 57 → FOUND at index 6 ✅
```
If `lo > hi`, the item isn't there → return -1.

**Speed:** O(log n). Each step halves the problem.
**Catch:** the data **must be sorted**. Sorting first costs O(n log n), so it's worth it when you search many times.

**Classic bugs:** `while lo < hi` vs `while lo <= hi`, and forgetting `+1`/`-1` (infinite loop). Test with 1 item and with 2 items.

**Exercise:** `binary_search(sorted_items, target)` iteratively, then recursively. Then: in the week 1 guessing game, make the computer guess your number.

---

## Part 3: Sorting
Python's `sorted()` is excellent (Timsort, O(n log n)). You learn these to **train your algorithmic thinking**, and because interviewers ask about them.

### Bubble sort
**In one line:** Repeatedly swap neighbors that are in the wrong order; big values "bubble up" to the end.
**Everyday picture:** Sorting people by height by only letting neighbors swap places.
**Worked example:** `[5, 1, 4, 2]`
```
pass 1: (5,1) swap → [1,5,4,2]  (5,4) swap → [1,4,5,2]  (5,2) swap → [1,4,2,5]   ← 5 in place
pass 2: (1,4) ok    (4,2) swap → [1,2,4,5]                                    ← 4 in place
pass 3: no swaps → stop early ✅
```
**Speed:** O(n²). Used in practice: almost never. Know it, don't use it.

### Selection sort
**In one line:** Find the smallest remaining item and put it next in line.
**Everyday picture:** Picking the shortest person from a crowd, then the next shortest, and so on.
**Worked example:** `[5, 1, 4, 2]` → smallest is 1, swap to front → `[1,5,4,2]` → smallest of the rest is 2 → `[1,2,4,5]` → done.
**Speed:** O(n²) always.

### Insertion sort
**In one line:** Take items one at a time and insert each one into its correct place among the already-sorted ones.
**Everyday picture:** Sorting playing cards in your hand.
**Worked example:** `[5, 1, 4, 2]`: take 1 → goes before 5 → `[1,5 | 4,2]` → take 4 → between 1 and 5 → `[1,4,5 | 2]` → take 2 → `[1,2,4,5]`.
**Speed:** O(n²) worst case, but **very fast on nearly-sorted data**. That's why Python's Timsort uses it for small chunks.

### Merge sort ⭐
**In one line:** Split the list in half, sort each half (recursively), then **merge** the two sorted halves.

**Everyday picture:** Two teachers each sort half of the exam papers. Then you merge the two sorted piles by always taking the smaller top paper.

**Where it's used:** Python's `sorted()` (Timsort is merge sort + insertion sort), sorting huge files that don't fit in memory (external sorting), and any time you need a **stable** sort (equal items keep their original order).

**Worked example:** `[38, 27, 43, 3]`
```
split:   [38, 27]        [43, 3]
split:   [38] [27]       [43] [3]        ← 1 item = already sorted (base case)
merge:   [27, 38]        [3, 43]
merge:   compare 27 vs 3 → take 3
         compare 27 vs 43 → take 27
         compare 38 vs 43 → take 38
         left side empty → take 43
         = [3, 27, 38, 43] ✅
```
**Speed:** O(n log n) always. There are log n levels of splitting, and each level does O(n) merging work. Uses O(n) extra memory.

**Exercise:** write `merge(left, right)` first (two sorted lists → one sorted list). That's the heart of it. Then `merge_sort` is ~6 lines.

### Quick sort ⭐
**In one line:** Pick a **pivot**; put smaller items to its left and bigger ones to its right; repeat on each side.

**Everyday picture:** Splitting a class with "everyone shorter than Ali, go left; taller, go right." Then do the same inside each group.

**Where it's used:** many standard libraries (C's `qsort`, parts of NumPy's sort). It's often the fastest in practice.

**Worked example:** `[7, 2, 9, 4, 3]`, pivot = last item (3)
```
smaller than 3: [2]        pivot: [3]        bigger: [7, 9, 4]
recurse on [7, 9, 4], pivot 4 → smaller: []  pivot: [4]  bigger: [7, 9]
recurse on [7, 9], pivot 9 → smaller: [7]  pivot: [9]  bigger: []
combine: [2] + [3] + ([] + [4] + ([7] + [9])) = [2, 3, 4, 7, 9] ✅
```
**Speed:** O(n log n) on average. **O(n²) worst case** (e.g. an already-sorted list with a bad pivot), which is why real implementations pick a random or median pivot.

**Interview question:** merge sort vs quick sort? Merge is always O(n log n), stable, needs extra memory. Quick is usually faster, can sort in place, but has an O(n²) worst case.

**Exercise:** implement all 5 sorts, then **benchmark** them with `time.perf_counter()` on 1,000 / 5,000 / 20,000 random numbers. Plot the times. Watch O(n²) explode. That's a week 6 project.

---

## Part 4: Patterns that solve half of all interview problems

### Two pointers
**In one line:** Use two positions moving through the data (often from both ends) instead of a loop inside a loop.
**Everyday picture:** Two people walking toward each other from opposite ends of a hallway.
**Used:** pair sums in sorted data, reversing, palindrome checks, removing duplicates in place, merging sorted lists.
**Worked example:** sorted `[1, 3, 4, 6, 8, 11]`, find two numbers that add to **10**
```
L=1, R=11 → 12 too big   → move R left
L=1, R=8  → 9  too small → move L right
L=3, R=8  → 11 too big   → R left
L=3, R=6  → 9  too small → L right
L=4, R=6  → 10 ✅
```
**Speed:** O(n) instead of the O(n²) "try every pair" approach.

### Sliding window
**In one line:** Keep a "window" over consecutive items and slide it: add the new item, remove the old one. Never recompute from scratch.
**Everyday picture:** A train window. As the train moves, one tree enters the view and one leaves.
**Used:** **moving averages in time series** (you'll use this for traffic data in ML!), rolling features in pandas (`df.rolling()`), longest substring without repeats, rate limiting.
**Worked example:** largest sum of **3** consecutive numbers in `[2, 1, 5, 1, 3, 2]`
```
[2,1,5] = 8
slide: −2 +1 → [1,5,1] = 7
slide: −1 +3 → [5,1,3] = 9  ← max
slide: −5 +2 → [1,3,2] = 6
```
**Speed:** O(n) instead of O(n × k).

### Stack (Last In, First Out)
**In one line:** You can only add or remove at the top.
**Everyday picture:** A stack of plates.
**Used:** Undo/Redo, the browser back button, **the function call stack** (that's how recursion works!), matching brackets `({[]})`, DFS.
**In Python:** a list. `append()` pushes, `pop()` pops. Both O(1).
**Exercise:** `is_balanced("({[]})")` → True; `"(]"` → False.

### Queue (First In, First Out)
**In one line:** Add at the back, remove from the front.
**Everyday picture:** A line at a shop.
**Used:** task queues (Celery workers in backend week), print jobs, BFS, request buffering.
**In Python:** `collections.deque`. `append()` and `popleft()` are O(1). Don't use `list.pop(0)`; it's O(n).

---

## Part 5: The map ahead (full explanations when you reach them)
You'll get a full explanation (same format as above) when you reach each one. Ask Claude: **`explain <algorithm name>`**.

### Data structures & graph algorithms (weeks 6–7)
| Algorithm | The idea in one line | Where it's really used |
|---|---|---|
| Linked list | Items that each point to the next one | Building block for queues and LRU caches; classic interview topic |
| Binary tree / BST | Each node has ≤2 children; left side smaller, right side bigger | Database indexes, decision trees in ML |
| Heap / priority queue | Always gives you the smallest (or biggest) item fast | "Top 10" lists, schedulers, Dijkstra (`heapq` module) |
| Graph | Dots (nodes) connected by lines (edges) | Maps, social networks, road networks for MOBIUS AI |
| BFS | Explore a graph ring by ring, nearest first | Shortest path when every step costs the same; "people you may know" |
| DFS | Go as deep as possible, then backtrack | Mazes, detecting cycles, exploring folders |
| Dijkstra | Shortest path when roads have different lengths/costs | **Google Maps routing**, traffic-aware routing in your capstone |
| Topological sort | Order tasks so each comes after what it depends on | `pip` installing packages, build systems, course prerequisites |
| Greedy | Take the best-looking choice at each step | Making change with coins, scheduling, Huffman compression |
| Dynamic programming | Remember answers to sub-problems so you never solve one twice | Spell-check (edit distance), DNA matching, route optimization |
| Backtracking | Try a choice; if it fails, undo it and try the next | Sudoku solvers, generating permutations/combinations |

### Machine-learning algorithms (weeks 18–22): you'll code the core ones from scratch in NumPy first
| Algorithm | The idea in one line | Everyday picture | Where it's used |
|---|---|---|---|
| Linear regression | Draw the straight line that best fits the points | Guessing a house price from its size | Predicting prices, sales, **traffic speed** |
| Gradient descent | Take small steps downhill on the error until you reach the bottom | Walking down a foggy mountain by feeling the slope under your feet | How almost **every** ML model learns, including ChatGPT |
| Logistic regression | Linear regression squashed into a 0–1 probability | "How likely is this email spam?" | Yes/no predictions, a baseline for classification |
| K-nearest neighbors | You're probably like the k items closest to you | "People who live near you vote like you" | Recommendations, simple classifiers |
| Naive Bayes | Combine word probabilities to guess a category | A spam filter counting suspicious words | Text classification |
| Decision tree | A flowchart of yes/no questions learned from data | The game "20 Questions" | Interpretable models, the base of forests |
| Random forest | Many trees, each trained on random data, vote together | Asking 100 people instead of 1 | Strong default for tabular data |
| Gradient boosting (XGBoost/LightGBM) | Each new tree fixes the mistakes of the previous ones | A student re-studying only the questions they got wrong | **Wins most tabular-data competitions**; widely used in industry |
| K-means | Group unlabeled data into k clusters around centers | Sorting a pile of mixed coins without labels | Customer segments, grouping road segments by traffic pattern |
| PCA | Squash many features into a few that keep most of the information | Taking a photo of a 3D object from its most informative angle | Compression, visualization, speeding up models |
| Neural network | Layers of weighted sums + simple non-linear functions | Many tiny dimmer switches tuned together | Images, speech, text, everything "deep learning" |
| Backpropagation | Work out how much each weight is to blame for the error, using the chain rule | Tracing a wrong final answer back through each step of the working | How neural networks learn |
| CNN | A network that slides small filters over an image | A magnifying glass scanning for edges, then shapes | Image recognition |
| RNN / LSTM | A network with memory of previous steps in a sequence | Reading a sentence word by word | Older time-series and text models |
| Attention / Transformer | Each word looks at every other word to decide what matters | Highlighting the relevant words in a paragraph while reading | ChatGPT, Claude, modern NLP |
| Embeddings | Turn meaning into coordinates, so similar things are close together | A map where "king" sits near "queen" | Search, RAG, recommendations |
