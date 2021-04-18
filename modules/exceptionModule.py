def dividedByZero(num):
    num /= 0
    return num

def isItName(name):
    raise NameError("Invalid name!")

def negativeNumberRaise():
    print("\nGive me a number and i will throw an error if it's negative: ", end=" ")
    num=int(input())
    if num<0:
        raise ValueError("Negative number!")

def assertExample():
    temp = -10
    print("\nTemperature: " + str(temp), end=", ")
    assert (temp >= 0), "colder than absolute zero!"

def main():
    try:
        print(dividedByZero(7))
    except ZeroDivisionError:
        print("\nCan't be divided by zero")
    #except: catch every single error
    finally:
        print("This code will run no matter what")

    try:
        isItName("Name")
    except:
        print("Invalid name!")

    try:
        negativeNumberRaise()
    except Exception as e:
        print(e)

    try:
        assertExample()
    except Exception as e:
        print(e)