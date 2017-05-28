# else
'''
for n in range(2,10):
    for i in range(2,n):
        if n % i  == 0 :
            print("{} = {}*{}".format(n,i,n/i))
        #    break

    else:
        print("{}是素数".format(n))
'''

i = 10
while i < 20:
    print(i)
    i += 1
else:
    print("i>=20")
