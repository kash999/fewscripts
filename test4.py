

l = [[0]] * 10

print l

l[0][0] = 1

print l


def paradox():
    try:
        raise Exception("Here")
    except:
        return "There"
    finally:
        return "Or maybe there"

    return "Or it that here?"

print paradox()


word = 'abcdefghij'

print word[:3]
print word[3:]

print sum([1, 2, 3])
