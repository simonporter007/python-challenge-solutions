
import itertools
# View code for our initial hint gives us the clue to a ternary system, each number describing the last
# a = [1, 11, 21, 1211, 111221 ...

# Generate the sequences up until 30
x = '1'
for i in range(30):
    x = "".join([str(len(list(j))) + i for i, j in itertools.groupby(x)])

print(len(x))
