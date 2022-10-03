def partition(arr,low,high):

    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1



def quick_Sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_Sort(arr,low,pi-1)
        quick_Sort(arr,pi+1,high)

arr=list(map(int,input().split()))
n=len(arr)

quick_Sort(arr,0,n-1)
print(arr)

