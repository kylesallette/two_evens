def lesser(a,b):
    if a and b % 2 == 0:
      print(min(a,b))
    elif a or b % 2 == 1:
      print(max(a,b))

lesser(6,19)
