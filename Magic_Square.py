n = int(input("Enter the order of Magic Square: "))


def Magic_Square(n):
    magicSquare = [[0 for a in range(n)] for b in range(n)]
    
    i = n//2
    j = n-1
    count = 1

    while(count<=n*n):
        if i==-1 and j==n:
            i = 0
            j = j-2
        else:
            if i == -1:
                i = n-1
            if j == n :
                j = 0

        if(magicSquare[i][j]!=0):
            i = i+1
            j = j-2
            continue
        else:
            magicSquare[i][j] = count
            count += 1
            i = i-1
            j = j+1

    for i in range(0,n):
        for j in range(0,n):
            print(magicSquare[i][j],end=" ")
        print()
    print("The sum of Row/Column/Diagonal elements are: ",(n*(n**2+1))//2) 

if n%2 == 0:
    print("Magic Square not possible")
    exit()
else:
    pass    
Magic_Square(n)    
