# Python code of IP address and network

"""
This is the code of knowing IP related information from a particular IP Address as input by the user.
"""

import ipaddress

import os

from datetime import datetime

# User defined module - netsubcalc

import netsubcalc

try:

    my_file = 'output.txt'

    if os.path.exists('output.txt') == True:

        file = open(my_file, 'a')
        file.write("\n***********************************************************")
        file.write("\n")
        file.write("\nIP subnetting result \n\nToday is:")
        file.write(str(datetime.now()))
        file.write("\n")
        file.write("\n***********************************************************")
        file.write("\n")
        file.close()

    elif os.path.exists('output.txt') == False:

        file = open(my_file, 'w')
        file.write("\n***********************************************************")
        file.write("\n")
        file.write("\nIP subnetting result \n\nToday is:")
        file.write(str(datetime.now()))
        file.write("\n")
        file.write("\n***********************************************************")
        file.write("\n")
        file.close()

    print("\nThe result of subnetting is present in a 'output' file under the current directory.\n\n")


    input_ip = input("Enter the IP Address for subnetting in XXX.XXX.XXX.XXX/YY format:")

    ip_details = ipaddress.ip_network(input_ip, strict=False)

    print("\nThe details of IP address entered is given below..\n", file=open('output.txt', 'a'))

    ip_ver = ip_details.version

    print("IP Version:", ip_ver, file=open('output.txt', 'a'))

    if ip_ver == 4:

        print("\nIP Address:", ipaddress.IPv4Interface(input_ip).ip, file=open('output.txt', 'a'))

    elif ip_ver == 6:

        print("\nIP Address:", ipaddress.IPv6Interface(input_ip).ip, file=open('output.txt', 'a'))

    print("\nIP Network:", ip_details, " or ", ip_details.with_netmask, file=open('output.txt', 'a'))

    print("\nSubnet Mask:", ip_details.netmask, file=open('output.txt', 'a'))

    print("\nPrefix Length:", ip_details.prefixlen, file=open('output.txt', 'a'))

    print("\nHost Wild card Mask:", ip_details.hostmask, file=open('output.txt', 'a'))

    if ip_ver == 4:

        print("\nUsable addresses in the network:", ip_details.num_addresses - 2, file=open('output.txt', 'a'))

        print("\nFirst host of the network:", ip_details[1], file=open('output.txt', 'a'))

        print("\nLast host of the network:", ip_details[-2], file=open('output.txt', 'a'))

        print("\nBroadcast Address:", ip_details.broadcast_address, file=open('output.txt', 'a'))

    elif ip_ver == 6:

        print("\nTotal addresses in the network:", ip_details.num_addresses, file=open('output.txt', 'a'))

        print("\nNetwork in expanded form:", ip_details.exploded, file=open('output.txt', 'a'))

        print("\nNetwork in compressed form:", ip_details.compressed, file=open('output.txt', 'a'))

        print("\nAddress range:", ip_details[0], "-", ip_details[-1], file=open('output.txt', 'a'))

    # IP Subnet calculator module invoke

    letsubnet = netsubcalc.LetSubnet(input_ip)

    letsubnet.mysubnet()

    letsubnet.subnetcalc()

    file.close()

except FileNotFoundError:

    print("\nOutput File does not exist")

except ValueError:

    print("\n", input_ip, " does not appear to be an IPv4 or IPv6 address.", file=open('output.txt', 'a'))

    file.close()

except:

    print("\nSorry. An error occurred. Try again.", file=open('output.txt', 'a'))

    file.close()

finally:

    print("\n...Thank you...", file=open('output.txt', 'a'))

    file.close()
