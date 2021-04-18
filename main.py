from modules.cycleModule import cycleModule
from modules.listModule import listModule
from modules.basicModule import basicModule
from modules.functionModule import main as mainFunctionModule
from modules.exceptionModule import main as mainExceptionModule


print("\n1: Basic module")
print("2: List module")
print("3: Cycle module")
print("4: Function module")
print("5: Exception module")
print("\nSelect a module with number: ", end=" ")

try:
    moduleNum = int(input())

    lista = [4, 5, 8, 12, 3, 0]

    if(moduleNum==1):
        basicModule()
    elif(moduleNum==2):
        listModule(lista)
    elif(moduleNum==3):
        cycleModule(lista)
    elif(moduleNum==4):
        mainFunctionModule()
    elif(moduleNum==5):
        mainExceptionModule()
    else: print("\nWrong module number!")
except ValueError:
    print("\nInvalid input!")




