try:
 num = int(input("Enter number : "))
except ValueError:
 print "This is not a number"
sum = 0
while num != 0:
 r = num%10
 sum = sum+r
 num = num/10
print sum