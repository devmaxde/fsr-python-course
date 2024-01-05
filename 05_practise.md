
# Python Programming Tasks with Hints

## Task 1: Username Checker
Write a program that asks the user to enter a username. If the username is less than 5 characters long, print "Username is too short". If it's more than 15 characters, print "Username is too long". Otherwise, print "Username is valid".


## Task 2: Number Guessing Game
Develop a simple number guessing game. The program should generate a random number between 1 and 10 and ask the user to guess it. Inform the user if their guess is too high, too low, or correct.

```python3
def get_random_number(max_num):
    import random
    return random.randint(1, max_num)
```

## Task 3: Multiplication Table Printer
Create a script that asks the user for a number and prints the multiplication table for that number up to 10 (e.g., if the user enters 3, then print the 3 times table).


<details>
<summary>Hint</summary>
Inside the loop, multiply the user's number by the current number in the loop's range.
</details>


## Task 5: Count Character Occurrences
Write a script that asks the user to enter a sentence and then counts and prints the number of vowels in that sentence.

<details>
<summary>Hint 1</summary>
Use a dictionary to store the vowels and their counts.
for example:

```python
data = {
    "a": 0,
    "b": 3
}
```
</details>

## Task 6: Fibonacci Sequence Generator
Develop a program that asks the user how many Fibonacci numbers to generate and then generates them. The Fibonacci sequence is a series of numbers where the next number is the sum of the two preceding ones, usually starting with 0 and 1.