from MapDirect import MapDirect
from MapSetAssosiative import MapSetAssosiative
class MainCache():
	TaxaAcerto = 0
	TaxaErro = 0
	lista = []
	hit = 0
	miss = 0
	i = 0
	j = 4
	linhasSet = [2,4,8]
	TamanhosCache = [1024,2048,4096,8192,16384]
	Resultados  = open("Result","a")
	with open('trace','r') as arq:
		lista = arq.read().splitlines()

	
	
	while(i<len(lista)):
		c =  MapSetAssosiative(TamanhosCache[j],8,16,"FIFO",lista[i])
		if(c.VerificarCache()==1):
			hit+=1
		else:
			miss+=1
		i+=1
	Resultados.write("\nMapeamento Associatio em conjunto FIFO-8-way| %i" %(TamanhosCache[j]))
	Resultados.write("\nEnderecos Lidos: 1012176")
	Resultados.write("\nAcertos: %i" %(hit))
	Resultados.write("\nFalhas: %i" %(miss))
	TaxaAcerto = 100*(hit/1012176.0)
	TaxaErro = 100*(miss/1012176.0)
	Resultados.write("\nTaxa de acertos: %f" %TaxaAcerto )
	Resultados.write("\nTaxa de Falhas: %f" %TaxaErro )
	Resultados.write("\n==============================")
	Resultados.close()
		
	