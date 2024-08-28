
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
print(triangle(5))