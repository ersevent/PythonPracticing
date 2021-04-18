from modules.cycleModule import cycleModule
from modules.listModule import listModule
from modules.basicModule import basicModule
from modules.functionModule import main as mainFunctionModule
from modules.exceptionModule import main as mainExceptionModule
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
    print("Select a module with number (type help for commands): ", end=" ")
    
    try:
        module = input()
        if(module=="help"): 
            commandHelp()
        elif(int(module)==0):
            sys.exit()
        elif(int(module)==1):
            basicModule()
        elif(int(module)==2):
            listModule()
        elif(int(module)==3):
            cycleModule()
        elif(int(module)==4):
            mainFunctionModule()
        elif(int(module)==5):
            mainExceptionModule()
        else: print("\nWrong module number!")
    except ValueError:
        print("Invalid input!")



