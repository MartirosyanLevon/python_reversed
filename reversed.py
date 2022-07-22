from range_manualy import range_manualy


def reversed_manualy(lst):
    for i in range_manualy(len(lst), 0, -1):
        yield lst[i - 1]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in reversed_manualy(a):
        print(i)
