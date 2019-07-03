


n = int(input('Number of tuples '))
tup_list = []
for i in range(n):
    input_string =input('Enter your tuple with elements separated by space ')
    if(len(input_string)>0):
        my_list =[int(x) for x in input_string.split()]
        tup_list.append(tuple(my_list))

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):
            tup1 = arr[j]
            tup2 = arr[j+1]
            if tup1[len(tup1)-1] > tup2[len(tup2)-1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr

print(bubbleSort(tup_list))
