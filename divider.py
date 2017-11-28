fp=open("Final_index.txt","r")
ff=open("final/total","w")
# ft=open("final/title","w")
# fb=open("final/body","w")
# fi=open("final/info","w")
# fc=open("final/category","w")
# fe=open("final/external","w")
# fr=open("final/reference","w")
#doc_id total_freq title body info category external reference
for line in fp:
	line=line[0:len(line)-1]
	tep=line.split(":")
	name=tep[0]
	# tt=0
	# bb=0
	# ii=0
	# cc=0
	# ee=0
	# rr=0
	ff.write(name+": ")
	# if("t-") in line:
	# 	tt=1
	# 	ft.write(name+": ")
	# if("b-") in line:
	# 	bb=1
	# 	fb.write(name+": ")
	# if("i-") in line:
	# 	ii=1
	# 	fi.write(name+": ")
	# if("c-") in line:
	# 	cc=1
	# 	fc.write(name+": ")
	# if("e-") in line:
	# 	ee=1
	# 	fe.write(name+": ")
	# if("r-") in line:
	# 	rr=1
	# 	fr.write(name+": ")
	docs=tep[1].split("|")
	for word in docs:
		temp=word.split(" ")
		Id=temp[0]
		ff.write(Id+" "+temp[1]+" ")
	# 	for wo in temp[2:]:
	# 		if(wo[0:2]=="t-"):
	# 			ft.write(Id+" "+wo[2:]+" ")
	# 		if(wo[0:2]=="b-"):
	# 			fb.write(Id+" "+wo[2:]+" ")
	# 		if(wo[0:2]=="i-"):
	# 			fi.write(Id+" "+wo[2:]+" ")
	# 		if(wo[0:2]=="c-"):
	# 			fc.write(Id+" "+wo[2:]+" ")
	# 		if(wo[0:2]=="e-"):
	# 			fe.write(Id+" "+wo[2:]+" ")
	# 		if(wo[0:2]=="r-"):
	# 			fr.write(Id+" "+wo[2:]+" ")
	# if(tt==1):
	# 	ft.write('\n')
	# if(bb==1):
	# 	fb.write('\n')
	# if(ii==1):
	# 	fi.write('\n')
	# if(cc==1):
	# 	fc.write('\n')
	# if(ee==1):
	# 	fe.write('\n')
	# if(rr==1):
	# 	fr.write('\n')
	ff.write('\n')