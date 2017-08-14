try:
 num = int(input("Enter number : "))
except ValueError:
 print "This is not a number"
count=0
while num!=0:
 num%10
 count+=1
 num=num/10
print count