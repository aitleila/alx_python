#!/usr/bin/python3
n= 99

for i in range (0,n+1):
    
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
    