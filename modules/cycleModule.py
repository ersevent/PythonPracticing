def cycleModule():
    lista = [4, 5, 8, 12, 3, 0]

    print("\nprint even numbers till 13:", end=" ")
    index = 0
    while index<=13:
        if index%2==0:
            print(index, end=" ")
        index+=1

    print("\n\nprint even numbers till 13 and skip number 4:", end=" ")
    index = 0
    while index<=13:
        if index%2==0:
            if index==4:
                index+=1
            else: print(index, end=" ")
        index+=1

    print("\n\n" + str(lista), end=" ")
    num=3
    print("numbers that cant be divided by " + str(num) + ": " + str(), end=" ")
    for i in lista:
        if i%num==0:
            continue
        else: print(i, end=" ")

    print("\n\n" + str(lista), end=" ")
    index=0
    num=0
    print("elements till the first appearance of number 0: ", end=" ")
    for i in lista:
        if i==num:
            print("\n")
            break
        else:
            print(i, end=" ")

    print("cycle with range: ", end=" ")
    num=12
    for i in range(num):
        print(i, end=" ")
    print()