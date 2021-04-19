def main():
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

    print("\nlist slice:")
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(squares[2:6])
    print(squares[3:8])
    print(squares[0:1])

    print("\ntumple:")
    words = ("spam", "eggs", "sausages",)
    print(words[0])

    print("\ndictionary:")
    squares = {1: 1, 2: 4, 3: "error", 4: 16,}
    squares[8] = 64
    squares[3] = 9
    print(squares)

    print("\ntumple slice:")
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(squares[:7])
    print(squares[7:])

    print("\nlist slice with step")
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(squares[::2])
    print(squares[2:8:3])

    print("\nlist slice with negative")
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(squares[1:-1])