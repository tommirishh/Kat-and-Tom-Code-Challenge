list = []

for i in range(4):
    listInp = int(input('enter a number'))
    list.append(listInp)

num = int(input('Please the sum you wish to find'))
print(list)

for i in range(len(list)-1):
    if (list[0] + list[i+1]) == num:
        print(list[0], '+', list[i+1], '=', num)
    try:
        if (list[1] + list[i+2]) == num:
            print(list[1], '+', list[i+2], '=', num)
    except:
        print('out of list range')
    try:
        if (list[2] + list[i+3]) == num:
            print(list[2], '+', list[i+3], '=', num)
    except:
        print('out of list range')

