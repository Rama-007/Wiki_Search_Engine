from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from word_getter import get_title , get_all 
from check import checker
import sys , re
from math import log
from collections import defaultdict
index=defaultdict(list)
import bz2,bz2file
cont=0
cnt=0
fp=open("mapping.txt",'w')
fp.write("\n")
class wikihandler(ContentHandler):
	title=""
	title1=""
	text=""
	Id=""
	title_flag=0
	text_flag=0
	id_flag=0
	page_flag=0
	flag=0
	title_words=[]
	body_text=[]
	infobox=[]
	categories=[]
	external_links=[]
	references=[]
	un_tag=["<sup>","#REDIRECT","format=","dts","dmy","colspan","</sup>","<big>","</big>","<small>","</small>","</tr>","<br>","<br />","<center>","</center","</abbr>","<abbr","<code>","</code>","<div>","</div>","<imagemap>","</imagemap>","<gallery>","</gallery>"]

	def invertedindex(self,doc_id,titles,bodytext,infobox,categories,external_links,references):
		global index 
		global cnt
		#doc_id total_freq title body info category external reference
		vocabulory=list(set(titles.keys()+bodytext.keys()+infobox.keys()+categories.keys()+external_links.keys()+references.keys()))
		
		for word in vocabulory:
			temp=str(doc_id)+" "
			#temp=""
			total_count=1+round(log(titles[word]+bodytext[word]+infobox[word]+categories[word]+external_links[word]+references[word]),2)
			temp+=str(total_count)+" "
			if(titles[word]):
				temp+="t-"+str(titles[word])+" "
			if(bodytext[word]):
				temp+="b-"+str(bodytext[word])+" "
			if(infobox[word]):
				temp+="i-"+str(infobox[word])+" "
			if(categories[word]):
				temp+="c-"+str(categories[word])+" "
			if(external_links[word]):
				temp+="e-"+str(external_links[word])+" "
			if(references[word]):
				temp+="r-"+str(references[word])
			index[word].append(temp)
		ind_list=[]
		# if(cont%50000==0):
		# 	print "hie"
		# 	for key in sorted(list(index.keys())):
		# 		temp1=str(key)+":"+"|".join(index[key])
		# 		ind_list.append(temp1)
		# 	out="out"+str(cnt)+".txt"
		# 	with open(out,"w") as f:
		# 		f.write("\n".join(ind_list))
		# 	cnt+=1
		#	index=defaultdict(list)
		#return

	def startElement(self,name,attrs):
		#global cont
		if(name=="page"):
			self.page_flag=1
		if(name=="id" and self.flag==0):
			self.id_flag=1
			self.flag=1
		if(name=="title"):
			self.title_flag=1
		elif(name=="text"):
			self.text_flag=1
	def endElement(self,name):
		global cont
		global fp
		if(name=="id"):
			self.id_flag=0
		elif(name=="page"):
			self.page_flag=0
			self.flag=0
			self.Id=""
		elif(name=="title"):
			#self.title_words=get_title(self.title)
			#print(self.title)
			self.title1=self.title
			self.title_flag=0
			self.title=""
		elif(name=="text"):
			# print str(cont)+":"+self.title1.encode('utf-8')+'\n'
			fp.write(str(cont)+":"+self.title1.encode('utf-8')+'\n')
			
			# self.text=re.sub("_","",self.text)
			# self.text=re.sub(",","",self.text)
			# self.text=re.sub("<ref.*?/ref>"," ",self.text)
			# self.text=re.sub('#([0-9a-fA-F]{6})',"",self.text)
			# self.text=re.sub("style=.*?;\""," ",self.text)
			# self.text=re.sub("style=.*?\""," ",self.text)
			# self.text=re.sub("style=.*?;"," ",self.text)
			# self.text=re.sub("width=.*?%\""," ",self.text)
			# self.text=re.sub("width=.*?\""," ",self.text)
			# self.text=re.sub("border=.*?\""," ",self.text)
			# self.text=re.sub("<!--.*?-->"," ",self.text)
			# for tag in self.un_tag:
			# 	self.text=re.sub(tag," ",self.text)
			# #self.text=re.sub(r'<ref>.+</ref>'," ",self.text)
			# self.body_text,self.infobox,self.categories,self.external_links,self.references=get_all(self.text.encode('utf-8'))
			# self.text_flag=0
			# self.text=""
			# self.invertedindex(str(cont),self.title_words,self.body_text,self.infobox,self.categories,self.external_links,self.references)

	def characters(self,content):
		global cont
		if(self.id_flag==1 and self.page_flag==1):
			#self.Id+=content
			cont+=1
		if(self.title_flag==1):
			self.title+=content
		# elif(self.text_flag==1):
		# 	self.text+=content
def main():
	if(len(sys.argv)<3):
		print("Use: python2.7 wiki.py input.xml output.txt")
		return
	handler=wikihandler()
	saxparser=make_parser()
	saxparser.setContentHandler(handler)
	#source=open(sys.argv[1],"r")
	source=bz2file.open("enwiki-latest-pages-articles-multistream.xml.bz2","r")
	saxparser.parse(source)
	#ind_list=[]
	#out=str(sys.argv[2])
	# if ".txt" not in sys.argv[2]:
	# 	out=out+".txt"
	# legth=len(index.keys())
	# out="out"+str(cnt)+".txt"
	# for key in sorted(list(index.keys())):
	# 	temp1=str(key)+":"+"|".join(index[key])
	# 	ind_list.append(temp1)
	# with open(out,"w") as f:
	# 	f.write("\n".join(ind_list))
	#checker(out)

if __name__=="__main__":
	main()