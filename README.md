# ip_subnet_calculator
A basic handy IP subnet calculator written in Python that can be used for IPv4/IPv6.

This programme is written in Python 3.7.

This is a IP subnet calculator that works for both IPv4 and IPv6. Most of us use online IP subnet calculator when required. I thought of giving the same flavor through Python, thinking about the case where you have no internet access and need an urgent subnetting.

Here is the code to survive from this type of situation.

1. Main code to fire - net_ip_address.py - Run this file to start the subnet calculator.
2. Module name - netsubcalc.py - imported the classes under this created module to perform the IP subnetting.

When the code is triggered, it will ask for providing IP address in XXX.XXX.XXX.XXX/YY format.

![Enter IP Address](https://github.com/sajalda23409/ip_subnet_calculator/blob/master/image/1.PNG)


In return, it will create an "output" file in the same directory where the code is present and push all the subnet information in it.

The file is appended with new information of subnetting, everytime the code is triggered.

After the IP address is entered, it will ask for the new subnet size, you want to move and planned in "YY" format.

![Enter the new subnet size](https://github.com/sajalda23409/ip_subnet_calculator/blob/master/image/2.PNG)

The subnetting is done at backend and the results are added in the "ouput.txt" file.

Here is a sample output details of IPv4 and IPv6 as reference.

Please check my Repo for the same. Thanks.






