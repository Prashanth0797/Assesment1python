import sys
def binary_search(my_list, search, l, r):
    if r>= l:
        mid = l + int((r-l)/2)
        if my_list[mid] == search:
            return mid
        elif my_list[mid]>search:
            return binary_search(my_list, search, l, mid-1)
        else:
            return binary_search(my_list, search, mid+1, r)
    else:
        return -1






input_string =input('Enter your list with elements separated by space ')
search = int(input('Enter the element to be searched '))
my_list =[int(x) for x in input_string.split()]
indices = list(range(1,len(my_list)+1))



def bubbleSort(arr,indices):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                indices[j], indices[j+1] = indices[j+1], indices[j]

    return arr


my_list = bubbleSort(my_list,indices)
s =len(my_list)
if s==0:
    print('No elements present')
    sys.exit()

l = 0
r = s-1
ans = binary_search(my_list, search, l ,r)

if ans != -1:
    print('The element is found at the index ' + str(indices[ans]))
else:
    raise Exception('The element does not exist')
