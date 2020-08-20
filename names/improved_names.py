import time
from binary_search_tree import BinarySearchTree
from multiprocessing import Pool
from itertools import chain, islice

# Start the timer and open the files
start_time = time.time()
read_names_1 = open('names/names_1.txt', 'r')
names_1 = read_names_1.read().split("\n")  # List containing 10000 names
read_names_1.close()
read_names_2 = open('names/names_2.txt', 'r')
names_2 = read_names_2.read().split("\n")  # List containing 10000 names
read_names_2.close()


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?




# The function to be run in parallel :
def my_func(strings):
    return [j+i for i in strings for j in listSubstrings if i.find(j)>-1]

# A small recipe from itertools to chunk an iterable :
def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

# Generating some fake & random value :
from random import randint
listStrings = \
    [''.join([chr(randint(65, 90)) for i in range(randint(1, 500))]) for j in range(10000)]
listSubstrings = \
    [''.join([chr(randint(65, 90)) for i in range(randint(1, 100))]) for j in range(1000)]

# You have to prepare the searches to be performed:
prep = [strings for strings in chunk(listStrings, round(len(listStrings) / 8))]
with Pool(4) as mp_pool:
    # multiprocessing.map is a parallel version of map()
    res = mp_pool.map(my_func, prep)
# The `res` variable is a list of list, so now you concatenate them
# in order to have a flat result list
result = list(chain.from_iterable(res))



def find_dups (set_1, set_2):
    starting = set_1 + set_2
    starting = starting[0:10]
    dups = []

    for name in map(0, starting):
        dups.append(name)

    return dups

duplicates = find_dups(names_1, names_2)

# Timer End, print results
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


