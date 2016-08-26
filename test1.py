

def charlengt(s):
    a = {}

    for i in s.replace(' ',''):
        if not a.has_key(i):
        	a[i] = s.count(i)
    #p = lambda x: "%s %d" % (x[0], x[1])
    #print '\n'.join(map(p, a.items()))
    pp = lambda x:'{0} {1}'.format(*x) 
    print '\n'.join(map(pp, a.items()))


charlengt('this is a 1 string length')
