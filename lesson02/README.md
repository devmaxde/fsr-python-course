# Lesson02

### Recap

We installed Python.
You can get a user input with the input() command.
To control your Program you can use if and else Statements.
In Python there are variables. Variables have a type. You can sometimes convert one into another. (More later)

### Loops

In Python3 you can use Loops to do a task x amount of times.

There are 2 types of Loops:
 - The For Loop
 - and the while loop


 #### The For Loop
 The for loop can be used to iterate through a list. For example:

 ```python3
for i in [1,2,3,4]:
   print(i)

# Output will be:
# 1
# 2
# 3
# 4
```

The For Loop it works by going to each item in the list. It then calls the sequence and puts the current item in the i variable. The name of this variable doesn't matter.

#### The While loop
The While Loop repeats a Sequence as long as the parameter is True. For example:

```python3

while True: # This will never stop
    print("I love you")

```

You can also use it to count to 100. Here is an example.

```python3
i = 0
while i < 100:
    print(i)
    i += 1

```

#### Loop control
There are 2 python commands to control the behavior of the loop. These are break and continue.

The break command stops the loop completely and jumps to the next command.
The continue command only skips 1 iteration of the loop.

You can see it in action in the Following example. This Script should count to 10 and only display the numbers 1-3:

```python3
a = 10
while a <= -1:
    a -= 1
    if a > 3:
        continue # jump to next iteration
    
    print(a)
    if a == 1:
        break # break out of the loop immediately
```


## Lists
For a python List you don't have to set a length. You can just create them using these brackets []:

```python3
a = [1,2,3,4,5]
# you can sort a list using the sort command
# !This does not work for all types
a.sort()

# remove the last item
a.pop()


# insert an item into the list
a.insert(0, 69)


# get a list element
b = a[0] # <-- 0 is the index. Lists start with the index 0

# get the length of a list
l = len(a)
print(f"You have {l} Elements")

````