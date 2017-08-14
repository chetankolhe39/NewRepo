try:
 num=int(input("Enter number : "))
except ValueError:
 print "This is not a number"
if num%2==0:
 print "Number is Even"
else:
 print "Number is Odd"