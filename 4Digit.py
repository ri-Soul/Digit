num = 0
num0 = "000"
print("________  .__       .__  __   ")
print("\______ \ |__| ____ |__|/  |_ ")
print(" |    |  \|  |/ ___\|  \   __/")
print(" |    `   \  / /_/  >  ||  |  ")
print("/_______  /__\___  /|__||__|  ")
print("        \/  /_____/           ")

print("")
print("Loading...")
print("")

while True:
  
  if len(str(num)) == 2:
    num0 = "00"
  if len(str(num)) == 3:
    num0 = "0"
  if len(str(num)) == 4:
    num0 = ""
  if num >= 9999:
    break
	 
  
  with open('4Digits.txt', 'a') as f:
    f.write("\n" + num0 +str(num))

  num += 1
 
print("Done!")
