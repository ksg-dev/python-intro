def main():
    a = get_gauge()
    x = int(a[0])
    y = int(a[2])
    perc = x / y
    if perc <= 0.01:
        print("E")
    elif perc >= 0.99:
        print("F")
    else:
        print("{:.0%}".format(x/y))



def get_gauge():
    while True:
        f = (input("Fraction: "))
        try:
            g = int(f[0])
            h = int(f[2])
            if g <= h:
                break
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    return(f)



main()