num = 0
done = 0
num0 = 0
print("________  .__       .__  __   ")
print("\______ \ |__| ____ |__|/  |_ ")
print(" |    |  \|  |/ ___\|  \   __/")
print(" |    `   \  / /_/  >  ||  |  ")
print("/_______  /__\___  /|__||__|  ")
print("        \/  /_____/           ")
print("")

while done == 0:

  if num0 == 0:
    with open('Digits.txt', 'a') as f:
      f.write("\n" + "000" +str(num))

  elif num0 == 1:
    with open('Digits.txt', 'a') as f:
      f.write("\n" + "00" +str(num))

  elif num0 == 2:
    with open('Digits.txt', 'a') as f:
      f.write("\n" + "0" +str(num))

  else:
    with open('Digits.txt', 'a') as f:
      f.write("\n" + str(num))


  if len(str(num)) == 2:
    num0 = 1
  if len(str(num)) == 3:
    num0 = 2
  if len(str(num)) == 4:
    num0 = 3
  if num >= 9999:
    done = 1

  num += 1
