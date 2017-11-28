fp=open("final/total","r")
f=[[] for i in range(0,36)]
for i in range(0,10):
	f[i]=open("total"+str(i),"w")
	f[i].write('\n')
for i in range(10,36):
	f[i]=open("total"+chr(ord('a')+i-10),"w")
	f[i].write('\n')
for line in fp:
	k=line.strip()[0]
	if(k>='0' and k<='9'):
		f[int(k)].write(line)
	else:
		print k
		f[ord(k)-ord('a')+10].write(line)