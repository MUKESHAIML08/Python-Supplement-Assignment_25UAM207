# Copilot Instructions for Python Debugging Assignment

## Project Overview
This is a **debugging challenge repository** with 100 Python problems (`problem_01.py` through `problem-100.py`). Each file contains working code with **exactly one subtle error** that must be identified and fixed without rewriting the entire code.

## Critical Workflow
- **Goal:** Find and fix ONE error per file (do NOT rewrite)
- **Testing:** Each problem should execute without errors after fixing
- **Pattern:** All files follow this structure:
  ```python
  # Problem XX: [Description]
  # Find and fix the error
  
  [code with one bug]
  ```

## Common Error Categories
Errors typically fall into these patterns:

### Logic & Boundary Errors
- **Off-by-one in ranges:** `range(1, 10)` vs `range(1, 11)` - check loop boundaries
- **Comparison operators:** `<` vs `<=`, `>` vs `>=` - verify edge cases
- **Loop conditions:** Verify termination logic and boundary values

### Type & Operator Errors
- **Integer vs float division:** `/` always returns float, `//` returns int
- **Type comparisons:** Comparing different types (e.g., string to int)
- **ASCII operations:** Using `ord()` and `chr()` for character manipulation

### Data Structure Issues
- **List reference vs copy:** Direct assignment creates reference, not copy (`list2 = list1.copy()`)
- **Mutable default arguments:** Avoid `def func(lst=[])` - use `None` and initialize inside
- **String immutability:** Remember strings are immutable; assignment doesn't modify original

### Case & String Issues
- **Case sensitivity:** `.lower()` or `.upper()` needed for comparisons
- **Whitespace:** `.strip()` for leading/trailing spaces, `.split()` for tokenizing
- **Character conditions:** `char.isdigit()`, `char.isalpha()` for checking types

### Algorithm Implementation
- **Euclidean Algorithm (GCD):** Swap values correctly with temp variable
- **Stack operations:** Verify push/pop sequences for balanced parentheses
- **Accumulation patterns:** Ensure initialization value matches operation (sum=0, product=1)

## Debugging Approach
1. **Read the code and docstring** to understand intended behavior
2. **Run the code** mentally or actually execute to see what goes wrong
3. **Identify the discrepancy** between expected vs actual output
4. **Locate the single bug** - typically 1-3 lines need modification
5. **Test the fix** - verify output is now correct

## Key Patterns in Codebase
- Problems progress from simple string/math operations to algorithms (sorting, stacks, recursion)
- Later problems (50+) involve more complex logic with multiple functions
- Each problem is self-contained; no dependencies between files
- All problems use basic Python (no external libraries required)

## Testing Problems
Run directly with Python:
```bash
python problem_XX.py
```
Problems either print correct output or fail silently/with error - success criteria varies per problem, but the comment describes the intended behavior.
