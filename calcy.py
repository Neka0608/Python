#using calcy.py
i=int(input("enter a value of i:"))
j=int(input("enter a value of j:"))
s=input("what do you want to do? +,-,*,/ : ")
 
def add():
 	return (i+j)
def sub():
 	return (i-j)
def multi():
 	return (i*j)
def div():
 	return (i/j)

 	if(s=='+'):
 		print("addition=",add())
 	elif(s=='-'):
 		print("substraction=",sub())
 	elif(s=='*'):
 		print("multiplication=",multi())
 	elif(s=='/'):
 		print("division=",div())
 	else:
 		print("give a proper input")


