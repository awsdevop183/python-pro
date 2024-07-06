#!/bin/python3
count = 1
table = int(input("enter your table number: "))

while count <=10:
    result = count * table
    print(f"{count} * {table} = {result}")
    count+=1
