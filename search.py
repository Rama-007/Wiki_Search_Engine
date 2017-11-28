import os
name="ramarohit"
filename='test/body'
def seekTo(f,c):
	while f.read(1)!=c:
		f.seek(-2,1)
def parseRow(row):
	k=row.split(":")
	print k
	return (k[0],k[1])
step=os.path.getsize(filename)/2
with open(filename,"r") as f:
	l=0
	r=os.path.getsize(filename)
	while l<=r:
		mid=(l+r)/2
		f.seek(int(mid))
		f.readline()
		namer=parseRow(f.readline())
		if(name==namer[0]):
			print(namer[1])
			break
		elif(name>namer[0]):
			l=mid+1
		else:
			r=mid-1