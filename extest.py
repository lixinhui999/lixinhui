#!/usr/bin/env python3

num = input("Enter number:")
new_num= int(num)
print('INT:{}'.format(new_num))

try:
    f = open(num)
    print(f.read())
    f.close()
except ValueError as Error:
    print("ERROR:{}".format("num"))
