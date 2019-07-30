

# Implementação de um simulador de memória cache po Steve Nascimento
# 
# Mapeamento direto				
# 
# Política de Substituição FIFO
#
# RAM de 96 bytes ou 768 bits (24 Blocos de 4 linhas de 1 byte)
#
# CACHE de 32 bytes (8 Linhas de 32 bits)







		

def main():

	print("..................Bem Vindo ao Simulador de memória CACHE..................")
	print()
	print("ATENÇÂO")
	print("Ao inserir um arquivo no simulador, certifique-se que os espaçamentos estão corretos")
	print("Exemplo:")
	print("INSTRUCOES TIPO R: 'add $1,$2,$3'")
	print("INSTRUCOES TIPO I: 'addi $1,$2,10'")
	print("INSTRUCOES TIPO J: 'j 15'")
	print()
	nome = str(input("Insira a seguir o nome do arquivo em cógido assembly com extensão: "))

	memorias = ramCacheRegistersGenerate()
	exception = inicializacaoDoArquivo(nome)

	if (exception == 0):
		return 0
	else:
		REG = memorias[0]
		RAM = memorias[1]
		CACHE = memorias[2]
		INSTRUCOES = exception

		calculo(REG,RAM,CACHE,INSTRUCOES)

def ramCacheRegistersGenerate():

	# Registers 

	REG = [[],[]]
	for i in range(8):
		REG[0].append([])
	for i in range(10):
		REG[1].append([])

	# RAM

	RAM = []
	for i in range(96):
		RAM.append(["00000000"])

	# CACHE

	CACHE = []
	for i in range(8):
		CACHE.append(["00000000000000000000000000000000"])

	return ([REG,RAM,CACHE])

def inicializacaoDoArquivo(nome):

	# Tratamento de erro de arquivo inexistente

	try:
		arquivo = open(nome, 'r')

	except:
		print()
		print("Não existe arquivo neste diretório com este nome!!!")
		print()

		return 0

	else:
		lista = arquivo.readlines()
		arquivo.close()
		newlista = conversorDeInstrucoes(lista)
		return (newlista)

def imprimirMatriz(res,inst):
	
	print()
	print("REGISTRADORES")
	print()
	print("----------------------------")
	print("    REG     |     VALOR     ")
	print("----------------------------")
	for i in range(8):
		print("    $"+ str(i)+"    |    "+str(res[0][i])+"    ")
	for i in range(10):
		print("    t"+ str(i)+"    |    "+str(res[1][i])+"    ")
	print("----------------------------")	
	print()
	print("INSTRUÇỖES")
	print()
	for i in range(len(inst)):
		print(inst[i])
	print()
	print()
	print("*********************************************************************")

def conversorDeInstrucoes(lista):

	# Retirando todos os /n e removendo as linhas vazias
	for i in range(len(lista)):
		lista[i] = lista[i].rstrip()
	total = len(lista)
	i = 0
	while i < total:
		if(lista[i]  == ""):
			del(lista[i])
			total-=1
		i+=1
	return(lista)

def calculo(REG,RAM,CACHE,INSTRUCOES):
	resultados = REG
	for i in range(len(INSTRUCOES)):

		#Mostra a linha que está sendo executada
		INSTRUCOES[i] += "*"
		if (INSTRUCOES[i][:3] == 'add'):
			resultados = add(resultados)
		elif (INSTRUCOES[i][:4] == "addi"):
			resultados = addi(resultados)
		elif (INSTRUCOES[i][:2] == "lw"):
			resultados = lw(resultados)
		elif (INSTRUCOES[i][0] == "j"):		
			resultados = j(resultados)
		elif (INSTRUCOES[i][:3] == "bne"):
			resultados = bne(resultados)
		elif (INSTRUCOES[i][:3] == "beq"):
			resultados = beq(resultados)
		else:
			print("Esta seguinte instrução não foi reconhecida!!!")
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			print(INSTRUCOES[i])
			break

		INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
		print('EXECUTOU')

		











def add(res):
	print("Oi, Eu sou goku!")


def addi(res):
	print("Oi, Eu sou goku!")


def lw(res):
	print("Oi, Eu sou goku!")


def j(res):
	print("Oi, Eu sou goku!")


def bne(res):
	print("Oi, Eu sou goku!")


def beq(res):
	print("Oi, Eu sou goku!")

















main()