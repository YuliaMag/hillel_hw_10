def sum_(a, b):
    return a + b


def custom_map(sum_, lst1, lst2):
    print(list(map(sum_, lst1, lst2)))


lst1 = [10, 5, 0]
lst2 = [1, -2, 12, 8, 9]

custom_map(sum_, lst1, lst2)
custom_map(sum_, [1, 2, 3], [3, 5, 0, 5])

