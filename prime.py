try:
  num = int(input("Enter Number : "))
except ErrorValue:
  print "This is not a number"
flag = False
for count in range(2, num):
  if (num % count) == 0:
    flag = True
    break
if flag == False:
   print "Number",num,"is prime"
else:
  print "Number",num,"is not prime"