import random

# Set the range of numbers
lower_limit = 1
upper_limit = 950

# Create a list of numbers in the specified range
numbers = []
for i in range(627):
    numbers.append(random.randint(lower_limit, upper_limit))



# Shuffle the list to get random order
random.shuffle(numbers)
