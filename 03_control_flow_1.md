> [!NOTE]
> **Recap**
>
> 1. What is the defining property of an expression?  
>    _↳ An expression **always** evaluates to a single value_
> 2. What kind of expression can't be split into further expressions?  
>    _↳ Literal expressions_
> 3. Solve the following expression.
>    ```python
>        s = "hello world"
>        (10 + 5 // 3 - 3) / 4 + len("7" * s.index("w")) + s[2:9].count("l")
>    ```
>    _↳ `10.0` (of `float` data type)_

# Control Flow

## The "Boolean" data type (`bool`)

While the integer, floating-point, and string data types have an unlimited number of possible values, the Boolean data type has only two values: `True` and `False`.

> [!TIP]
> The boolean literals `True` and `False` have to be capitalized.
> Also not to be confused with the **string** literals `"True"` and `"False"` (marked by the double quotes).

The Boolean data type is a subclass of the integer data type, meaning every Boolean is also an integer (but **not** vice versa!)

`False` is equivalent to `0` and `True` is equivalent to `1`.

As a result, any arithmetic expression (like `x + y`) can also use Booleans instead of the numeric data types.
By extension, wherever an integer is valid, you can always use a Boolean.

```console
>>> True + True
2
```


### Comparison Expressions

Let `x` and `y` be any expression, and `s` be an expression of a sequence data type (e.g. `string`).
We define the following **comparison expressions**:

| Expression  | Operation                               | Example                     | Result |
|-----------|-------------------------------------------|-----------------------------|--------|
| `x == y`  | Equal to                                  | `5 == 5`                    | `True` |
| `x != y`  | Not equal to                              | `5 != 3`                    | `True` |
| `x < y`   | Less than                                 | `10 < 15`                   | `True` |
| `x > y`   | Greater than                              | `20 > 18`                   | `True` |
| `x <= y`  | Less than or equal to                     | `8 <= 8`                    | `True` |
| `x >= y`  | Greater than or equal to                  | `25 >= 30`                  | `False`|
| `x in s`  | Membership (x in a sequence s)            | `'a' in 'hello'`            | `False`|
| `x not in s` | Negated membership (x not in a sequence s) | `'z' not in 'hello'`       | `True` |

> [!TIP]
> Values of different types, except different numeric types, never compare equal.
> e.g. `5 == "5"`, evaluates to `False`. However, `5 == 5.0` evaluates to `True`.

> [!CAUTION]
> Do not confuse `x == y` *(comparison expression)* with `=` *(assignment statement)*
> ```console
> >>> 5 == "5"
> false 
> ```
> `5` (`integer`) and `"5"` (`string`) are different data types

### Logical Expressions

Let `x` and `y` be expressions of the boolean data type.
We define the following **logical expressions**:

| Expression  | Operation                           | Example                          | Result |
|-----------|---------------------------------------|----------------------------------|--------|
| `x and y`     | Logical AND                           | `True and False`                 | `False`|
| `x or y`      | Logical OR                            | `True or False`                  | `True` |
| `not x`     | Logical NOT                           | `not True`                      | `False`|


## Interacting with the Terminal

### Input: The `input()` Expression

Until now we have only used fixed values, that we defined as a literal expression at some point.
Chances are, you want to receive inputs from the user.

To do that, we can use the `input()` Expression.
It pauses the program and waits for the user to input some text.
Once the user confirms their input by pressing <kbd>Enter</kbd>, the expression evaluates to that text.

```console
>>> input()
Hello # <-- type here, then press Enter
'Hello'
```

```console
>>> input("Please enter your name: ")
Please enter your name: John # <-- type here, then press Enter
'John'
```

We can optionally provide a prompt, by inserting a string expression inside the parantheses

### Output: The `print()` Statement

Inside the Interactive Shell, we always conveniently get the result of an expression displayed.
However, this is not the case when executing a Python-Script/`.py`-file

The `print()` statement takes any string expression inside the parantheses, and outputs it to the terminal.

```console
>>> print("Hello")
Hello
```

> [!TIP]
> `print()` is a statement, **not** an expression.
> The `Hello` you see in the interactive shell is **not** the result of an expression.
> It just immediatly executes the `print()` statement, which displays text without representing a value.

[^1]


## Programming a Python-Script

Up until now we only used the Interactive Shell to evaluate expressions and create variables using assignment statements.
With the basics covered, we are ready to leave the interactive shell and start writing proper programs.

A Python-Script is a file with a `.py` suffix, e.g. `my_first_script.py`.
Avoid using spaces in your filename.
Use underscores (`_`) instead.
a series of instructions (i.e. statements and expressions) to execute.

You can open the file in any text editor you desire.
It's recommended to use either [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/), which we installed in the first course.

**`my_first_script.py`**
```python
name = input("Please enter your name: ")
print("Your name is " + name)
```

Execute it by running the following command
```console
python3.12 my_frst_script.py
```

> [!TIP]
> Depending on the Operating System and/or Python version you have installed the exact command may differ slightly.
> If the command above does not work, you can also try one of the following:
> ```console
> python my_frst_script.py
> ```
> ```console
> python3 my_frst_script.py
> ```

The program will display `Please enter your name: ` and wait for the user to input some text.
Once confirmed by pressing <kbd>Enter</kbd> the resulting string is then stored in the `name` variable, which then again is being displayed in the terminal with the text `Your name is <xyz>`, where `<xyz>` is the name you typed into the terminal before.


## Conditional Code Execution (`if`, `else` and `elif`)

### Simple Statements vs. Compound Statements

Expanding upon the definition of a **Statement**, we introduce two subclasses of statements:

1. **Simple Statements** 
2. **Compound Statements**

A **simple statement** is comprised within a single logical line.
For example the assignment statement is a simple statement[^2].

Unlike simple statements, **compound statements** contain (groups of) other statements; they affect or control the execution of those other statements in some way. In general, compound statements span multiple lines, although in simple cases a whole compound statement may be contained in one line[^3].

> [!Tip]
> A **block of code** or **code block** are one or more lines of code, that share the same indentation.
> Python uses the indentation to determine, whether a line of code belongs to a block or not.

### `if` statement

An `if` statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the condition is False.

In plain English, an `if` statement could be read as, “If this condition is true, execute the code in the clause.”
In Python, an if statement consists of the following:

- The `if` keyword
- A condition (that is, an expression that evaluates to `True` or `False`)
- A colon (`:`)
- Starting on the next line, an indented block of code

> [!TIP]
> Indentation is used to create a code block, that is executed or skipped depending on the `if` statement's condition.

```python
name = input()

if name == "Alice":
    print("You are Alice")
```

<img src="/assets/03_if.svg" width="520" />

### `else` clause

An `if` statement can optionally be followed by an `else` clause, which is only executed when the `if` statement's condition is `False`.
In plain English, an `else` clause could be read as, “If this condition is true, execute this code. Or else, execute that code.”

```python
name = input()

if name == "Alice":
    print("You are Alice")
else:
    print("You aren't Alice")
```

<img src="/assets/03_if_else.svg" width="588" />

### `elif` clause

```python
name = input()
age = int(input())

if name == "Alice":
    print("You are Alice")
elif age >= 21:
    print("You aren't Alice, but you are allowed to drink")
else:
    print("You are neither Alice nor drinking age")
```

<img src="/assets/03_if_elif_else.svg" width="780" />

This creates a distinction between 3 cases, only **one** of which is ever executed.

1. `name == Alice` (The name is Alice)
2. `name != Alice` and `age >= 21` (The name isn't Alice and the age is >= 21)
3. `name != Alice` and `age < 21` (The name isn't Alice and the age is < 21)

### `if` and `elif` are **not** equivalent

If you are wondering whether `elif` and `if` are equivalent, consider the following code:

```python
name = input()
age = int(input())

if name == "Alice":
    print("You are Alice")
if age >= 21:
    print("You aren't Alice, but you are allowed to drink")
else:
    print("You are neither Alice nor drinking age")
```

<img src="/assets/03_if_if_else.svg" width="720" />

This code does indeed behave differently to the one before.
If you set the name to `Alice` and age to something above or equal to `21`, e.g. `23`, you will get two outputs:

```
You are Alice
You aren't Alice, but you are allowed to drink
```

Let's add an empty line between the two `if` statements to see what's happening here:

```python
name = input()
age = int(input())

if name == "Alice":
    print("You are Alice")

if age >= 21:
    print("You aren't Alice, but you are allowed to drink")
else:
    print("You are neither Alice nor drinking age")
```

Unlike before, where we used `elif`, the `age >= 21` condition is checked regardless if `name` was Alice or not.
Likewise, the `else` clause is attached to the age check and completely independent of the Alice name check.

We no longer have three distinct cases, but rather two sequential statements with two distinct cases each.

The first statement has the following two cases:

1. `name == Alice` (The name is Alice), so print `You are Alice`
2. `name != Alice` (The name isn't Alice), so do nothing (since there is no `else` clause)

The second statement differentiates between these:

1. `age >= 21` (The age is greater than or equal to 21), so print `You aren't Alice, but you are allowed to drink`
2. `age < 21` (The age is below 21), so print `You are neither Alice nor drinking age`

Changing the print statements to reflect the functionality of the code, it should look something like this:

```python
name = input()
age = int(input())

if name == "Alice":
    print("You are Alice")

if age >= 21:
    print("You are allowed to drink")
else:
    print("You are not allowed to drink")
```

And if we add an `else` clause to the first `if` statement, we could do the following:

```python
name = input()
age = int(input())

if name == "Alice":
    print("You are Alice")
else:
    print("You aren't Alice")

if age >= 21:
    print("You are allowed to drink")
else:
    print("You are not allowed to drink")
```

[^1]: [The Python Standard Library: Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-functions)
[^2]: [The Python Language Reference: Simple Statements](https://docs.python.org/3/reference/simple_stmts.html#simple-statements)
[^3]: [The Python Language Reference: Compound Statements](https://docs.python.org/3/reference/compound_stmts.html#compound-statements)

