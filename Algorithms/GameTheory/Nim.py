##URL https://www.hackerrank.com/challenges/tower-breakers-1/problem
import sys

def nimGame(pile):
    result=pile[0]
    for i in range(0,len(pile)-1):
        result=result^pile[i+1]

    if result==0:
        return 'Second'
    else:
        return 'First'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
