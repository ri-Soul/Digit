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

num_def = len(str(num))
while True:
  if num_def == 2:
    num0 = "00"
  if num_def == 3:
    num0 = "0"
  if num_def == 4:
    num0 = ""
  if num >= 9999:
    break
	 
  
  with open('4Digits.txt', 'a') as f:
    f.write("\n" + num0 +str(num))

  num += 1
 
print("Done!")
