'''
	O Criador de Tag apenas pega o meu endereco e 
	faz operacoes bit a bit tal que no final tenhamos 
	apenas a tag do meu endereco
'''
def  CriadorTag(BitsTag,Tag,Ra):
	Mask = 0x0
	BitsMask = 0
	i = 0
	if(BitsTag%4!=0):
		BitsMask = BitsTag/4
		while(i<BitsMask):
			Mask = Mask<<4
			Mask+=15
			i+=1

		if(BitsTag%4==1):
			Mask = Mask<<4
			Mask+=8
			Mask = Mask<<(32-4*(i+1)) 
		elif(BitsTag%4==2):
			Mask = Mask<<4
			Mask+=12
			Mask = Mask<<(32-4*(i+1)) 
		elif(BitsTag%4==3):
			Mask = Mask<<4
			Mask+=14
			Mask = Mask<<(32-4*(i+1)) 

		Tag = Ra & Mask
		Tag = Tag>>(32-4*(i+1))

	elif(BitsTag%4==0):
		BitsMask = BitsTag/4
		while(i<BitsMask):
			Mask = Mask<<4
			Mask+=15
			i+=1
		Mask = Mask<<(32-4*i)
		Tag = Ra & Mask
		Tag = Tag>>(32-4*i)
	
	
	return Tag	

'''
	O Criador de line apenas pega o meu endereco e 
	faz operacoes bit a bit tal que no final tenhamos 
	apenas a line do meu endereco.
'''

def CriadorLine(BitsLine,BitsWord,Line,Ra):
	Mask = 0x0
	aux = 0x0
	BitsMask = 0
	i = 0

	if(BitsLine%4!=0):
		BitsMask = BitsLine/4
		while(i<BitsMask):
			Mask  = Mask<<4
			Mask+=15
			i+=1

		if(BitsLine%4==1):
			aux+=1
			aux = aux<<4*BitsMask
			
			Mask = Mask|aux
		elif(BitsLine%4==2):
			aux+=3
			aux = aux<<4*BitsMask
			
			Mask = Mask|aux
		elif(BitsLine%4==3):
			aux+=7
			aux = aux<<4*BitsMask
			Mask = Mask|aux

	elif(BitsLine%4==0):
		BitsMask = BitsLine/4
		while(i<BitsMask):
			Mask  = Mask<<4
			Mask+=15
			i+=1

	Mask = Mask<<BitsWord
	Line = Ra & Mask
	Line = Line>>BitsWord
		
	return Line

'''
	O Criador de set apenas pega o meu endereco e 
	faz operacoes bit a bit tal que no final tenhamos 
	apenas a set do meu endereco
'''
def CriadorSet(BitsSet,BitsWord,Set,Ra):
	Mask = 0x0
	aux = 0x0
	BitsMask = 0
	i = 0

	if(BitsSet%4!=0):
		BitsMask = BitsSet/4
		while(i<BitsMask):
			Mask  = Mask<<4
			Mask+=15
			i+=1

		if(BitsSet%4==1):
			aux+=1
			aux = aux<<4*BitsMask
			
			Mask = Mask|aux
		elif(BitsSet%4==2):
			aux+=3
			aux = aux<<4*BitsMask
			
			Mask = Mask|aux
		elif(BitsSet%4==3):
			aux+=7
			aux = aux<<4*BitsMask
			Mask = Mask|aux

	elif(BitsSet%4==0):
		BitsMask = BitsSet/4
		while(i<BitsMask):
			Mask  = Mask<<4
			Mask+=15
			i+=1

	Mask = Mask<<BitsWord
	Set = Ra & Mask
	Set = Set>>BitsWord
		
	return Set



#Ordena o vetor com as tags , da tag mais utilizada para a tag menos utilizada
def OrdVectTags(VectTags,indicie,i):
	j = i
	contador = 0
	aux  = 0
	if(i!=0):
		while(contador<i):
			aux = VectTags[indicie + j]
			VectTags[indicie+j] = VectTags[indicie+(j-1)]
			VectTags[indicie+(j-1)] = aux
			contador+=1
			#print(j)
			j-=1

	return VectTags;

	

def FIFO(VectTags,indicie,LinhasSet,Tag):
	'''
		Funcoes de fila em python , pop() retira o primeiro da fila e append() 
		adiciona mais um a fila
	'''
	i = 1
	j = indicie
	aux = 0
	
	

	'''
		O while a sequir ira apenas subir os valores do conjunto uma posicao acima
		pois o "primeiro bloco" , ou seja minha Tag tem de sair e entao a nova e 
		adicionada ao final da fila
	'''
	
	while(i<LinhasSet):
		aux = VectTags[j]
		VectTags[j] = VectTags[j+1]
		VectTags[j+1] = aux
		j+=1
		i+=1

	VectTags[j] = Tag
	return VectTags



'''
	Apenas retira o menos recem utilizado, ou seja o ultimo da pilha 
	e coloca o novo no topo da minha pilha
'''
def LRU(VectTags,indicie,LinhasSet,Tag):
	i = LinhasSet-1
	aux = 0
	while(i>0):
		aux = VectTags[indicie + i-1]
		VectTags[indicie + i-1] = VectTags[indicie + i]
		VectTags[indicie + i] = aux
		i-=1
	VectTags[indicie] = Tag

	return VectTags



		