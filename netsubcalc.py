# IP subnet calculator

"""
This is the code of calculating subnet from a particular IP Address as input by the user.
"""

import ipaddress

class LetSubnet():

    def __init__(self, input_data):

        self.input_data = input_data

        self.ip_net = ipaddress.ip_network(self.input_data, strict=False)

    def mysubnet(self):

        print("\nNumber of possible subnet from ", self.ip_net, ":", file=open('output.txt', 'a'))

        for i in list(self.ip_net.subnets()):

            print("\n", i, file=open('output.txt', 'a'))

        print("\nNumber of possible supernet from ", self.ip_net, ":", file=open('output.txt', 'a'))

        print("\n", self.ip_net.supernet(), file=open('output.txt', 'a'))

    def subnetcalc(self):

        self.target_subnet = input("\nMove to:- Provide the new subnet size. /")

        if int(self.target_subnet) >= int(self.ip_net.prefixlen):

            print("\nTarget size to achieve:/", self.target_subnet, file=open('output.txt', 'a'))

            print("\nSubnet:", len(list(self.ip_net.subnets(new_prefix=int(self.target_subnet)))), file=open('output.txt', 'a'))

            for i in list(self.ip_net.subnets(new_prefix=int(self.target_subnet))):

                print("\n", i, file=open('output.txt', 'a'))

        elif int(self.target_subnet) <= int(self.ip_net.prefixlen):

            print("\nTarget size to achieve:/", self.target_subnet, file=open('output.txt', 'a'))

            print("\nSupernet:", file=open('output.txt', 'a'))

            print("\n", self.ip_net.supernet(new_prefix=int(self.target_subnet)), file=open('output.txt', 'a'))

