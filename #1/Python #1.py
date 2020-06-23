list = []

for i in range(4):
    listInp = int(input('enter a number'))
    list.append(listInp)

num = int(input('Please the sum you wish to find'))
print(list)

for i in range(len(list)-1):
    if (list[0] + list[i+1]) == num or (list[1]) + list[i+2]) == num or (list[2]):
        print(list[0], '+', list[i+1], '=', num)

