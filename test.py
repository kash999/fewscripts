import os


def averageTime(first, second):
    a = map(int, first.split(':'))
    b = map(int, second.split(':'))
    av = lambda i: (a[i] + b[i]) / 2
    # c = [(a[i] + b[i]) / 2 for i in range(0, len(a))]
    c = map(av, xrange(0, 3))
    print '{0:02d}:{1:02d}:{2:02d}'.format(*c)

    s = lambda a: '%02d' % a
    return ':'.join(map(s, c))


print averageTime('00:02:20', '00:04:40')


ss = lambda a, b: (a + b) / 2

print ss(2, 4)
