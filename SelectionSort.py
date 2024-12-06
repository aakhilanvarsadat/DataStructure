#Selection Sort
array = list(map(int, input("Give Array: ").split()))
length = len(array)
counter = 0
print(array)
while(counter != length-1):
    min_value = array[counter]
    small_ind = counter
    for index in range(counter, length):
        if(array[index] < min_value):
            small_ind = index
            min_value = array[index]
    array.pop(small_ind)
    array.insert(counter, min_value)
    counter = counter + 1
    print(array)
