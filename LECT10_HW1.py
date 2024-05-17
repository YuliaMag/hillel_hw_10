import random


def get_random_string(length=10):
    val = [chr(i) for i in range(128) if chr(i).isalnum()]
    result = "".join(random.choices(val, k=length))
    return result


print(get_random_string())
print(get_random_string(100))
