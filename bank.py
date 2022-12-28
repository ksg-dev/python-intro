def main():
    greeting = input("Greeting: ").casefold().strip()
    print(dollars(greeting))

def dollars(n):
    if n.startswith("hello"):
        return("$0")
    elif n.startswith("h"):
        return("$20")
    else:
        return("$100")

main()