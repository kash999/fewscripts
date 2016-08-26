from random import choice

nicks = 'Victoria kash Jhon Tim Jemma Ian Andy Spman Ironman'.split()
run = 10000000

r = map(lambda x: '{0} =  {1} is {2:.2f}%'.format(x[0], x[1], (float(x[1]) / (run / 100))),  [(a, ' '.join([choice(nicks) for i in range(0, run)]).count(a)) for a in nicks])

print '\n'.join(r)
