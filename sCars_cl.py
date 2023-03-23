#!/usr/bin/env python3
# Switch Config Access/Retreval System by MDB

import lib.hpSwitchTools as hpt

# Function Definitions

def getConfig():
    switchInfo = {
        "device_type": "hp_procurve",
        "host": input("Please enter Switch IP or FQDN: "),
        "username": "admin"
    }
    print("1) Display Config Only")
    print("2) Display and Save to File")
    saveChoice = input("Type Choice: ")
    if saveChoice != "1" or saveChoice != "2":
        print("Try again, save choice must be 1 or 2...")
        getConfig()
    switchConfig = hpt.showConf(**switchInfo)
    print(switchConfig)
    if saveChoice == "2":
        fileName = switchInfo["host"] + ".txt"
        with open(fileName, "w") as file:
            file.write(switchConfig)
        print("\nConfig saved to " + fileName)
    main()

def getVersion():
    switchInfo = {
        "device_type": "hp_procurve",
        "host": input("Please enter Switch IP or FQDN: "),
        "username": "admin"
    }
    switchVersion = hpt.showVersion
    print("\n" + switchVersion + "\n")
    main()

# Main Loop and if called as Main call

def main():
    menuChoice = 0
    print("\n\n-------------------------------------------------------")
    print("S-CARS - Switch Config Accress/Retreval System - by mdb")
    print("-------------------------------------------------------\n")
    print("1) Get Switch Config")
    print("2) Get Switch Version")
    print("3) Exit\n")
    menuChoice = input("Type Choice: ")
    if menuChoice == "1":
        getConfig()
    elif menuChoice == "2":
        getVersion()
    elif menuChoice == "3":
        print("\n\n Thank you for using S-CARS\n\n")
        exit
    else:
        print("\n>>> Please try again with a number for the option you desire <<<\n")
        main()


if __name__ == "__main__":
    main()
