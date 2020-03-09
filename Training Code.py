from random import randint
import time
board = [['_','_','_'],['_','_','_'],['_','_','_']]
stop = 0

def ini_board():
	for i in range(3):
		for j in range(3):
			board[i][j] = '_'
			
def print_board():
	s=''
	print 'Board :- '
	for i in range(3):
		s+='   '+' '.join(board[i])+'\n'
	print s

def check():
	c=0
	if (board[0][0] is 'X' and board[0][1] is 'X' and board[0][2] is 'X') or (board[1][0] is 'X' and board[1][1] is 'X' and board[1][2] is 'X') or (board[2][0] is 'X' and board[2][1] is 'X' and board[2][2] is 'X') or (board[0][0] is 'X' and board[1][0] is 'X' and board[2][0] is 'X') or (board[0][1] is 'X' and board[1][1] is 'X' and board[2][1] is 'X') or (board[0][2] is 'X' and board[1][2] is 'X' and board[2][2] is 'X') or (board[0][0] is 'X' and board[1][1] is 'X' and board[2][2] is 'X') or (board[0][2] is 'X' and board[1][1] is 'X' and board[2][0] is 'X') : c=1
	elif (board[0][0] is 'O' and board[0][1] is 'O' and board[0][2] is 'O') or (board[1][0] is 'O' and board[1][1] is 'O' and board[1][2] is 'O') or (board[2][0] is 'O' and board[2][1] is 'O' and board[2][2] is 'O') or (board[0][0] is 'O' and board[1][0] is 'O' and board[2][0] is 'O') or (board[0][1] is 'O' and board[1][1] is 'O' and board[2][1] is 'O') or (board[0][2] is 'O' and board[1][2] is 'O' and board[2][2] is 'O') or (board[0][0] is 'O' and board[1][1] is 'O' and board[2][2] is 'O') or (board[0][2] is 'O' and board[1][1] is 'O' and board[2][0] is 'O') : c=2
	else :
		f=0
		for i in range(3):
			for j in range(3):
				if board[i][j] is '_' : 
					f=1
					break
		if f is 0 : c=3
		else : pass
	return c

def update(plyr,pos):
	c=''
	if plyr is 1 : c='X'
	elif plyr is 2 : c='O'
	if board[(pos-1)//3][(pos-1)%3] is '_' : board[(pos-1)//3][(pos-1)%3]=c
	else : pass


def main():
	ini_board()
	save = ['_','_','_','_','_','_','_','_','_',0,0,0,0]
	tmp=[0,0,0,0,0,0,0,0,0]
	i=1
	tmn=0
	xmn=0
	omn=0
	while True:
		#print_board()
		#g= int(raw_input("Move : "))
		while True:
			a=randint(1, 9)
			#print "a is "+str(a)
			if tmp[a-1] is 0 :
				tmp[a-1] = 1
				g=a
				break
		update(i,g)
		tmn+=1
		if i is 1 : 
			xmn+=1
			save[g-1]='X'+str(tmn)
			i=2
		elif i is 2 : 
			omn+=1
			save[g-1]='O'+str(tmn)
			i=1
		#print check()
		if check() is 1 : 
			#print 'Player 1 Wins'
			save[9]=1
			break
		elif check() is 2 : 
			#print 'Player 2 Wins'
			save[9]=2
			break 
		elif check() is 3 :
			#print 'Game Draw'
			save[9]=0
			break
	save[10]=tmn
	save[11]=xmn
	save[12]=omn
	p=str(save)
	tmp=p+'\n'
	#print_board()
	found=0
	f=open("data.txt","r+")
	lines = f.readlines()
	no = len(lines)
	if no is 255168 :
		print "Database ready"
		stop = 1
	for line in lines :
		if line == tmp : 
			found = 1
			break;
	f.close()
	if found is 0 : 
		f=open("data.txt","a+")
		f.write(p+'\n')
		f.close()
	
	Final = "Progress : "+str(float("{0:.5f}".format(round((no*100.0)/255168.0,5))))+"% Games Played : "+str(no)  
	
	return Final

def bro():
	start = time.time()
	while stop is not 1:
		print main()
	end = time.time()
	print "Time Taken : "+str(end-start)

bro()
