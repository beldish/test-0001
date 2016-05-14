def ttt(num):
    for i in range(num):
        yield i**2

for i in ttt(55):
    print i