list = []

for i in range(4):
    listInp = input('enter a number')
    list.append(listInp)

num = input('Please the sum you wish to find')

for i in range(len(list)):
    temp = list[i]
    if temp+list[i+1] == num:
        print(temp, '+', list[i+1])