
import random
import time
Array=[]
def selection(Array):

  for i in range(len(Array)):
     mininum_index=i

     for j in range(i+1,len(Array)):

        if Array[mininum_index]>Array[j]:
            mininum_index=j
     Array[i],Array[mininum_index]=Array[mininum_index],Array[i]

n=int(input("Enter no of element:"))
for i in range(n):
    Array.append(random.randint(1,1000))
print("Unordered array:",Array)
selection(Array)
c=time.time()
print("Sorted array: ",Array)
print("Time taken",time.time()-c)
