import os
from automata import *

def parserDocument():
	os.remove('parser.txt')
	#coarse source file
	src=open('source.txt','r')
	#final file without Car Returns with whitespace 
 	#after of characters ';' and '{' or '}'
	finalFile=open('parser.txt','a')
	for line in src.readlines():
		s=line
		for char in s:
			# detection the characters for whitespace
			if char == ';' or char=='{' or char=='}':
				pos=s.index(char)+1
				l=s[0:pos]
				r=s[pos:len(s)]
				s=l+' '+r
		s=s.strip('\n')
		s=s.strip('\t')
		s=s+' ';	
		finalFile.write(s)
	print('Archivo depurado satisfactoriamente')
    	finalFile=open("parser.txt")
	lis=finalFile.readline().split()
	for c in lis:
		print(c)
	src.close()
	
	finalFile.close()

parserDocument()
