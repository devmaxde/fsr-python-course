# Functions

## Mutable vs. Immutable Sequence Types

Before we get to this chapter's topic, functions, a quick refresher on the three sequence types:
We defined the sequence types Strings, Tuples and Lists.
We further categorize them into two categories:

* **Mutable Sequence Types:** Lists
* **Immutable Sequence Types:** Strings, Tuples

When we introduced the String data type, we have defined **sequence operations** which have allowed us to e.g. find and count symbols in a string, create a new string by concatenating two strings together, etc.

These **sequence operations** work for both, **mutable** and **immutable** sequences, i.e. Lists, Strings and Tuples.

For the sake of completeness, the following table shows the sequence operations again, but instead of using a String in the example, we use a List.

Let `s`, `t` be sequences and `i`, `j`, `k`, `n` be integers.

| Expression         | Operation                                                                              | Example                    | Result         |
| ------------------ | -------------------------------------------------------------------------------------- | -------------------------- | -------------- |
| `s + t`            | The concatenation of `s` and `t`                                                       | `["hello"] + ["world"]`    | `["hello", "world"]` |
| `s * n` or `n * s` | Equivalent to adding `s` to itself `n` times                                           | `["abc"] * 3`              | `["abc", "abc", "abc"]`  |
| `s[i]`             | _i_-th item of `s`, starting at 0                                                      | `["zero", "one", "two"][1]`| `"one"`|
| `s[i:j]`           | Slice of `s` from `i` to `j`                                                           | `["zero", "one", "two", "three"][1:3]`| `["one", "two"]`   |
| `s[i:j:k]`         | Slice of `s` from `i` to `j` with step `k`                                             | `[0, 1, 2, 3, 4, 5, 6, 7, 8][1:6:2]`| `[1, 3, 5]`        |
| `len(s)`           | Length of `s`                                                                          | `len(["zero", "one", "two"])`           | `3`            |
| `s.index(x)`       | Index of the first occurrence of `x` in `s`                                            | `["zero", "one", "two"].index("two")`     | `2`            |
| `s.index(x, i)`    | Index of the first occurrence of `x` in `s` at or after index `i`                      | `["apple", "pear", "kiwi", "apple"].index("apple", 3)`  | `3`            |
| `s.index(x, i, j)` | Index of the first occurrence of `x` in `s` at or after index `i` and before index `j` | `[7, 4, 4, 5, 6, 4, 4, 8].index(4, 3, 7)`| `5`            |
| `s.count(x)`       | Total number of occurrences of `x` in `s`                                              | `["apple", "pear", "kiwi", "apple"].count("apple")`     | `2`            |


**Mutable** sequence types, i.e. Lists, support a variety of additional expressions and statements, which **actively modify** a List.

Let `s`, `t` be sequences, `i`, `j`, `k`, `n` be integers, and `x` be an expression of any data type.

| Statement             | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| `s[i] = x`            | item `i` of `s` is replaced by `x`                                 |
| `s[i:j] = t`          | slice of `s` from `i to j` is replaced by the contents of `t`      |
| `del s[i:j]`          | same as `s[i:j] = []`                                           |
| `s[i:j:k] = t`        | the elements of `s[i:j:k]` are replaced by those of `t`           |
| `del s[i:j:k]`    | removes the elements of `s[i:j:k]` from the list                |
| `s.append(x)`         | appends `x` to the end of the sequence (equivalent to `s = s + [x]`) |
| `s.clear()`           | removes all items from `s` (equivalent to `s = []`)                   |
| `s.extend(t) or s += t` | extends `s` with the contents of t (equivalent to `s = s + t)` |
| `s *= n`              | updates `s` with its contents repeated n times                   |
| `s.insert(i, x)`      | inserts `x` into `s` at the index given by i |
| `s.pop(i)` | retrieves the item at `i` and also removes it from `s`          |
| `s.pop()` | retrieves the last item in `s` and also removes it from `s` (equivalent to `s.pop(len(s) - 1)`)          |
| `s.remove(x)`     | remove the first item from `s` where `s[i]` is equal to `x`         |
| `s.reverse()`      | reverses the items of `s` in place                               |

> [!TIP]
> These are a lot of statements to memorize.
> It is recommended to try them out in the **Interactive Shell** to get familiar with their behavior.
> ```console
> >>> test = ["apple", "oranges", "bananas"]
> >>> test.pop()
> 'bananas'
> >>> test
> ['apple', 'oranges']
> ```

## Advent of Code 2023

Let's use what we learned so far in practice by solving the first day of [Advent of Code 2023](https://adventofcode.com/2023/day/1).

