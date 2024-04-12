def is_prime(P):

    if P == 2:
        return True

    if P % 2 == 0 or P == 1:
        return False

    else:
        for i in range(3, int(P ** 0.5 + 1), 2):
            if P % i == 0:
                return False

        return True


i = 0
while i < 999:
  num = str(i)
  l = len(num)
  components = set()

  for j in range(l):
   for k in range(l):
     if j + k < l:
       components.add(int(num[j: j + k + 1]))

  for component in components:
    if not is_prime(component):
      continue
    continue

  print(f"{i} | {components}")













  i += 1
