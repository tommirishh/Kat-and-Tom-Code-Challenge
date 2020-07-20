
def sort_list(list):

    productList = []
    product = 1

    for i in list:
        product *= i

    for i in range(len(list)):
        productList.insert(0,int(product/list[-1]))
        list.insert(0,list.pop())

    return(productList)

print(sort_list([1,2,3,4,5]))

print(sort_list([3,2,1]))


def sort_list_no_division(list):

    productList = []

    for i in range(len(list)):
        
        product = 1
        popped = list.pop()
        print(list)
        for i in list:
            product *= i
        
        productList.insert(0,product)

        list.insert(0,popped)


    return(productList)

print(sort_list_no_division([1,2,3,4,5]))

print(sort_list_no_division([3,2,1]))