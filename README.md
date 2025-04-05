# Letter Increment (lincr)

A simple Python utility that increments sequences of letters, similar to how spreadsheet columns work (A, B, C, ..., Z, AA, AB, etc.).

## Usage

```python
from letter_increment import LetterIncrement

# Create an instance
incrementer = LetterIncrement()

# Increment a single letter
result = incrementer.increment_sequence('A')  # Returns ['B']

# Increment multiple times
result = incrementer.increment_sequence('A', 3)  # Returns ['B', 'C', 'D']

# Works with longer sequences
result = incrementer.increment_sequence('ZZ', 2)  # Returns ['AAA', 'AAB']

# Supports lowercase too
result = incrementer.increment_sequence('abc', 1)  # Returns ['abd']
```

## Features

- Supports both uppercase and lowercase letter sequences
- Can increment multiple times in one call
- Automatically handles carrying over (Z → AA)
- Maintains case consistency (raises error if mixed case)
