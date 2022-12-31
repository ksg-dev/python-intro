def main():
    var = input("Variable: ")
    for i in var:
        if i.isupper() is True:
            print("_" + i.lower(), end="")
        else:
            print(i, end="")
    print()
main()


