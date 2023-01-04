import sys

list = []
comment = []


try:
    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif (".py") not in sys.argv[1]:
        print("Not a Python file")
        sys.exit()
    else:
        with open(file_name) as file:
            for line in file:
                if line.isspace() is False:
                    list.append(line.strip())
                if line.strip().startswith("#") is True:
                    comment.append(line.strip())
            t_lines = (int(len(list))) - (int(len(comment)))
            print(t_lines)
            sys.exit()
except IndexError:
    print("Too few command-line arguments")
    sys.exit()
except FileNotFoundError:
    print("File does not exist")
    sys.exit()







