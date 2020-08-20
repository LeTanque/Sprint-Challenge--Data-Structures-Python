import time
from binary_search_tree import BinarySearchTree

# Start the timer and open the files
start_time = time.time()
read_names_1 = open('names/names_1.txt', 'r')
names_1 = read_names_1.read().split("\n")  # List containing 10000 names
read_names_1.close()
read_names_2 = open('names/names_2.txt', 'r')
names_2 = read_names_2.read().split("\n")  # List containing 10000 names
read_names_2.close()

# List comprehension
# duplicates = [i for i in names_1 if i in names_2]

# Cache solution
duplicates = []
cash = {}
# cash = set()
# Check out sets from python docs
# intersection(*others)
# set & other & ...
# Return a new set with elements common to the set and all others.

# Put's each name in the dict
for name in names_1:
    cash[name] = True
    # cash.add(name)  # This is a set and how you add to it

# Compares each name to the name in the dict
for name in names_2:
    if name in cash:
        duplicates.append(name)


# Timer End, print results
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
