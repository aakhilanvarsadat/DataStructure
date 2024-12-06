# Improved version of Bubble Sort, which stops iterating if the sorting is completed early
array = list(map(int, input("Give Array: ").split()))
length = len(array)
counter = 0
swap_flag = 1
while(counter != length-1):
    counter = counter + 1
    if swap_flag == 0:
        break
    print("Pass ",counter)
    for index in range(0,length-1):
        if(array[index] > array[index + 1]):
            array[index], array[index + 1] = array[index+1], array[index]
            print(array)
        else:
            swap_flag = 0
