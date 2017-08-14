import random

words=["kohli","pandya","rohit","ashwin","jadeja","sachin"]
random_word=random.choice(words)
count=0
max=3
while count<=max:
   for i in words:
     print i
   guess=raw_input("Enter a word : ")
   
   if guess!=random_word:
     print "It's a wrong guess"
     count+=1
    
   if guess==random_word:
     count+=1
     print "well done!! you have guessed it right in ",count," attempt"
     break

if count>max:
  print "You lose!!"
    