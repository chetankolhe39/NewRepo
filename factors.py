num=input("Enter number : ")
count=1
check = num / 2
while count<=check:
  if num%count==0:
    print count,
  count+=1
print num