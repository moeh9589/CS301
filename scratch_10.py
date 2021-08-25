import time

import csv
n=int(input())

def writerfunc(n):
    with open('speedData.csv', mode='w') as results:

        results = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(0,n+1,1000):

            seconds = time.time()#*1000000

            x = testFunction(i, n)

            end = time.time()#*1000000

            results.writerow([i, (end-seconds)])

    print("Done")
    return n

def testFunction(i, n):
    newlist = []
    for i in range(n):
        newlist.append(i)

    mydict = {a: b for a, b in enumerate(newlist)}

    #for i in range():
    print (mydict)

    return mydict

writerfunc(n)

