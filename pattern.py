
# printing square with stars
def squareprint(N):
    for i in range(N):
        for j in range(N):
            print("*",end='')
        print()
# print(squareprint(5))


# triangle pattern using stars(*)

def triangle(N):
    for i in range(N):
        for j in range(i+1):
            print("*",end='')
        print()
# print(triangle(5))


# printTriangle() which takes an integer n  as the input

def trianglewithnum(N):
    for i in range(N):
        num=1
        for j in range(i+1):
            print(num,end='')
            num+=1
        print()
# print(trianglewithnum(5))


def Numberpyramid(N):
    for i in range(N):
        n=i+1
        for j in range(i+1):
            print(n,end='')
        print()
# print(Numberpyramid(5))


# triangle in reversed order
def triangleReverse(N):
    for i in range(N,0,-1):
        # print(i)
        for j in range(i):
            print("*",end='')
        print()
# print(triangleReverse(5))


#  printTriangle in reversed which takes an integer n  as the input


def trianglenumreversed(N):
    for i in range(N,0,-1):
        num=1
        for j in range(i):
            print(num,end='')
            num+=1
        print()
# print(trianglenumreversed(5))

# print a centered triangle of asterisks with N rows.
def Triangle(N):
    for i in range(N):
        for j in range(N-i-1):
            print(" ",end='')
        for j in range(2*i+1):
            print("*",end='')
        print()
# print(Triangle(5))

# print a centered triangle in reversed of asterisks with N rows
def triangle(N):
    for i in range(N):
        for j in range(i):
            print(" ",end='')
        for j in range(2*(N-i)-1):
            print("*",end='')
        print()
# print(t(5))

