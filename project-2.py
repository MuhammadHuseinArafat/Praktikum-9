#project 2
def bintang(n):
    a = 0
    b = -1
    for a in range (1,9,2):
        a += 1
        b += 2
        bil = '*' * b
        print (bil.center(n+n))

bintang(4)
   

