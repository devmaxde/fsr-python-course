# Expressions

> [!INFO] Reminder
> Launch the **Interactive Shell** by running the `python3.12` command in your terminal.

Enter `2 + 2` into the prompt to have Python do some simple math.
After pressing <kbd>Enter</kbd> it will display the result `4` and create a new prompt `>>>` for further inputs.

```bash
>>> 2 + 2
4
>>>
```

In Python, `2 + 2` is called an **_expression_**, which is the most basic kind of programming instruction.
Expressions always evaluate (that is, reduce) down to a single value.
In the previous example, `2 + 2` is evaluated down to a single value, `4`.

## Literals

The simplest type of an expression is a **_literal_**.
A literal only consists of a single value and always evaluates to itself.

```bash
>>> 2
2
```

## Arithmetic Expressions

The expression `2 + 2` we evaluated earlier is an **_arithmetic expression_**.
An arithmetic expression consists of an **_operator_** and either one _("unary")_ or two _("binary")_ **_operands_**.
The table below shows the most commonly used arithmetic operators with `x` and `y` representing the operands.

| Operator | Operation                   | Example   | Result |
| -------- | --------------------------- | --------- | ------ |
| `x + y`  | sum of x and y              | `3 + 4`   | `7`    |
| `x - y`  | difference of x and y       | `5 - 2`   | `3`    |
| `x * y`  | product of x and y          | `2 * 5`   | `10`   |
| `x / y`  | quotient of x and y         | `10 / 4`  | `2.5`  |
| `x // y` | floored quotient of x and y | `10 // 4` | `2`    |
| `x % y`  | remainder of x / y          | `10 % 3`  | `1`    |
| `-x`     | x negated                   | `-5`      | `-5`   |
| `+x`     | x unchanged                 | `+5`      | `5`    |
| `x ** y` | x to the power of y         | `2 ** 3`  | `8`    |

Operands can not only be literal values, but any expression that evaluates to a number.
That means we can combine arithmetic expressions however we like.
The _order of operations_ (also called _precedence_) of math operators applies.

```bash
>>> 2 + 3 * 6
20
```

You may use parantheses to override the usual precedence.

```bash
>>> (2 + 3) * 6
30
```

For complex expressions Python will keep evaluating parts of the expression until it becomes a single value.

```bash
>>> (5 - 1) * ((7 + 1) / (3 - 1))
16.0
```

![Stepwise evaluation of a complex arithmetic expression in Python](assets/02_arithmetic_expressions.svg)

## Data Types

TODO

## Variables

TODO

## Bonus

Try dividing by zero and see what happens.
