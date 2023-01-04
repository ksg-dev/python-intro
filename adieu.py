import inflect

input_list = []
adieu = "Adieu, adieu, to "
p = inflect.engine()

def main():
    while True:
        try:
            name = input("Name: ")
            input_list.append(name)
        except EOFError:
            name_list = p.join((input_list))
            print(adieu + name_list)
            break
main()