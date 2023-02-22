import csv
import sys
from tabulate import tabulate
# ----this code block produces tabular table in proper format-----
menu = []

with open("sicilian.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        menu.append({"Sicilian Pizza" : row[0], "Small" : row[1], "Large" : row[2]})
    print(tabulate(menu, tablefmt = "grid"))
# --------end of code block-----------------------------------------

#def filter(file):
 #   try:
  #      file = sys.srgv[1]
   #     if len(sys.argv) > 2:
    #        print("Too many command-line arguments")
     #       return 1
      #  elif file.lstrip(".")
