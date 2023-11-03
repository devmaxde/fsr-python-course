# The Caesar Cipher

Given a message, each letter in the message is shifted by 10 positions in the alphabet.
The letter `a`, which is the first letter in the alphabet becomes `k`, which is the eleventh letter in the alphabet.
`b` becomes `l`, `c` becomes `m`, and so on.
Overflowing letters simply loop back around, e.g. the letter `z` becomes `j`.
For the sake of simplicity we assume only lowercase letters from `a` to `z` without umlauts, etc.
For example the message `hello` becomes `rovvy`.
To decipher a message this process can simply be reversed.

Here is a Tipp for the List:
Use the Modulo Function to prevent an overflow.
For example:
```python3
a = [1,2,3,4]

b = a[4] # Is an error. There are only 4 elements, Index 4 is out of range

c = a[4%len(a)] # This will go to the end of the List,
# if the index is bigger than the list it will start at the beginning
```
The Math:

Modulo is the rest function of the division
if you calculate 30%6 the modulo is 0, because 30 can be divided by 6
34%6 will give you 4. 34/6 = 5 rest 4 <--- Modulo result
