def pyramid(asinout):
    for i in range(asinout):
        for j in (asinout -i -1):
            print (" ", end="")
        for k in ( 2 * i +1 ):
            print ("*", end="")
            print ()
asinout=5
pyramid(asinout)


