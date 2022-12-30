#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dell
#
# Created:     30-12-2022
# Copyright:   (c) dell 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

number = input("enter number: ")
num = 1
number1 = int(number) * 2 - 1
r = int(number1) // 2
if num != number:
    while r >= 0:
        print(r * " ", num * " *")
        r = r - 1
        num = num + 1
