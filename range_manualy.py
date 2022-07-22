def range_manualy(stop, start=0, step=1):
    if step > 0:
        if start > stop:
            stop, start = start, stop
        while start < stop:
            yield start
            start += step


    elif step < 0:
        if stop > start:
            start, stop = stop, start
        while start > stop:
            yield start
            start += step


if __name__ == "__main__":
    for i in range_manualy(10, 20, -1):
        print(i, end=' ')

    for i in range_manualy(10, 0):
        print(i)
