list = []

for i in range(4):
    listInp = int(input('enter a number'))
    list.append(listInp)

num = input('Please the sum you wish to find')
print(list)

for i in range(len(list)-1):
    print(list[0] + list[i+1])

for i in range(len(list)-2):
    print(list[1] + list[i+2])

for i in range(len(list)-3):
    print(list[2] + list[i+3])