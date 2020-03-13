# test.assert_equals(productFib(4895), [55, 89, True])
# test.assert_equals(productFib(5895), [89, 144, False])


def productFib(prod):
    No1=0
    No2=1
    NewNo=0
    total=0
    ReturnList = [0,1,True]
    if prod == 0:
        return ReturnList
    else:
        while (total < prod):
            NewNo = No1 + No2
            No1 = No2
            No2 = NewNo
            total = No1 * No2
            ReturnList[0] = No1
            ReturnList[1] = No2
            ReturnList[2] = False
            if total == prod:
                ReturnList[2] = True
        return ReturnList

print(productFib(0))
print(productFib(4895))
print(productFib(5895))


def productFib2(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
