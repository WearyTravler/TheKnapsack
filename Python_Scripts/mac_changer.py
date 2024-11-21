#!/usr/bin/python3

import subprocess
import random

# Mac Changer in Python

# Run program
# List all the interfaces
# Ask which one the user wants to change the MAC address of 
# Changes it 
# Asks if they want to change it again.


import subprocess

def get_interfaces():
    try:
        # Run the `ifconfig` command
        result = subprocess.run(['ifconfig'], capture_output=True, text=True, check=True)
        
        # Parse the output
        output = result.stdout
        interface_names = []

        for line in output.splitlines():
            # Look for lines that start with an interface name (not indented)
            if line and not line.startswith(' '):
                interface_name = line.split()[0].rstrip(':')  # Remove trailing colon
                interface_names.append(interface_name)
        
        return interface_names
    except subprocess.CalledProcessError as e:
        print("Error running ifconfig:", e.stderr)
        return []

# Call the function and display results
#interfaces = get_interfaces()

def generate_random_mac():
    #Organizationally Unique Identifier (OUI): The first 24 bits (00:1A:2B in the example) represent the manufacturer of the NIC.
    #Network Interface Controller (NIC) Specific: The last 24 bits (3C:4D:5E) are unique to the device within the manufacturer’s range.
    mac_parts = [f"{random.randint(0,255):02x}" for _ in range(6)]
    return ":".join(mac_parts)



def change_interface(interface):
    turn_off = subprocess.run(['ifconfig' + interface + 'down'])
    change_mac = subprocess.run(['ifconfig hw ether' + generate_random_mac])
    turn_on = subprocess.run(['ifconfig' + interface + 'up'])


def main():
    print("Mac Changer in Python ")
    print("Author: @WearyTravler")
    interface_list = get_interfaces()
    count = 1
    for x in interface_list:
        print(count,":",x)
        count +=1
    chosen_interface = input("Which interface would you like to change: ")
    #need to write a for loop and assign each discovered interface as a choice to select
    change_interface(chosen_interface)


main()


