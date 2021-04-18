from modules.cycleModule import cycleModule
from modules.listModule import listModule
from modules.basicModule import basicModule
from modules.functionModule import add, conv

basicModule()

lista = [4, 5, 8, 12, 3, 0]

listModule(lista)

cycleModule(lista)

x=7
y=8
print("\nx: " + str(x) + ", y: " + str(y) + ", x+y: " + str(add(7,8)))

print("\nGive me a celsius value: ", end=" ")
celsius = int(input())
fahrenheit = conv(celsius)
print("The converted fahrenheit value: " + str(fahrenheit))