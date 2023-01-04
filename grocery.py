g_list = {

}
keys = g_list.keys()
values = g_list.values()

def main():
    while True:
      try:
        inst = input("").upper().strip()
        g_list.setdefault(inst, 0)
        g_list[inst] = g_list[inst] + 1
      except EOFError:
        sortg = sorted(g_list.items())
        new = dict(sortg)
        for key in new:
           print(new[key], key)
        break
print()

main()