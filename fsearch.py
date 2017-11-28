import os ,sys
import linecache
import math , time
from collections import defaultdict
from word_getter import tokenize,stem,stopwords
def parseRow(row):
	k=row.split(":")
	return (k[0],k[1])
def get_list(filename,name):
	with open(filename,"r") as f:
		l=0
		r=os.path.getsize(filename)
		while l<=r:
			mid=(l+r)/2
			f.seek(int(mid))
			f.readline()
			namer=parseRow(f.readline())
			if(name==namer[0]):
				temp=namer[1][1:].split(" ")
				ret_val=[]
				ret_val1=[]
				i=0
				while i < len(temp)-1:
					#print(temp[i],temp[i+1])
					ret_val.append(temp[i])
					ret_val1.append(temp[i+1])
					i+=2
				return (ret_val,ret_val1)

			elif(name>namer[0]):
				l=mid+1
			else:
				r=mid-1
		return -1

def getline(filename,name):
	with open(filename,"r") as f:
		l=0
		r=os.path.getsize(filename)
		name=int(name)
		while l<=r:
			mid=(l+r)/2
			f.seek(int(mid))
			f.readline()
			nam=f.readline()
			namer=nam.split(":")
			if(name==int(namer[0])):
				return nam
			elif(name>int(namer[0])):
				l=mid+1
			else:
				r=mid-1
		return -1



def get_finallist(postlist):
	temp=postlist[0]
	for i in postlist[1:]:
		temp=list(set(temp).intersection(i))
		if(len(temp)==0):
			break
	return temp

def fieldquery(query):
	query1=query.split(",")
	postlist=[]
	dictnry=defaultdict(float)
	for words in query1:
		word=words.strip().split(":")
		querywords=tokenize(word[1])
		querywords=stopwords(querywords)
		querywords=stem(querywords)
		if(word[0]=='t'):
			filename="final/title"
		elif(word[0]=='b'):
			filename="final/body"
		if(word[0]=='i'):
			filename="final/info"
		if(word[0]=='c'):
			filename="final/category"
		if(word[0]=='e'):
			filename="final/external"
		if(word[0]=='r'):
			filename="final/reference"
		for war in querywords:
			temp=get_list(filename,war)
			if(temp==-1):
				print war+" :Not found"
				return
			i=0
			#print temp
			while i < len(temp[0]):
				dictnry[temp[0][i]]+=((1+math.log(float(temp[1][i])))*math.log(17600000/len(temp[0])))
				i+=1
				# if(temp==-1):
				# 	print war+" :Not found"
				# 	quit()
				# else:
			postlist.append(temp[0])
	postlist.sort(key=len)
	final_list=get_finallist(postlist)
	#print final_list
	lst=sorted(final_list,key=lambda k:dictnry[k],reverse=True)
	c=0
	#print(lst)
	for i in lst:
		k=getline("final_mapping.txt", i)
		print k
		if(k!=-1):
			#print k
			c+=1
		if(c>9):
			break
	return


def qquery(query):
	#query=raw_input("Enter query: ")
	#query=sys.argv[1]
	if ":" in query:
		fieldquery(query)
		return
	querywords=tokenize(query)
	querywords=stopwords(querywords)
	querywords=stem(querywords)
	postlist=[]
	dictnry=defaultdict(float)
	for word in querywords:
		temp=get_list("final/total",word)
		i=0
		if(temp==-1):
			print word+" :Not found"
			return
		while i < len(temp[0]):
			dictnry[temp[0][i]]+=(1+float(temp[1][i])*math.log(17600000/len(temp[0])))
			i+=1
		# if(temp==-1):
		# 	print word+" :Not found"
		# 	quit()
		# else:
		postlist.append(temp[0])
	if(len(postlist)==0):
		print "phrase not found"
		return
	postlist.sort(key=len)
	final_list=get_finallist(postlist)
	if(len(final_list)==0):
		print "phrase not found"
		return
	lst=sorted(final_list,key=lambda k:dictnry[k],reverse=True)
	c=0
	for i in lst[5:]:
		k=getline("final_mapping.txt", i)
		print k
		if(k!=-1):
			#print k
			c+=1
		if(c>1000):
			break
	return


def main():
	while True:
		query=raw_input("Enter Query-->")
		if(query.strip()==""):
			continue
		stime=time.time()
		qquery(query)
		print(time.time()-stime)

if __name__=="__main__":
	#start=time.time()
	main()
	#print time.time()-start