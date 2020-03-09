import operator
all_lists=[]
x_lists=[]
y_lists=[]
d_lists=[]
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
	f=open("data.txt","r")
	lines = f.readlines()
	for c in range(len(lines)):
		#print c
		get_list(lines,c)
		
lists()

for x in range(len(all_lists)):
	if all_lists[x][9] is 1 : x_lists.append(all_lists[x])
	elif all_lists[x][9] is 2 : y_lists.append(all_lists[x])
	elif all_lists[x][9] is 0 : d_lists.append(all_lists[x])
		
x_lists=sorted(x_lists,key=operator.itemgetter(11))
y_lists=sorted(y_lists,key=operator.itemgetter(12))
#d_lists=sorted(d_lists,key=operator.itemgetter(10))


f=open("x_lists.txt","w+")
for x in range(len(x_lists)):
	f.write(str(x_lists[x])+'\n')
f.close()

f=open("y_lists.txt","w+")
for y in range(len(y_lists)):
	f.write(str(y_lists[y])+'\n')
f.close()

f=open("d_lists.txt","w+")
for d in range(len(d_lists)):
	f.write(str(d_lists[d])+'\n')
f.close()

