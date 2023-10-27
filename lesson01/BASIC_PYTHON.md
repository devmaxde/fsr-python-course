# Basics
## Syntax
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

```python
x = 5    # Variable named x with the value 5
y = "Johannes"
```

But still, a variable still has a type. you can print it using the following command
```python
x = 5
print(type(x)) # result <class 'int'>
print(type(y)) # result <class 'str'>
```

You can use the input command to Ask the user for his input.
````python
z = input("Please input ur name: ")
print("Welcome ", z)
````

## Controlling the Program

### If Statements
You can use If Statements to execute commands, if the condition is matched
````python

x = input("Your Name: ")

if x == "Hans":
    print("Hans is back in de Hoood :D")
else:
    print("Welcome ", x)
````

As you can see i the Example, the first print will only be triggerd, if the input name is Hans.
The default type of the input is a String. An if Statement will only be triggerd, if the input is a Boolean and the value is True.
You can create booleans by logic operations. For example:

```python
x = 3 > 2
y =  99 > 2
print(x) # True
print(type(x)) # <class 'bool'>

# These Boolean Values ca be used to trigger an if Statement

if x:
    print("3>2 is True")

if not y:
    print("This Statement will be triggerd, because the y is inverted")

```

### Converting Types

```python

a = "5"
print(type(a)) # <class 'str'>

b = int(a)

print(type(b)) # <class 'int'>

```