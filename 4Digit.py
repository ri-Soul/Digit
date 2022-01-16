num = 0
done = 0
num0 = "000"
print("________  .__       .__  __   ")
print("\______ \ |__| ____ |__|/  |_ ")
print(" |    |  \|  |/ ___\|  \   __/")
print(" |    `   \  / /_/  >  ||  |  ")
print("/_______  /__\___  /|__||__|  ")
print("        \/  /_____/           ")
print("")

while done == 0:
  
  if len(str(num)) == 2:
    num0 = "00"
  if len(str(num)) == 3:
    num0 = "0"
  if len(str(num)) == 4:
    num0 = ""
  if num >= 9999:
    done = 1
	 
  
  with open('Digits.txt', 'a') as f:
    f.write("\n" + num0 +str(num))

  num += 1
