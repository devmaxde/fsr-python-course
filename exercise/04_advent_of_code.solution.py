#---------------#
# Prerequisites #
#---------------#

# The example inputs represented as a list of strings
eingaben = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

# Use a helper variable for digit checking later
numbers = "1234567890" 

#------------#
# Solution 1 #
#------------#

# Idea:
# (1) Loop over all symbols per input
# (2) Check if the symbol is a digit
# (3) Store it in a list IF it is
# (4) Extract the first and last digit in the list respectively
# (5) Concatenate (not add) both digits to create a new number
# (6) Do steps 1 - 4 for every input and sum up the numbers

sum = 0 # Store 0 in a new variable called sum (6)

for eingabe in eingaben: # Loop over all inputs (6)

    found_digits = [] # Create an empty list called found_digits for later (3)

    for symbol in eingabe: # Loop over all symbols of the input string (1)
        if symbol in numbers: # Check if it is a number by using our helper variable we created earlier (2)
            found_digits.append(symbol) # Store the found symbol in found_digits (3)

    first_digit = found_digits[0] # Get the first element in found_digits (4)
    last_digit = found_digits[-1] # Get the last element in found_digits (4)

    concatenated_digits = int(first_digit + last_digit) # Concatenate the digits and convert it to an integer (5)

    sum = sum + concatenated_digits # Sum up all numbers (6)

# Print the result
print(sum)
