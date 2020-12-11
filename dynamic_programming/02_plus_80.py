




cache ={}

def plus_eighty(n):
    if n in cache:
        return cache[n]
    else:
        print('long time ...')
        cache[n]=n+80 
        return n+80        


print('1.',plus_eighty(10))
print('2.',plus_eighty(10))        