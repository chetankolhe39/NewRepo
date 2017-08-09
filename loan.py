print "Loan Calculator"

borrow = input("Amount Borrowed : ")
interest = input("Interest Rate : ")
term = input("Term (years) : ")

def loan_cal(borrow, interest, term):
  paid = borrow * interest / 100 * term
  print "Amount borrowed : ",borrow
  print "Total Interest paid : ",paid
  monthly = (borrow + paid)/(term * 12)
  period = term * 12
  count = 1
  balance = borrow + paid
  print "pymt     Amnt paid     balance" 
  while count <= period:
    balance = balance - monthly
    print count,"           ",monthly,"           ",balance
    count+=1
loan_cal(borrow, interest, term)

