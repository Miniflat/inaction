def my_count(start, step=1):
    i = start
    print(i)
    while True:
        i += step
        yield i


for x in my_count(5, 2):
    print(x)

