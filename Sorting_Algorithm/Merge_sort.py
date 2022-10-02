def merge_sort(arr):

    if len(arr)>1:

        mid=len(arr)//2
        left_arry=arr[:mid]
        right_array=arr[mid:]

        merge_sort(left_arry)
        print(left_arry)
        merge_sort(right_array)

        l,r,k=0,0,0


        while l<len(left_arry) and r<len(right_array):
            if left_arry[l]<=right_array[r]:
                arr[k]=left_arry[l]
                l+=1
            else:
                arr[k]=right_array[r]
                r+=1
            k+=1

        while l<len(left_arry):
            arr[k]=left_arry[l]
            l+=1
            k+=1
        while r<len(right_array):
            arr[k]=right_array[r]
            r+=1
            k+=1

        return arr


l=list(map(int,input().split()))
n=len(l)
print(merge_sort(l))
