
# printing square with stars
def squareprint(N):
    for i in range(N):
        for j in range(N):
            print("*",end='')
        print()
print(squareprint(5))