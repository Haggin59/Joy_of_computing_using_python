def binary_search(l,x,start,end):
    if start == end:
        if l[start] == x:
            return start
        else:
            return -1
    else:
        mid = (start + end)//2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            return binary_search(l,x,start,mid-1)
        else:
            return binary_search(l,x,mid+1,end)

a = [1,3,5,6,7,9,10]
print(binary_search(a,1,0,6))                    
