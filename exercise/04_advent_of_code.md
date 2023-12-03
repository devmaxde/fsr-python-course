# Advent of Code

Advent of Code is an annual event, that publishes a coding problem every day starting on December 1st until December 25th.
For this exercise solve Day 1 of Advent of Code 2023.

**Link:** https://adventofcode.com/2023/day/1

## Hint

At one point we will need to check if a string is a digit.

We can do so by creating a sequence of all the numbers as strings and use the `in` operation to do so:

```python
digits = "1234567890" 
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] # Equivalent to "1234567890", except it's mutable
```

Let `s` be any expression of the string data type.
We can check, if `s` is a digit by doing the following:

```python
if s in digits:
    # s is a digit, e.g. "1", "5", "2"
```

Including the else clause it looks like this

```python
if s in digits:
    # s is a digit, e.g. "1", "5", "2"
else:
    # s is NOT a digit, e.g. "abcd", "a46ba", "b3"
```

We can then use the `int(s)` expression to convert a string `s` to an integer.

For example, we can store the converted integer in a new variable called `n`

```python
if s in digits:
    n = int(s) # n is an integer
```

