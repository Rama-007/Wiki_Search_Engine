i=0
lenth=176
l=0
while lenth!=1:
	while i+1 <lenth:
		fp1=open("out"+str(i)+".txt","r")
		lines1=fp1.readlines()
		fp2=open("out"+str(i+1)+".txt","r")
		lines2=fp2.readlines()
		j=0
		k=0
		fp=open("output"+str(l)+".txt","w")
		while j<len(lines1) and k<len(lines2):
			k1=lines1[j].split(":")
			k2=lines2[k].split(":")
			if(k1[0]==k2[0]):
				temp=k1[0]+":"+k1[1][:-1]+"|"+k2[1]
				fp.write(temp)
				j+=1
				k+=1
			elif(k1[0]<k2[0]):
				fp.write(lines1[j])
				j+=1
			elif(k1[0]>k2[0]):
				fp.write(lines2[k])
				k+=1
		while(j<len(lines1)):
			fp.write(lines1[j])
			j+=1
		while(k<len(lines2)):
			fp.write(lines2[k])
			k+=1
		l+=1
		i+=2

	if(i<lenth):
		fp=open("output"+str(l)+".txt","w")
		fp1=open("out"+str(i)+".txt","r")
		for line in fp1:
			fp.write(line)
	break

# fp1=open("out0.txt","r")
# lines1=fp1.readlines()
# fp2=open("out1.txt","r")
# lines2=fp2.readlines()
# i=0
# j=0
# fp=open("output.txt","w")
# while i<len(lines1) and j<len(lines2):
# 	t1=lines1[i].split(":")[0]
# 	t2=lines2[j].split(":")[0]
# 	if(t1==t2):
# 		temp=t1+":"+lines1[i].split(":")[1][:-1]+"|"+lines2[j].split(":")[1]
# 		fp.write(temp)
# 		i+=1
# 		j+=1
# 	elif(t1<t2):
# 		fp.write(lines1[i])
# 		i+=1
# 	elif(t1>t2):
# 		fp.write(lines2[j])
# 		j+=1
# if(i<len(lines1)):
# 	fp.write(lines1[i])
# 	i+=1
# if(j<len(lines2)):
# 	fp.write(lines2[j])
# 	j+=1