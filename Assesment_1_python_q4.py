n = int(input('Number of pairs '))

my_dict = {}
my_dict[0] = []
x = 0

def check(s, j):
    if(s in my_dict[j]):
        return True
    return False

for i in range(n):
    input_string =input('Enter your pair with strings separated by space ')
    my_list =input_string.split()
    flag = 0
    for j in range(x+1):
        if check(my_list[0], j) or check(my_list[1], j):
            if(check(my_list[0], j)):
                my_dict[j] = my_dict[j] + [my_list[1]]
            else:
                my_dict[j] = my_dict[j] + [my_list[0]]
            flag = 1
            break

    if flag == 0:
        if(i!=0):
            x=x+1
        else:
            x = 0
        my_dict[x] = []
        print(my_dict)
        my_dict[x] = my_dict[x] + my_list



print(my_dict)

print('There are ' + str(len(my_dict)) + ' groups')

input_string =input('Enter your pair to find if they are connected with strings separated by space ')
my_list =input_string.split()
flag = 0
for j in range(x+1):
    if check(my_list[0], j) and check(my_list[1], j):
        flag = 1
        break

if(flag == 1):
    print(my_list[0] + ', ' + my_list[1] + ' belong to the same group')
else:
    print(my_list[0] + ', ' + my_list[1] + ' do not belong to the same group')
