#!/usr/bin/env python3
# HP Switch Tools Using Netmiko by MDB

# Imports
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

# Info

# Functions will require passing a dictionary that is formatted as such:
# testSwitch = {
#     "device_type": "hp_procurve",
#     "host": "1.1.1.1",
#     "username": "admin",
# }

# Tests an SSH Connection to a Device
def connectionTest(**device) -> None:
        print(f"About to establish connection to {device['ip']}...")
        sshSession = ConnectHandler(ip = device["ip"], device_type = 'hp_procurve', username = device["username"], password = getpass('Please enter device password:\n'))
        print (sshSession)
        sshSession.disconnect()

# Returns the result of the 'show version' command for a Device
def showVersion(**device) -> str:
        print(f"About to establish connection to {device['ip']}...")
        sshSession = ConnectHandler(ip = device["ip"], device_type = 'hp_procurve', username = device["username"], password = getpass('Please enter device password:\n'))
        print(sshSession)
        result = sshSession.find_prompt() + " Version as of " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' :\n' + sshSession.send_command('show version')
        print("Closing Connection...")
        sshSession.disconnect()
        return(result)

# Returns the result of the 'show running config' command for a Device
def showRunningConf(**device) -> str:
        print(f"About to establish connection to {device['ip']}...")
        sshSession = ConnectHandler(ip = device["ip"], device_type = 'hp_procurve', username = device["username"], password = getpass('Please enter device password:\n'))
        print(sshSession)
        result = sshSession.find_prompt() + " Runngng Config as of " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' :\n' + sshSession.send_command('show running config')
        print("Closing Connection...")
        sshSession.disconnect()
        return(result)

# Returns the result of the 'show config' command for a Device
def showConf(**device) -> str:
        print(f"About to establish connection to {device['ip']}...")
        sshSession = ConnectHandler(ip = device["ip"], device_type = 'hp_procurve', username = device["username"], password = getpass('Please enter device password:\n'))
        print(sshSession)
        result = sshSession.find_prompt() + " Config as of " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' :\n' + sshSession.send_command('show config')
        print("Closing Connection...")
        sshSession.disconnect()
        return(result)

