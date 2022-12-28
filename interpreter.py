def main():
    problem = (input("Problem: "))
    x, y, z = problem.split(" ")
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))
    else:
        print("Error")

main()
