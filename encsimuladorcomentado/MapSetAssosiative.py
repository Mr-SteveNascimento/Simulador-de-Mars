import Modulo
class MapSetAssosiative(object):
	"""docstring for MapSetAssosiative"""
	Ra = 0x0
	Tag = 0x0
	Mask = 0x0
	Set = 0x0
	VectTags = []
	BitUses = []
	BitsTag = 0
	BitsSet = 0
	BitsWord = 0
	NumbersSets = 0
	Escrita = ''
	Lines = 0
	LinhasSet = 0
	'''
		Construtor da Cache com mapeamento assosiativo em conjunto 
		a funcao verificarCache Verifica se o meu endereco passado 
		esta na Cache 
	'''

	def __init__(self,TamanhoCache,LinhasSet,TamanhoBloco,Escrita,Ra):
		self.LinhasSet = LinhasSet
		self.NumbersSets = TamanhoCache/(TamanhoBloco*LinhasSet)
		self.Lines = self.NumbersSets*LinhasSet
		while(TamanhoBloco%2==0):
			self.BitsWord+=1
			TamanhoBloco/=2
		
		
		while(self.NumbersSets%2==0):
			self.BitsSet+=1
			self.NumbersSets/=2
		self.BitsTag = 32 - (self.BitsSet + self.BitsWord)
		self.Ra = int(Ra,16)
		self.Escrita = Escrita

	#Verifica se a minha Cache contem o bloco acessado
	def VerificarCache(self):
		i=0
		aux = 0
		self.Tag = Modulo.CriadorTag(self.BitsTag,self.Tag,self.Ra)
		#A variavel Tag recebe apenas a parte da tag do endereco
		self.Set = Modulo.CriadorSet(self.BitsSet,self.BitsWord,self.Set,self.Ra)
		#A variavel set recebe apenas a aparte da set do endereco
		self.indicie = self.LinhasSet*self.Set
		#indicie no qual começa o meu conjunto

		#Cria um vetor de zeros para o vetor de tags
		if(len(self.VectTags)==0):
			while(i<self.Lines):
				self.VectTags.append(0)
				i+=1
			i = 0
			
		'''
			Verificando se existe o bloco acessado na cache
			,Caso existir e a politica de escrita for LRU,
			tem que ordenar o meu conjunto para que o recem 
			acessado fique no topo, e o menos recente acessado 
			fique no final da pilha
		'''
		i=0
		while(i<self.LinhasSet):
			if(self.VectTags[self.indicie+i]==self.Tag):
				if(self.Escrita=="LRU"):
					self.VectTags =  Modulo.OrdVectTags(self.VectTags,self.indicie,i)
			
				return 1
				break
			i+=1
			
		

		i = 0
		
		#Apenas verifica se um conjunto esta cheio
		while(i<self.LinhasSet):
			if(self.VectTags[self.indicie+i]!=0):
				aux+=1
			i+=1

		
		#Caso esteja escolhe-se a politica de substituicao.
		if(aux==self.LinhasSet):
			
			if(self.Escrita=='FIFO'):
				self.VectTags = Modulo.FIFO(self.VectTags,self.indicie,self.LinhasSet,self.Tag)
				return 0 
			else:
				self.VectTags = Modulo.LRU(self.VectTags,self.indicie,self.LinhasSet,self.Tag)
				return 0
					
		
		#Senao eu apenas adiciono a pilha colocando-a no topo caso for recente
		else:
			if(self.Escrita=="FIFO"):

				i = 0
				aux = 0	
				while(i<self.LinhasSet):
					if(self.VectTags[self.indicie+i]!=0):
						aux+=1
					i+=1
				self.VectTags[self.indicie+aux] = self.Tag
			
			else:
				i = 0
				aux = 0	
				while(i<self.LinhasSet):
					if(self.VectTags[self.indicie+i]!=0):
						aux+=1
					i+=1
				self.VectTags[self.indicie+aux] = self.Tag
				self.VectTags = Modulo.OrdVectTags(self.VectTags,self.indicie,aux)
			

		


		
	

		
		
					