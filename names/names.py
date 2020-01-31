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


def find_dups (set_1, set_2):
    # init empty list for duplicates
    dups = []
    # init bst with empty string starting place
    bst = BinarySearchTree("")

    # for each name in the first list, insert it into the bst
    for name_1 in set_1:
        bst.insert(name_1)

    # for each name in the second list, check for it in the bst
    for name_2 in set_2:
        if bst.contains(name_2):
            dups.append(name_2)
    
    return dups


duplicates = find_dups(names_1, names_2)

# Timer End, print results
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# 64 duplicates
# Current runtime: 13.01737...
# Polynominal time O(n^c)

# improved runtime: 0.20588421821594238 seconds
# Linear, I supposed. BST complexity.
