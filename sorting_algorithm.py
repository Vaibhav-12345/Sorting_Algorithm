
def heapfiy(arr,n,i):
    parent=i
    l=2*parent+1
    r=2*parent+2
    
    if l<n and arr[l]>arr[parent]:
        parent=l
        
    if r<n and arr[r]>arr[parent]:
        parent=r
        
        
    if parent!=i:
        arr[i],arr[parent]=arr[parent],arr[i]
        heapfiy(arr,n,parent)
        
        
def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapfiy(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapfiy(arr,i,0)
        
        
arr=[int(i) for i in input().split()]
heapsort(arr)
# print(arr)
l=len(arr)
for i in range(l):
    print(arr[i],end=", ")
    
# for i in arr[::-1]:
#     print(i,end=", ")    



    
    
    

