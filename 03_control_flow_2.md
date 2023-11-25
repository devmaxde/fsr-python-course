# Control Flow 2

## Loops

### `while` statement: the conditional loop

You can make a block of code execute over and over again using a `while` statement.
The code in a while clause will be executed as long as the `while` statement’s condition evaluates to `True`.

In code, a while statement always consists of the following:

- The `while` keyword
- A condition (that is, an expression that evaluates to `True` or `False`)
- A colon (`:`)
- Starting on the next line, an indented block of code

You can see that a while statement looks similar to an `if` statement.
The difference is in how they behave.
At the end of an `if` statement, the program execution continues after the if statement. But at the end of a while statement, the program execution jumps back to the start of the while statement.

Let’s look at an `if` statement and a `while` loop that use the same condition and take the same actions based on that condition.

**Example**
```python
i = 0
if i < 5:
    print("Hello World")
    i = i + 1
```
**Output**
```console
Hello World
```
**Flowchart**

<img src="assets/03_if_while.svg" width="452" />

**Example**
```python
i = 0
while i < 5:
    print("Hello World")
    i = i + 1
```
**Output**
```console
Hello World
Hello World
Hello World
Hello World
Hello World
```
**Flowchart**

<img src="assets/03_while.svg" width="448" />

### `for` statement: the sequence loop

```python
for c in "Hello":
    print(c)
```
**Output**
```console
H
e
l
l
o
```

## The "List" and "Tuple" Sequence Data Types

So far we established `string` data type, which consists of a sequence of Unicode symbols.
Going a step further, we can generalize the concept of sequences and obtain two new data types: _**Lists**_ and _**Tuples**_.

### Lists

Similar to a `string`, a list is a sequence of values, however instead of being limited to single unicode symbols, the elements can be of any size and data type.
Lists may contain items of different data types, but usually the items all have the same type.

The literal expression of the List data type consists of comma-separated values, wrapped in square brackets (`[`, `]`)

For example, let `a`, `b` and `c` be expressions of any data type.
A List containing `a`, `b` and `c` in this order looks like this:
```python
[a, b, c]
```

Just like other expressions, we can use variables to store a List, e.g. a shopping list:

```python
groceries = ["Apples", "Oranges", "Cheddar Cheese", "Milk", "Bread"]
```

Just like letters/symbols in a String, each item in our List is assigned to an Index:

| Element | `"Apples"` | `"Oranges"` | `"Cheddar Cheese"` | `"Milk"` | `"Bread"` |
| ------: | :---: | :---: | :---: | :---: | :---: |
| Index   | `0` | `1` | `2` | `3` | `4` |

We can use the same sequence operations we learned earlier with strings:

```console
>>> ["zero", "one", "two"] + ["three", "four"]
["zero", "one", "two", "three", "four"]
```


### Tuples

A Tuple ist almost identical to a List, however it is _**immutable**_.
So unlike a List, you cannot add or remove elements to or from a tuple after the fact.

Creating a tuple is done the same way, but instead of using square (`[`, `]`), we use parantheses (`(`, `)`):

```python
>>> foo = ("the meaning of life", 42)
>>> foo[0]
'the meaning of life'
>>> foo[1]
42
```

## The `range()` expression

Very commonly, you need to execute a block of code a specific number of times.
For example we want to output all numbers from `0` to `10`.
With our current knowledge, we have two ways to accomplish:

1. Using a `while` loop with a counter variable:
   ```python
   i = 0
   while i <= 10:
       print(i)
       i = i + 1
   ```

2. Using a `for` loop with a List Literal Expression:
   ```python
   for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
       print(i)
       i = i + 1
   ```

But there is a better way in Python to do this: The `range()` expression.
In fact, there are three different ways to use `range()`:

| Syntax                                              | Description                                      | Example                                    | Result                          |
|-----------------------------------------------------|--------------------------------------------------|--------------------------------------------|---------------------------------|
| `range(stop)`                                       | Generates numbers from 0 up to, but not including, `stop` | `range(5)`                                 | `[0, 1, 2, 3, 4]`                |
| `range(start, stop)`                                 | Generates numbers from `start` up to, but not including, `stop` | `range(2, 7)`                              | `[2, 3, 4, 5, 6]`                |
| `range(start, stop, step)`                           | Generates numbers from `start` up to, but not including, `stop` with a step of `step` | `range(1, 10, 2)`                         | `[1, 3, 5, 7, 9]`                |

Using it in conjunction with the `for` loop, we can achieve the same goal with the following:

```python
for i in range(0, 11):
    print(i)
```
**Output**
```console
0
1
2
3
4
5
6
7
8
9
10
```

Instead of just counting up numbers, we can also simply repeat a task `x` times:

```python
for i in range(0, 5):
    print("Hello World")
```
**Output**
```console
Hello World
Hello World
Hello World
Hello World
Hello World
```

## Loop Control using `continue` and `break`

### `continue`

`continue` statements are exclusively used inside loops.
When the program execution reaches a `continue` statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.
(This is also what happens when the execution reaches the end of the loop.)

```python
for i in range(1,10):
    if i == 7:
        continue
    print(i)
```
**Output**
```console
0
1
2
3
4
5
6
8
9
```

Notice how the output does not contain `7`.
Since we the `if` condition evaluates to `True` for `i` = `7`, the `continue` statement is executed.
As such, we jump back to the beginning of the loop and continue with the next number (`8`).
This results in the `print(i)` statement being skipped.

The same works for `while` loops.
Using continue inside a `while` loop skips over the rest of the code block and goes back to the `while` loop's condition, checks it, and executes the code block again if the condition evaluated to `True`.
If the condition evaluates to `False`, we exit the loop and the rest of the program is executed as usual.

The following script creates the same output as shown above in the `for` loop example:

```python
i = 0
while i < 10:
    if i == 7:
        i = i + 1
        continue
    print(i)
    i = i + 1
```

### `break`

Like `continue` statements, `break` statements are used inside loops.
When the execution reaches a break statement, it immediately stops and exits the loop.
Unlike `continue`, the execution does not jump back to beginning of the loop, but instead skips over the rest of the code block and leaves the loop entirely.

A classical example is a `while True` loop, which would run indefinitely, since the condition is always `true`.
However, with the `break` statement we can use an `if` statement inside the `while` loop to exit the loop once we reach the number `7`.

```python
i = 0
while True:
    if i == 7:
        break
    print(i)
    i = i + 1
```
**Output**
```console
0
1
2
3
4
5
6
```

> [!TIP]
> If you happen to run into an infinite loop, you can kill the program by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd> inside the Terminal.
