def custom_map(funct, *seq):
    if not seq:
        raise TypeError("TypeError!")
    iters = [iter(s) for s in seq]
    try:
        while True:
            yield funct(*[next(i) for i in iters])
    except StopIteration:
        pass


# ================================================ #
# Function test:

def sum_(a, b):
    return a + b


lst1 = [10, 5, 0]
lst2 = [1, -2, 12, 8, 9]
print(list(custom_map(sum_, lst1, lst2)))
print(list(map(sum_, lst1, lst2)))

print(list(custom_map(lambda x: x * x, [1, 2, 3])))
print(list(map(lambda x: x * x, [1, 2, 3])))
