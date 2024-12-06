# Bubble Sort
array = list(map(int, input("Give Array: ").split()))
length = len(array)
counter = 0
while(counter != length-1):
    counter = counter + 1
    print("Pass ",counter)
    for index in range(0,length-1):
        if(array[index] > array[index + 1]):
            array[index], array[index + 1] = array[index+1], array[index]
            print(array)
