num=input("Enter number : ")
sum=0
count=1
check = num / 2
while count<=check:
  if num%count==0:
    print count,
    sum=sum+count
  count=count+1

if sum==num:
  print "It is a perfect number"
else:
  print "It's not a perfect number"