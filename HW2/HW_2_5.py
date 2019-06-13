def chain(*args):
    for it in args:
        for j in it:
            yield j


def iterator(start=0, stop=0):
    for i in range(start, stop):
        print(i)


for x in chain(range(3), range(1, 4), range(2, 5)):
    print(x)