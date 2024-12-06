#Insertion Sort
unsorted_arr = list(map(int, input("Give Array: ").split()))
length = len(array)
counter = 0
print(array)
sorted_arr = []
while(len(unsorted_arr)!=0):
    new_item = unsorted_arr.pop(0)
    if len(sorted_arr)== 0:
        sorted_arr.append(new_item)
    else:
        index=0
        insert_ind = index
        for item in sorted_arr:
            if item<new_item:
                insert_ind = insert_ind+1
            elif item>new_item:
                break
            index=index+1
        sorted_arr.insert(insert_ind, new_item)
    counter=counter+1
    print("SORTED", sorted_arr)
    print("UNSORTED", unsorted_arr)
