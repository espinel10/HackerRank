###URL https://www.hackerrank.com/challenges/an-interesting-game-1/problem

def gamingArray(arr):
    maxval = 0
    maxarr = {}
    newarr = {}
    for index,value in enumerate(arr):
        maxval = max(value,maxval)
        maxarr[index] = maxval
        newarr[value] = index
    bobwin = False
    while index >= 0:
        maxval = maxarr[index]
        index  = newarr[maxval]-1
        bobwin = not bobwin
    return "BOB" if bobwin else "ANDY"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
