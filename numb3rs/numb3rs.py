##unfinished
##unfinished
import re
import sys


def main():
    print(validate(input("IP Address: ").strip()))

def validate(ip):
    a, b, c, d = ip.split(".")
    if a > 255:
        return("False")
    elif b > 255:
        return("False")
    elif c > 255:
        return("False")
    elif d > 255:
        return("False")
    else:
        return("True")
if __name__ == "__main__":
    main()

