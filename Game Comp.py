board = [['_','_','_'],['_','_','_'],['_','_','_']]
all_lists=[]
def get_list(lines=[],q=0):
	s=lines[q]
	t=[]
	i=2
	while True:
		try : 
			if isinstance(int(s[i-1:i]),(int,long)) and isinstance(int(s[i+2:i+3]),(int,long)) : break
		except : pass
		if s[i:i+1] is '_' : 
			t.append(s[i:i+1])
			i=i+5
		else : 
			t.append(s[i:i+2])
			i=i+6
	z=i+10
	i=i-1
	while i < z:		
		t.append(int(s[i:i+1]))
		i=i+3
	all_lists.append(t)

def lists():
	f=open("test.txt","r")
	lines = f.readlines()
	for c in range(len(lines)):
		get_list(lines,c)

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

def best_move(ls=[],tm=0,al=[],ply=0):
	pos=[]
	val=[]
	for x,y in enumerate(ls):
		if y is '_' : pass
		else :
			pos.append(x)
			val.append(y)
			
	sw=[]
	sd=[]
	sl=[]
	mini = 9
	posi = 0
	s=''
	if ply is 1 : s='X'+str(tm)
	elif ply is 2 : s='O'+str(tm)
	for x in range(len(al)):
		f=0
		for y in range(len(val)):
			if al[x][pos[y]] != val[y] : 
				f=-1
				break
		if f is 0 : 
			if al[x][9] is ply : sw.append(al[x])
			elif al[x][9] is 0 : sd.append(al[x])
	          	elif al[x][9] is not ply : sl.append(al[x])
		if len(sw) is not 0 :
			for x in range(len(sw)) : 
				if mini>sw[x][10+ply] : 
					mini = sw[x][10+ply]
					posi = sw[x].index(s)
		elif len(sd) is not 0 :
			for x in range(len(sd)) : 
				if mini>sd[x][10+ply] : 
					mini = sd[x][10+ply]
					posi = sd[x].index(s)
					
	all_lists=sw+sd+sl
	return posi+1				
	
def main():	
	lists()
	ini_board()
	save = ['_','_','_','_','_','_','_','_','_']
	z=int(raw_input("1 for X & 2 for O : "))
	i=1
	tmn=0
	while True:
		tmn+=1
		print_board()
		if z is 1 :
			if i is 1:
				g=int(raw_input("Move : "))
				update(i,g) 
				save[g-1]='X'+str(tmn)
				i=2
			elif i is 2 : 
				g=best_move(save,tmn,all_lists,i)
				update(i,g)
				save[g-1]='O'+str(tmn)
				i=1
			if check() is 1 : 
				print 'You Win'
				break
			elif check() is 2 : 
				print 'Computer Wins'
				break 
			elif check() is 3 :
				print 'Game Draw'
				break
		elif z is 2 :
			if i is 1 : 
				g=best_move(save,tmn,all_lists,1)
				update(i,g)
				save[g-1]='X'+str(tmn)
				i=2
			elif i is 2:
				g=int(raw_input("Move : "))
				update(i,g) 
				save[g-1]='O'+str(tmn)
				i=1
			if check() is 2 : 
				print 'You Win'
				break
			elif check() is 1 : 
				print 'Computer Wins'
				break 
			elif check() is 3 :
				print 'Game Draw'
				break
	print_board()
main()

