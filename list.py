total = input("How many numbers in list?  ")
list = []
for i in range(total):
  x = input()
  list.append(x)
print list
new_list = []
for i in list:
  if i<10:
    new_list.append(i)
print new_list