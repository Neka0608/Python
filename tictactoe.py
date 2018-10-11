#playing TIC TAC TOE GAME
a=['1','2','3','4','5','6','7','8','9']
def print_Board():
	print(a[0],'|',a[1],'|',a[2])
	print("------------")
	print(a[3],'|',a[4],'|',a[5])
	print("------------")
	print(a[6],'|',a[7],'|',a[8])
player1turn=True
while True:
	print_Board()
	p=input("choose an available place : ")
	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='O'):
			print("Place taken,choose another place...")
			continue
		else:
			if player1turn:
				print("Player 1>>")
				a[int(p)-1] = 'X'
				player1turn = not player1turn
			else:
				print("Player 2>>")
				a[int(p)-1] = 'O'
				player1turn = not player1turn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i+2]):
					print("GAME OVER");
					exit()
#checking for columns
			for i in range(3):
					if(a[i]==a[i+3] and a[i]==[i+6]):
						print("GAME OVER...");
						if(a[i]=='X'):
							print("CONGRATULATIONS TO PLAYER1")
						else:
							print("CONGRATULATIONS TO PLAYER2")
							print_Board()
							exit()
#checking for diagnol (from left to right)
					if(a[0]==a[4] and a[0]==a[8]):
						print("GAME OVER")
						if(a[4]=='X'):
							print("CONGRATULATIONS TO PLAYER1")
						else:
							print("CONGRATULATIONS TO PLAYER2")
							print_Board()
							exit()
#checking for diagnol (from right to left)
					if(a[2]==a[4] and a[2]==a[6]):
						print("GAME OVER")
						if(a[4]=='X'):
							print("CONGRATULATIONS TO PLAYER1")
						else:
							print("CONGRATULATIONS TO PLAYER2")
						print_Board()
						exit()
					else:	
						continue
		

