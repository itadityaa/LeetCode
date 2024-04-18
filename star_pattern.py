count = 0
flag = True
n = int(input("Enter the number of rows: "))
for _ in range(n):
  if count == 0:
    flag = True
  print(f"{count * ' '}*\n")  
  if count % 2 == 0 and count != 0:
    flag = False
  if flag:    
    count += 1
  else:
    count -= 1

# Output:
# Enter the number of rows: 7
# *
#  *
#   *
#  *
# *
#  *
#   *