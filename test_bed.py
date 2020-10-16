import numpy as np

# Create a test vector
test = np.array([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0])
print(len(test))
# Find indexes of 1s

location = np.where(test == 1)[0]
print(location)

# Fistst 1
inicio = location.min()
# Last 1
fin = location.max()

print(f"the first 1 occurs at index {inicio}")
print(f"the last 1 occurs at index {fin}")

# How many groups of 1s?
# Expected result = 4

