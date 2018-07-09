arr=[]
n=int(input("enter the size of the list :"))
for i in range(0,n):
      temp=input("enter the number to array to be sorted: ")
      arr.append(temp)
print("the unsorted array is",arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            var=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=var
print("the sorted array is")
for i in range(0,n):
    print arr[i]   
