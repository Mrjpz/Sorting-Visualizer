import random

# Set the range of random numbers
lower_limit = 1
upper_limit = 1000

# Create a list of numbers in the specified range
numbers = []
for i in range(469):
    numbers.append(random.randint(lower_limit, upper_limit))



# Shuffle the list to get random order
random.shuffle(numbers)
