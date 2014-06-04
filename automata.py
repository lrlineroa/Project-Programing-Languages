import os

Y='Acept'
alphaB=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
AlphaB=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']


def autoDefVariables():
	G={}
	G[0]=[(alphaB,1)]
	G[1]=[(alphaB,1),(AlphaB,1),(digits,1),('=',2)]
	G[2]=[(digits[1:len(digits)],3),('"',4)]
	G[3]=[(digits,3),Y]
	G[4]=[(alphaB,4),(digits,4),('"',5)]
	G[5]=[Y]
	return G
def autoNameAgent():
	G={}
	G[0]=[(AlphaB,1)]
	G[1]=[(alphaB,1),('.',2)]
	G[2]=[(digits,3)]
	G[3]=[Y]	
	return G
#chain is the string to evaluate
#G is the automaton in which chain will be evaluate
def evaluateAutomaton(chain,G):
	
	cursor=0#counter that walks the automaton
	#counter that walks the chain
	for counter in range(0,len(chain)):
		flag=True
		subTree=G[cursor]
		if subTree=='Acept':
			cursor+=1
			break
		sizeT=len(subTree)
		if sizeT==1:
			if chain[counter] in subTree[0][0]:
				cursor=subTree[0][1]
			else:
				cursor=-1
				flag=False
		elif sizeT>1:
			for cur in range(0,len(subTree)+1):
				if cur==len(subTree):
					cursor=-1;
					flag=False
					break
				if chain[counter] in subTree[cur][0]:
					cursor=subTree[cur][1]
					break
				 
		if not(flag) or cursor==-1:
			break	
	if cursor!=-1 and 'Acept' in G[cursor]:
		return 'Evaluacion exitosa'
	else:	
		return 'Evaluacion infructuosa'
#Shell
Automaton=autoNameAgent()
testNameAgent=['Amigazo.5','amigazo.4','a.3','a,3','A.3','A,3']
testDefVariables=['hola8="temp"','a9=2','a3=32d','x=8','x=d']
print "======================="
print "test nombre del agente"
print "======================="
for i in range(0,len(testNameAgent)):
	print testNameAgent[i],"  ",evaluateAutomaton(testNameAgent[i],Automaton)
print "======================="
print "test definicion de las variables"
print "======================="
Automaton=autoDefVariables()
for i in range(0,len(testDefVariables)):
	print testDefVariables[i],"  ",evaluateAutomaton(testDefVariables[i],Automaton)
print "======================="
