import re
from collections import defaultdict
#from nltk.stem.porter import PorterStemmer
#stemmer=PorterStemmer()
from Stemmer import Stemmer
stemmer=Stemmer("english")

stopword=defaultdict(int)
fp=open("stopwords.txt","r")
for line in fp:
	line=line.strip()
	line=line.lower()
	stopword[line]=1
fp.close()
def tokenize(line):
	words=re.findall('[\w]+|\d+',line)
	for key in range(0,len(words)):
		if(words[key]=="00"):
			words[key]="0"
	return([key.lower() for key in words])

def stem(line):
	return([stemmer.stemWord(key) for key in line])

def stopwords(line):
	return([key for key in line if stopword[key]!=1 and key!=" "])


def find_external(text):
	data=text.split("==External links==")
	if(len(data)<=1):
		data=text.split("== External links ==")
	links=[]
	temp=defaultdict(int)
	if(len(data)>1):
		lines=data[1].split("\n")
		for line in lines:
			if ("* [" in line) or ("*[" in line) :
				link=line.split(" ")
				words=[word for word in link if "http" not in word]
				links.append(' '.join(words))
		links=tokenize(' '.join(links))
		links=stopwords(links)
		links=stem(links)
	for word in links:
		temp[word]+=1
	return temp	


def find_reference(text):
	data=text.split("== References ==")
	"""
	if(len(data)<=1):
		data=text.split("==References==")
	if(len(data)<=1):
		data=text.split("==References and sources==")
	if(len(data)<=1):
		data=text.split("==References and notes==")
	if(len(data)<=1):
		data=text.split("== References and notes ==")
	if(len(data)<=1):
		data=text.split("== References and further reading ==")
	if(len(data)<=1):
		data=text.split("==References and further reading==")
	"""
	references=[]
	temp=""
	ref=defaultdict(int)
	if(len(data)>1):
		tempo=data[1].find('==')
		tokka=data[1][0:tempo]
		if '*' not in tokka:
			return ref
		lines=tokka.split("\n")
		for line in lines:
			if(line=="" or line[0]!='*'):
				continue
			if("title =" in line):
				words=re.findall('le =(.+?)\|',line)
				temp=(' '.join(words))
			elif("\'\'" in line):
				words=re.findall('\'\'(.+?)\'\'',line)
				temp=(' '.join(words))
			elif("\"" in line):
				words=re.findall('\"(.+?)\"',line)
				temp=(' '.join(words))
			words=temp.split(" ")
			word1=[word for word in words if "http" not in word]
			references.append(' '.join(word1))
		references=tokenize(' '.join(references))
		references=stopwords(references)
		references=stem(references)
	for word in references:
		ref[word]+=1
	return ref


def find_BIC(text):
	body_text=[]
	infobox=[]
	categories=[]
	text_flag=1
	ref_flag=0
	data=text.split("\n")
	for i in range(0,len(data)):
		jj=0
		if("{{Infobox" in data[i]):
			b_count=0
			temp=data[i].split("{{Infobox")[1:]
			infobox.append(' '.join(temp))
			while i < len(data)-1:
				if("{{" in data[i]):
					b_count+=data[i].count("{{")
				if("}}" in data[i]):
					b_count-=data[i].count("}}")
				if(b_count<=0):
					break
				i=i+1
				if(i>=len(data)):
					break
				jj+=1
				if(jj>21):
					break;
				temp=re.sub("{{Infobox","",data[i])
				temp1=temp.split("|")
				words=[]
				for wor in temp1:
					tk=wor.split('=')
					if(len(tk)>1):
						words.append(tk[1])
				temp=' '.join(words)
				words=temp.split(" ")
				word1=[word for word in words if "http" not in word]
				infobox.append(' '.join(word1))
				"""
				try:
					temp1=temp.split('=',1)[1]
					words=temp.split(" ")
					word1=[word for word in words if "http" not in word]
					infobox.append(' '.join(word1))
				except:
					pass
				"""
				#temp=data[i]
				#if("=" in temp):
				#	ind=temp.find("=")
				#	temp=temp[ind:]

				
		elif text_flag:
			if "==See also==" in data[i] or "== See also ==" in data[i] or "== References ==" in data[i] or "==References and sources==" in data[i] or "==References==" in data[i] or "== Bibliography ==" in data[i] or "==External links==" in data[i] or "== External links ==" in data[i] :
				text_flag=0
				continue
			if("<ref" in data[i] and "</ref>" in data[i]):
				store=data[i].split("<ref")
				for refa in store:
					if("</ref>" in refa):
						tok=refa.split("</ref>")
						if(len(tok)>1):
							body_text.append(tok[1])
					else:
						body_text.append(refa)
			else:
				if("<ref" in data[i]):
					ref_flag=1
					tem=data[i].find("<ref")
					body_text.append(data[i][0:tem])
				if(ref_flag==0):
					if("|" in data[i] and "=" in data[i]):
						tem2=data[i].find("=")
						data[i]=data[i][tem2:]
					body_text.append(data[i])
				if("</ref>" in data[i]):
					ref_flag=0
					tem=data[i].find("</ref>")
					body_text.append(data[i][tem:])
		elif "[[Category" in data[i]:
			words=re.findall('\[\[Category:(.+?)\]\]',data[i])
			categories.append(' '.join(words))
	finalise=' '.join(body_text)
	finalise=re.sub("<ref.*?/>"," ",finalise)
	finalise1=finalise.split(" ")
	finalise=[word1 for word1 in finalise1 if "http" not in word1]
	body_text=tokenize(' '.join(finalise))
	body_text=stopwords(body_text)
	body_text=stem(body_text)
	temp=defaultdict(int)
	for word in body_text:
		temp[word]+=1
	body_text=temp

	infobox=tokenize(' '.join(infobox))
	infobox=stopwords(infobox)
	infobox=stem(infobox)
	temp=defaultdict(int)
	for word in infobox:
		temp[word]+=1
	infobox=temp

	categories=tokenize(' '.join(categories))
	categories=stopwords(categories)
	categories=stem(categories)
	temp=defaultdict(int)
	for word in categories:
		temp[word]+=1
	#categories=temp

	return(body_text,infobox,temp)



def get_title(title):
	tokens=tokenize(title.encode('utf-8'))
	stop_removed=stopwords(tokens)
	stemmed_title=stem(stop_removed)
	title=defaultdict(int)
	for word in stemmed_title:
		title[word]+=1
	return title
	
def get_all(text):
	external_links=find_external(text)
	references=find_reference(text)
	#data=re.sub("<ref.*?/ref>"," ",text)
	data=re.sub('File:.*?px\|'," ",text)
	data=re.sub('File:.*?upright\|'," ",data)
	data=re.sub('File:.*?right\|'," ",data)
	data=re.sub('File:.*?upleft\|'," ",data)
	data=re.sub('File:.*?left\|'," ",data)
	data=re.sub('File:.*?thumb\|'," ",data)
	data=re.sub('File:.*?png\||File:.*?PNG\|'," ",data)
	data=re.sub('File:.*?jpg\||File:.*?JPG\|'," ",data)
	data=re.sub('Image:.*?px\|'," ",data)
	data=re.sub('Image:.*?right\|'," ",data)
	data=re.sub('Image:.*?upright\|'," ",data)
	data=re.sub('Image:.*?upleft\|'," ",data)
	data=re.sub('Image:.*?left\|'," ",data)
	data=re.sub('Image:.*?thumb\|'," ",data)
	data=re.sub('Image:.*?png\||File:.*?PNG\|'," ",data)
	data=re.sub('Image:.*?jpg\||File:.*?JPG\|'," ",data)
	body_text,infobox,categories=find_BIC(data)
	return(body_text,infobox,categories,external_links,references)
	