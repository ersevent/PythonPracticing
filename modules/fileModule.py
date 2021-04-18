def fileWriteExample():
    file = open("files/example.txt", "w")
    file.write("exaple text")
    print("\nWriting to file was successful!")
    file.close()

def main():
    fileWriteExample()