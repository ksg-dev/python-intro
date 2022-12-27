answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if answer.strip() == "42" or answer.casefold() == "forty two" or answer.casefold() == "forty-two":
    print("Yes")
else:
    print("No")