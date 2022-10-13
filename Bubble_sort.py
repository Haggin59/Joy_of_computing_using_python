def bubble_sort(x):
    n = len(x)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
                
    print(x) 




x = [2,5,9,3,0]
bubble_sort(x)

