import Modulo
class MapDirect(object):
	"""docstring for MapDirect"""
	TamanhoCache = 0
	Ra = 0x0
	Tag = 0x0
	Line = 0x0
	VectTags = []
	BitsTag = 0
	BitsLine = 0
	BitsWord = 0
	indicie = 0
	aux = 0
	'''
	Construtor da Cache com  Mapeamento Direto , Dentro dele contruimos quantos bits existem na Tag,Line e Word
	Com a funcao VerificarCache , descobrimos se aquele endereco especifico esta dentro da memoria Cache

	'''
	#Construtor define o tamanho de cada parte do endereco 
	def __init__(self,TamanhoCache,TamanhoBloco,Ra):
		while(TamanhoBloco%2==0):
			self.BitsWord+=1
			TamanhoBloco/=2
		while(TamanhoCache%2==0):
			self.BitsLine+=1
			TamanhoCache/=2
		self.BitsLine-=self.BitsWord
		self.BitsTag = 32 - (self.BitsLine+self.BitsWord)
		self.Ra = int(Ra,16)

	
	#Essa funcao verifica se existe um bloco na cache
	def VerificarCache(self):
		i=0
		self.Tag = Modulo.CriadorTag(self.BitsTag,self.Tag,self.Ra)
		#A variavel Tag recebe apenas a parte da tag do endereco
		self.Line = Modulo.CriadorLine(self.BitsLine,self.BitsWord,self.Line,self.Ra)
		#A variavel line recebe apenas a aparte da line do endereco
		self.indicie = self.Line
		
		
		if(self.indicie<=2**self.BitsTag):
			while(self.indicie>=2**self.BitsLine):
				self.indicie-=2**self.BitsLine
		#Indicie indica onde eu devo salvar a minha tag ,pois o mapeamento e direto
		
		

		#Cria um vetor de zeros para o vetor de tags
		if(len(self.VectTags)==0):
			while(i<2**(self.BitsLine)):
				self.VectTags.append(0)
				i+=1

		'''
			Verificando se a tag esta no meu vetor de tags
			se estiver eh porque eu tenho aquele endereco 
			na minha cache , senao eu atualizo ela , colocando
			no meu vetor de tags
		'''
		
		if(self.VectTags[self.indicie]==self.Tag):
			return 1

		
		else:
			self.VectTags[self.indicie] = self.Tag
			return 0 

		
				
			




		
		