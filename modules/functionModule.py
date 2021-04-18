def add(x, y):
    return x+y

def conv(c):
    c = 9/5 * c + 32
    return c

def main():
    x=7
    y=8
    print("\nx: " + str(x) + ", y: " + str(y) + ", x+y: " + str(add(7,8)))

    print("\nGive me a celsius value: ", end=" ")
    celsius = int(input())
    fahrenheit = conv(celsius)
    print("The converted fahrenheit value: " + str(fahrenheit))