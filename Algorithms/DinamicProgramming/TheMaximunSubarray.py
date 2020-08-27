import sys
##URL https://www.hackerrank.com/challenges/maxsubarray/problem
def run(entrada):
    max_ending_here =entrada[0]
    mayor=entrada[0]
    x=0
    y=0
    mayor2=entrada[0]
    for i in range(1,len(entrada)):
        max_ending_here=max_ending_here+entrada[i]
        max_ending_here=max(entrada[i],max_ending_here)
        if mayor < max_ending_here :
            mayor =max_ending_here
            if max_ending_here==entrada[i]:
                mayor2=entrada[i]
            else:
                if entrada[i]>0:
                    mayor2=mayor2 + entrada[i]

    print(mayor)
    print(mayor2)

#entrada=[-2,-5,6,-2,-3,1,5,-6]
entrada=[2,3,4,5,7]
print(entrada)
run(entrada)
