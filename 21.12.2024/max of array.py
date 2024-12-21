
   
def find_maximum(arr, n):
    # Function to find the maximum in the array
    max_value = arr[0]
    for i in range(1, n):
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value


def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum(arr, n))
    
main()
