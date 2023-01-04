months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            indate = input("Date: ").strip()
            final_date = date_split(indate)
            print(final_date[0], end="-")
            print(f"{final_date[1]:02}", end="-")
            print(f"{final_date[2]:02}")
            break
        except TypeError:
            pass
        except IndexError:
            pass



def date_split(i):
        if i[0].isdigit():
            output1 = numb_date(i)
            return(output1)
        elif i[0].isalpha():
            output2 = alpha_date(i)
            return(output2)
        else:
            pass


def alpha_date(j):
    while True:
        try:
            x, y, z = j.split(" ")
            x = months.index(x) + 1
            y = int(y.strip(","))
            if "," in j and y < 32 and x < 13:
                return(z, x, y)
            else:
                return()
        except ValueError:
            pass


def numb_date(k):
    while True:
        try:
            x, y, z = k.split("/")
            x = int(x)
            y = int(y)
            if y < 32 and x < 13:
                return(z, x, y)
            else:
                return()
        except ValueError:
            pass



main()


