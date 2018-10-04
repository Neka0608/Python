#playing with rock paper and scissor
import random
a={1:"R",2:"P",3:"S"}
c=a[random.randint(1,3)]
print("computer choice is",c)
u=input("enter Rock Paper or Scissor: ")
if(u==c):
	print("TIE")
if(u =="P" and c =="R" or u =="S" and c =="P" or u =="R" and c =="S"):
	print("U WON")
else:
	print("U LOSE")



