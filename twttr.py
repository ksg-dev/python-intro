vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def main():
    twt = input("Type here: ")
    for i in twt:
        if i in vowels:
            print(i.replace(i,""), end="")
        else:
            print(i, end="")
    print()
main()
