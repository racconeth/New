import random
import os

# Start with the base number
number = "+123456"

# Generate 4 random numbers
for i in range(4):
  # Append a random number to the base number
  number += str(random.randint(0, 9))

# Save the resulting number to a text file
with open(os.path.join(".", "numbers.txt"), "w") as f:
  f.write(number)
