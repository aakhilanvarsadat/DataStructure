#IMPROVED Insertion Sort
array = list(map(int, input("Give Array: ").split()))
length = len(array)
counter = 1
print(array)
for index in range(0,length-1):
    new_item = array[counter]
    i=0
    for item in array[0:counter]:
        if new_item<item:
            array[index+1],array[i]=array[i],array[index+1]
        i=i+1
    counter = counter +1
    print("SORTED", array)
