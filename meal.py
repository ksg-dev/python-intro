def main():
    time = convert(input("What time is it? "))
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print()

# convert time to float
def convert(time):
    hour, minute = time.split(":")
    decmin = (float(minute)) / 60
    return(float(hour) + decmin)

# conditional phrasing
if __name__ == "__main__":
   main()