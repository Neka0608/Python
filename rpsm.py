import random
a=['r','p','s']
s1=0
s2=0
while(True):
	u = input("Your choice r/p/s: ")
	c = random.choice(a)
	print("You chose",u,"Computer chose",c)
	if(u=="r" or u=="p" or u=="s"):
		if(u==c):
			print("Tie")
		elif((u=="r" and c=="p") or (u=="p" and c=="s") or (u=="s" and c=="r")):
			s1=s1+1
			print("Computer Won",s1,"Times")
		else:
			s2=s2+1
			print("U Won",s2,"Times")
	else:
		print("Give me a proper input")
		exit()
	if(s1==3 or s2==3):
		if(s1==3):
			print("SORRY, COMPUTER WON THE GAME AGAINST U")
		else:
			print("CONGRATULATIONS U WON THE GAME AGAINST THE COMPUTER")
			exit()