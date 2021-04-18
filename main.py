from modules.cycleModule import main as mainCycleModule
from modules.listModule import main as mainListModule
from modules.basicModule import main as mainBasicModule
from modules.functionModule import main as mainFunctionModule
from modules.exceptionModule import main as mainExceptionModule
from modules.fileModule import main as mainFileModule

import sys

def commandHelp():
    print("\n1: Basic module")
    print("2: List module")
    print("3: Cycle module")
    print("4: Function module")
    print("5: Exception module")
    print("0: Exit")

while True:
    print("\n--------------------------------------------------------")
    print("Select a module with number (type help for module list): ", end=" ")
    
    try:
        module = input()
        if(module=="help"): 
            commandHelp()
        elif(int(module)==0):
            sys.exit()
        elif(int(module)==1):
            mainBasicModule()
        elif(int(module)==2):
            mainListModule()
        elif(int(module)==3):
            mainCycleModule()
        elif(int(module)==4):
            mainFunctionModule()
        elif(int(module)==5):
            mainExceptionModule()
        elif(int(module==6)):
            mainFileModule()
        else: print("\nWrong module number!")
    except ValueError:
        print("Invalid input!")



