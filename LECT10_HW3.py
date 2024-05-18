def custom_zip(*iterables, full=False, default=None):
    if not iterables:
        raise TypeError("Error!")
    try:
        if full is False:
            iterables = [iter(i) for i in iterables]
            while True:
                yield tuple([next(i) for i in iterables])
        else:
            def Q(x):
                for item in x:
                    yield item
                while True:
                    yield default

            longs = [Q(x) for x in iterables]
            for _ in range(max(map(len, iterables))):
                yield tuple(next(i) for i in longs)
    except StopIteration:
        return


# ================================================ #
# Function test:

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
print(list(custom_zip(seq1, seq2))) # [(1, 9), (2, 8), (3, 7)]
print(list(zip(seq1, seq2)))

print(list(custom_zip(seq1, seq2, full=True, default="Q")))  # [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
print(list(custom_zip(seq1, seq2, full=True))) # [(1, 9), (2, 8), (3, 7), (4, None), (5, None)]

