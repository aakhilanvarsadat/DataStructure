#Binary Search
def binary(array, num):
    print(array)
    mid = int(len(array)/2)
    print(mid)
    if(len(array)==1):
        if array[0]!=num:
            print("Num not found")
            return -1
        else:
            print("Num found at index 0")
    if array[mid] == num:
        print(f"Number found at index {mid}")
        return mid
    elif num < array[mid]:
        # print(array[:mid])
        binary(array[:mid], num)
    else:
        # print(array[mid:])
        binary(array[mid:], num)
array = list(map(int, input("Give Array: ").split()))
num = int(input("Enter a num to be searched: "))
binary(array, num)
