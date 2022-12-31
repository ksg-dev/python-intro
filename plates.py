numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 > len(s) or len(s) > 7:
        return()
    elif s[0] in numb:
        return()
    elif s[1] in numb:
        return()
    elif char(s) > 0:
        return()
    elif find_num(s) == "alpha":
        return(8)
    elif find_num(s)[1] == "0":
        return()
    elif let_sand(s) > 0:
        return()
    else:
        return(9)

def char(s):
    for i in s:
        if i.isalnum() is True:
            return(0)
        else:
            return(1)



def find_num(s):
    if s.isalpha() is True:
        return("alpha")
    else:
        for index, a in enumerate(s):
            if a.isdigit():
                ind = index
                return(index, a)
                break

def let_sand(s):
    v = find_num(s)[0]
    r = len(s)
    str = s[v:r]
    if str.isdigit() is True:
	    return(0)
    else:
        return(1)


main()