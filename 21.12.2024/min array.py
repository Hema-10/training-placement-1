def maximum(arr,n):
    maxarr=arr[0]
    for i in range(1,n):
        if maxarr>arr[i]:
            maxarr=arr[i]
    return maxarr
def main():
    a=int(input("Enter number of elements you want to store:"))
    b=[]
    for i in range(a):
        c=int(input())
        b.append(c)
    print(b)
    print(maximum(b,len(b)))
    
main()
