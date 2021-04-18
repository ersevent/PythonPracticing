def fileWriteExample():
    file = open("files/example.txt", "w")
    file.write("exaple text")
    print("\nWriting to file was successful!")
    file.close()

def fileReadExample():
    file = open("files/example.txt", "r")
    print(file.readlines())
    file.close()

def commands():
    print("-read")
    print("-write")
    print("-exit")

def main():
    while True:
        print("\nWhat to do with files (type help for commands): ", end=" ")
        task=input()

        if(task=="write"):
            fileWriteExample()
        elif(task=="read"):
            fileReadExample()
        elif(task=="help"):
            commands()
        elif(task=="exit"):
            return
        else:
            print("Wrong task!")