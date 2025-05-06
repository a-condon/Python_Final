# Explanation: python_final.py

This document explains the internal structure and logic of the `python_final.py` script. It addresses the required points: data structures used, edge case handling, and how overcounting is avoided.

---

## 1. What data structures were used and why?

The script uses **dictionaries** (`dict`) as the primary data structure for storing counts:

- `kmer_counts` — This dictionary stores the frequency of each k-mer found in the sequence. Each key is a string representing a k-mer, and the value is an integer count.

- `follower_counts` — This is a **nested dictionary**. The outer dictionary uses k-mers as keys. Each value is another dictionary that maps characters (which follow the k-mer) to their frequency.

These data structures were chosen because:
- They provide constant-time lookup and update (`O(1)`)
- They are easy to initialize and update using basic Python syntax
- They allow for dynamic creation of keys as new patterns are encountered

No external libraries or complex structures (like sets, classes, or pandas DataFrames) were used in order to stay within the material covered.

---

## 2. How are edge cases handled?

Edge cases are accounted for in both the script and the tests:

- **Empty sequence**:  
  If the input file contains no valid characters, both `kmer_counts` and `follower_counts` return as empty dictionaries. This avoids errors when trying to loop over nonexistent data.

- **Very large k**:  
  If the user enters a `k` value that is greater than or equal to the length of the sequence, the script does not enter the counting loops. This prevents out-of-bounds errors and results in empty outputs, which is the expected behavior.

- **Single character or repeated characters**:  
  The functions correctly count repeated k-mers and can handle sequences like `"AAAAAA"` or `"G"` without crashing.

All of these edge cases are tested explicitly in `test_python_final.py`.

---

## 3. How does the code avoid overcounting or missing context?

The script uses a `while` loop that moves through the sequence **one character at a time**, without skipping or overlapping incorrectly. Specifically:

- For k-mer counting, the loop starts at index `i` and reads `sequence[i:i+k]`
- For follower counting, the same index `i` is used, and the character immediately after the k-mer is taken from `sequence[i+k]`

Because:
- The loop stops at `len(sequence) - k`
- The character at `i+k` is only read if it exists

...this prevents:
- **Overcounting**: No k-mer is counted more than once per position
- **Out-of-bounds errors**: The last k-mer that doesn't have a following character is safely skipped from the follower analysis

The structure ensures that each substring and each follower character is counted exactly once in context.