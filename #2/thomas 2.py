
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