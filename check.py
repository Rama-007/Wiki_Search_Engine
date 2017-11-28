import os
def checker(name):
	temp=name
	name="split -b 66122346 "+name
	namer="mv xaa "+temp
	os.system(name)
	os.system(namer)
	os.system("rm xab")
