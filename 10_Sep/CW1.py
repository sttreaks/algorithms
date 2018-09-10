import random

BIN = [1, 2, 4, 8, 16, 32, 64, 124, 256, 512, 1024]


def find(ar):
    result = []
    for el in ar:
        if el in BIN:
            result.append(el)
    return result


if __name__ == "__main__":
    array = []
    for i in range(int(input(''))):
        array.append(random.randrange(1000))
    print(array)
    print(find(array))
