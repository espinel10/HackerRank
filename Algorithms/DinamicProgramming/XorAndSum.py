import sys
###URL https://www.hackerrank.com/challenges/xor-and-sum/problem
###cd Desktop/HackerRank/Algorithms/DinamicProgramming

import time
tic = time.process_time()
def run(a,b):
    memo={}
    N=314159
    sum=0
    for i in range(N+1):
        var=a^b<<i
        sum=sum+var

    sum=sum%((10**9)+7)
    print(sum)


a1=10
b1=1010
run(int(str(a1),2),int(str(b1),2))
toc = time.process_time()
print("Computation time = " + str(1000*(toc - tic )) + "ms")
