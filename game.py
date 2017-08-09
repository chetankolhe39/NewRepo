import random
points = input("How many points to win ? ")
player1 = raw_input("Your name? ")
list = ['R', 'S', 'P']
human = 0
machine = 0

while human <= points and machine <= points:
    ans1 = raw_input("%s, (R)ock, (P)aper, (S)cissors ? "% player1)
    ans2 = random.choice(list)
    if ans1 == ans2:
      print "Draw"
    elif ans1 == 'R':
       if ans2 == 'S':
         print "%s wins" % player1
         human+=1
       else:
         print "Computer wins"
         machine+=1 
    elif ans1 == 'S':
       if ans2 == 'P':
         print "%s wins" % player1
         human+=1
       else:
         print "Computer wins"
         machine+=1
    elif ans1 == 'P':
       if ans2 == 'R':
         print "%s wins" % player1
         human+=1
       else:
         print "Computer wins"
         machine+=1
    else:
      print "Invalid...."

print player1," = ",human,"    comp = ",machine
