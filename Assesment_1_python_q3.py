
input_string =input('Enter your new order separated by space ')
new_order =input_string.split()
mydict ={}
for i in range(len(new_order)):
    mydict[new_order[i]] = i



input_string =input('Enter your strings separated by space ')
StringList =input_string.split()

def check(str1, str2):
    size= min(len(str1),len(str2))
    for i in range(size):
        if mydict[str1[i]]< mydict[str2[i]]:
            print(str1, str2, i)
            return False
        elif mydict[str1[i]]> mydict[str2[i]]:
            return True
    if(len(str1)>len(str2)):
        return True
    else:
        return False

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
                if check(arr[j],arr[j+1]):

                    arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr
print(bubbleSort(StringList))
