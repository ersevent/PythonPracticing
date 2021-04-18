def listModule():
    lista = [4, 5, 8, 12, 3, 0]

    print("\nlista: " + str(lista))

    print("\nlista: " + str(lista) + ", 3rd element in lista: " + str(lista[2]))

    lista.append(9)

    print("\nlista: " + str(lista) + " with 9 at the end")

    listb = lista.copy()
    listb.insert(2, 21) 

    print("\nlistb: " + str(listb) + " with number 21 at the 2nd index")

    listb.remove(3)
    
    print("\nlistb: " + str(listb) + " with removed number 3")

    del listb[2]

    print("\nlistb: " + str(listb) + " with removed index 2")