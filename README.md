# 🧠 algorithms-vault

Welcome to **algorithms-vault** — a curated collection of algorithmic solutions, strategies, and concepts.  
This repository is designed not just for practice, but as a **vault of understanding**, where each problem is paired with clean code, clear explanations, and insights on performance and trade-offs.

---

## 📁 Repository Structure

Each folder represents a topic. Inside each, you'll find:
- ✅ Python solutions (multiple approaches if applicable)
- ✅ Short explanations of the logic used
- ✅ Time & space complexity analysis
- ✅ Visual tables or notes when useful

```bash
/sorting/
    ├── bubble_sort.py
    ├── merge_sort.py
    └── README.md

/hashing/
    ├── two_sum_brute.py
    ├── two_sum_hashset.py
    └── README.md

/greedy/
    └── activity_selection.py

---
## 🧾 Example Entry: Two Sum

<details>
  <summary><strong>Click to view code and explanation</strong></summary>

```python
# Brute Force
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

# Hash Set Optimised
seen = set()
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        return [i, nums.index(diff)]
    seen.add(num)

### ✅ Hash Set Approach

**Technique:** Hashing (Set Lookup)  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)  
**Concepts:** Complement lookup, early exit, constant-time set access

</details>

---

## 📊 Summary Table

| Problem    | Approach    | Time       | Space | Notes                 |
| ---------- | ----------- | ---------- | ----- | --------------------- |
| Two Sum    | Brute Force | O(n²)      | O(1)  | Naive, easy to write  |
| Two Sum    | Hash Set    | O(n)       | O(n)  | Optimal using hashing |
| Merge Sort | Recursion   | O(n log n) | O(n)  | Divide and conquer    |

---

## 🚀 How to Use

- Browse folders by topic  
- Read the explanation before diving into code  
- Try solving before looking at the answer  
- Fork the repo and practice on your own  

---

## 🛠 Tech Stack

- Python 3  
- Markdown for explanations  
- (Optional) Jupyter Notebooks for visual breakdowns  

---

## 🌱 In Progress

More problems will be added regularly under topics like:

- Arrays & Strings  
- Recursion & Backtracking  
- Greedy & Dynamic Programming  
- Sliding Window  
- Two Pointer  
- Stack & Queue  
- Graphs & Trees  
- Hashing  

---

## 📬 Suggestions or Contributions

You can:

- ⭐ Star the repo if you find it helpful  
- 📁 Open an issue to request a topic or improvement  
- 💡 Contribute new problems or explanations via pull requests  

