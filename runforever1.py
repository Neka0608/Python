import random

while True:
	i=input("enter 'r' for rolling of a dices,enter 'q' to quit:")
	if(i=='q'):
		print("Bye Bye")
		exit()
	else:
		print("you got",random.randint(1,6))
