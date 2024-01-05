
# Python Functions

## Introduction to Functions

### Defining a Function

In Python, a function is a block of code that only runs when it is called. You can define a function using the `def` keyword, followed by the function name and parentheses `()`.

**Syntax**
```python
def function_name():
    pass # pass == do nothing
    # code block
```

### Parameters

Functions can take arguments, known as parameters, that you pass inside the parentheses. These parameters act as variables within the function.

**Syntax**
```python
def function_name(parameter1, parameter2):
    pass
    # code block using parameter1 and parameter2
```

### Parameter types
You can set the type of the parameter by adding a colon `:` and the type after the parameter name. This is called type annotation. It is not required, but it can help you to avoid errors. Keep in mind, that Python does not enforce the type of a variable.

**Syntax**
```python
def function_name(parameter1: str, parameter2: int):
    pass
    # code block using parameter1 and parameter2

function_name("Hello", 42)  # This will work


def function_2(parameter1: int):
    print(type(parameter1))
    print(parameter1)

function_2("Hello")  # This will print <class 'str'> and "Hello"
```



### Return Values

A function can return a value using the `return` statement. The function ends as soon as a `return` statement is executed, and the value is returned to the caller.

**Syntax**
```python
def function_name():
    # code block
    return "Hey there!"
```

### The `None` Value

In Python, `None` represents the absence of a value. It is commonly used to indicate that a variable has no value or that a function doesn’t explicitly return anything.

**Examples**
```python
def function_without_return():
    pass
    # code block without return statement

result = function_without_return()
print(result)  # This will print `None`
```

### Calling a Function

To call a function, use the function name followed by parentheses, including any necessary parameters.

**Syntax**
```python
function_name(parameter1, parameter2)
```

### Functions with the Same Name but Different Parameters (Overloading)

In Python, function overloading is not directly supported. If you define two functions with the same name, the second one will overwrite the first. However, you can define a function that takes different numbers of arguments using default parameters or variable-length arguments.

**Example with Default Parameters**
```python

def greg(name):
    print(f"Bye, {name}")

def greet(name, msg="Hello"): # msg is a default parameter
    print(f"{msg}, {name}")

greet("Alice")       # Uses default message
greet("Bob", "Hi")   # Uses custom message
```