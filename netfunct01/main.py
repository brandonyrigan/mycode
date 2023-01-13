#!/usr/bin/env python3

import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {crayons.green(mycmds)}')
            # we'll learn to write code that sends cmds to device here
    return None

def devicereboot(ips):
    #loop through IPs
    for ip in ips:
        print(f"Connecting to.. {crayons.red('REBOOTING NOW!')}")
    return None

# start our main script
def main():
    """called at runtime"""

    #open external json file
    with open("netfunct01/devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)

    print(f"{crayons.blue('Welcome to the network device command pusher')}") # welcome message

    ## get data set
    print(f"\n{crayons.green('Data set found')}\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd) # call reboot function

# call our main function
main()

