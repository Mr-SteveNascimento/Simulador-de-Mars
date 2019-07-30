
# Implementação de um simulador de memória CACHE por Steve Nascimento
# 			
# CACHE de 192 bytes (96 Linhas de 8 bits)
import time
		

def main():

	print("..................Bem Vindo ao Simulador de memória CACHE..................")
	print()
	print("ATENÇÂO")
	print("Ao inserir um arquivo no simulador, certifique-se que os espaçamentos estão corretos")
	print("Exemplo:")
	print("INSTRUCOES TIPO ADD: 'add $1,$2,$3'")
	print("INSTRUCOES TIPO ADDI: 'addi $1,$2,10'")
	print("INSTRUCOES TIPO J: 'j LABEL'")
	print("INSTRUCOES TIPO LABEL: 'LABEL:'")
	print("INSTRUCOES TIPO BEQ: 'beq $3,$4,L1'")
	print("INSTRUCOES TIPO BNE: 'bne $3,$4,L1'")
	print()
	nome = str(input("Insira a seguir o nome do arquivo em cógido assembly com extensão: "))

	memorias = cacheRegistersGenerate()
	exception = inicializacaoDoArquivo(nome)

	if (exception == 0):
		return 0
	else:
		REG = memorias[0]
		CACHE = memorias[1]
		INSTRUCOES = exception

		calculo(REG,CACHE,INSTRUCOES)
	
	return 0

def cacheRegistersGenerate():

	# Registers 

	REG = [[],[]]
	for i in range(8):
		REG[0].append("0")
	for i in range(10):
		REG[1].append("0")

	# CACHE

	CACHE = []
	for i in range(96):
		CACHE.append("0")

	return ([REG,CACHE])

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
	print()
	print()
	print()
	print("      REGISTRADORES")
	print()
	print("      ----------------------------")
	print("      |   REG     |     VALOR    |")
	print("      ----------------------------")
	for i in range(8):
		print(("      |    ${0}     |       {1}      |").format(i, res[0][i]))
	for i in range(10):
		print(("      |    t{0}     |       {1}      |").format(i, res[1][i]))
	print("      ----------------------------")	
	print()
	print("     INSTRUÇÕES")
	print()
	for i in range(len(inst)):
		print(("     {}").format(inst[i]))
	print()
	print()
	print("*********************************************************************")

	return 0

def conversorDeInstrucoes(lista):

	# Retirando todos os /n e removendo as linhas vazias
	for i in range(len(lista)):
		lista[i] = lista[i].rstrip()
	total = len(lista)
	i = 0
	while i < total:
		if(lista[i]  == "" or lista[i] == " "):
			del(lista[i])
			total-=1
		else:
			i+=1

	return(lista)

def calculo(REG,CACHE,INSTRUCOES):
	resultados = REG
	imprimirMatriz(REG,INSTRUCOES)
	branch = 0
	i = 0
	laco = 0
	REG[0][1] = "5"
	REG[0][0] = "1"
	while (i < len(INSTRUCOES)):
		if (laco == 0):
			time.sleep(10)
			laco = 1
		else:
			time.sleep(3)
		atual = INSTRUCOES[i]
		INSTRUCOES[i] += "*"

		if (INSTRUCOES[i][0] == " "):
			print("Remova o espaço no início da seguinte instrução!!!")
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			print(("{} na linha {}").format(INSTRUCOES[i], i+1))
			break
			
		elif (INSTRUCOES[i][:4] == "addi"):
			resultados = addi(resultados,atual)
			if (resultados == 0):
				break
			imprimirMatriz(resultados,INSTRUCOES)

		elif (INSTRUCOES[i][:3] == 'add'):
			resultados = add(resultados,atual)
			if (resultados == 0):
				break
			imprimirMatriz(resultados,INSTRUCOES)

		elif (INSTRUCOES[i][:2] == "lw"):
			resultados = lw(resultados,CACHE,atual)
			if (resultados == 0):
				break
			imprimirMatriz(resultados,INSTRUCOES)

		elif (INSTRUCOES[i][:2] == "sw"):
			resultados = sw(resultados,CACHE,atual)
			if (resultados == 0):
				break
			imprimirMatriz(resultados,INSTRUCOES)

		elif (atual[-1] == ":"):
			imprimirMatriz(resultados,INSTRUCOES)
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			i+=1
			continue

		elif (INSTRUCOES[i][0] == "j"):
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			branch = j(atual,INSTRUCOES)
			if (branch == "Erro"):
				print("Seu jumper não funcionou, verifique se o label está correto!!!")
				print(("{} na linha {}").format(INSTRUCOES[i], i+1))
				break
			INSTRUCOES[i] += "*"
			imprimirMatriz(resultados,INSTRUCOES)

		elif (INSTRUCOES[i][:3] == "bne"):
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			branch = bne(atual,resultados,INSTRUCOES)
			if (branch == "Erro"):
				print("Seu branch if not equals não funcionou, verifique se o label está correto!!!")
				print(("{} na linha {}").format(INSTRUCOES[i], i+1))
				break
			INSTRUCOES[i] += "*"
			imprimirMatriz(resultados,INSTRUCOES)

		elif (INSTRUCOES[i][:3] == "beq"):
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			branch = beq(atual,resultados,INSTRUCOES)
			if (branch == "Erro"):
				print("Seu branch if equals não funcionou, verifique se o label está correto!!!")
				print(("{} na linha {}").format(INSTRUCOES[i], i+1))
				break
			INSTRUCOES[i] += "*"
			imprimirMatriz(resultados,INSTRUCOES)

		else:
			print("Esta seguinte instrução não foi reconhecida!!!")
			INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
			print(INSTRUCOES[i])
			break

		INSTRUCOES[i] = INSTRUCOES[i].replace("*", "")
		if (branch == 0):
			i +=1
		else:
			i = branch-1
			branch = 0

def add(res,inst):
	try:
		reg1 = list(inst[4:6])
		reg2 = list(inst[7:9])
		reg3 = list(inst[10:])
		valor1 = 0
		valor2 = 0
		valor3 = 0
		if (reg1[0] == "$"):
			valor1 = int(res[0][int(reg1[1])])
		else:
			valor1 = int(res[1][int(reg1[1])])
		if (reg2[0] == "$"):
			valor2 = int(res[0][int(reg2[1])])
		else:
			valor2 = int(res[1][int(reg2[1])])
		if (reg3[0] == "$"):
			valor3 = int(res[0][int(reg3[1])])
		else:
			valor3 = int(res[1][int(reg3[1])])
	except:
		print("Erro de formatação na instrução add!! (Verifique se há algum espaço no final)")
		return 0
	else:
		valor1 = valor2 + valor3
		if (reg1[0] == "$"):
			res[0][int(reg1[1])] = str(valor1)
		else:
			res[1][int(reg1[1])] = str(valor1)

	return res

def addi(res,inst):
	try:
		reg1 = list(inst[5:7])
		reg2 = list(inst[8:10])
		reg3 = inst[11:]
		valor1 = 0
		valor2 = 0
		valor3 = 0
		if (reg1[0] == "$"):
			valor1 = int(res[0][int(reg1[1])])
		else:
			valor1 = int(res[1][int(reg1[1])])
		if (reg2[0] == "$"):
			valor2 = int(res[0][int(reg2[1])])
		else:
			valor2 = int(res[1][int(reg2[1])])
		valor3 = int(reg3)
	except:
		print("Erro de formatação da instrução addi!! (Verifique se há algum espaço no final)")
		return 0
	else:
		valor1 = valor2 + valor3
		if (reg1[0] == "$"):
			res[0][int(reg1[1])] = str(valor1)
		else:
			res[1][int(reg1[1])] = str(valor1)
	return res

def lw(res,cache,inst):
	try:
		reg1 = list(inst[3:5])
		imm = 0
		reg2 = []
		resto = list(inst[6:])
		valor1 = 0
		if (reg1[0] == "$"):
			valor1 = int(res[0][int(reg1[1])])
		else:
			valor1 = int(res[1][int(reg1[1])])
		if (len(resto) == 5):
			imm == int(inst[6])
			reg2.append(inst[8:10])
		elif (len(resto) == 6):
			imm == int(inst[6:8])
			reg2.append(inst[10:12])
		else:
			print("Erro de formatação do lw, verifique se existe este endereço na CACHE ou se há espaço no final da instrução!")
			return 0
		reg2 = list(reg2[0])
	except:
		print("Erro de formatação do lw, verifique os espaços!")
		return 0
	else:
		valor2 = 0
		if (reg2[0] == "$"):
			valor2 = int(res[0][int(reg2[1])])
		else:
			valor2 = int(res[1][int(reg2[1])])

		try:
			valor3 = valor2 + imm
			valor = cache[valor3-1]
		except:
			print("Não existe esta posição de memória!!")
			return 0
		else:
			if (reg1[0] == "$"):
				res[0][int(reg1[1])] = str(valor)
			else:
				res[1][int(reg1[1])] = str(valor)
			return res

def sw(res,cache,inst):
	try:
		reg1 = list(inst[3:5])
		imm = 0
		reg2 = []
		resto = list(inst[6:])
		valor1 = 0
		if (reg1[0] == "$"):
			valor1 = int(res[0][int(reg1[1])])
		else:
			valor1 = int(res[1][int(reg1[1])])
		if (len(resto) == 5):
			imm == int(inst[6])
			reg2.append(inst[8:10])
		elif (len(resto) == 6):
			imm == int(inst[6:8])
			reg2.append(inst[10:12])
		else:
			print("Erro de formatação do lw, verifique se existe este endereço na CACHE ou se há espaço no final da instrução!")
			return 0
		reg2 = list(reg2[0])
		valor2 = 0
		if (reg2[0] == "$"):
			valor2 = int(res[0][int(reg2[1])])
		else:
			valor2 = int(res[1][int(reg2[1])])

	except:
		print("Erro de formatação do lw, verifique os espaços!")
		return 0
	else:
		try:
			valor3 = valor2 + imm
			cache[valor3-1] = valor1
		except:
			print("Não existe esta posição de memória!!")
			return 0
		else:
			return res

def j(inst,INSTRUCOES):
	control = 0
	branch = 0
	for i in range(len(INSTRUCOES)):
		if(INSTRUCOES[i][:-1] == inst[2:]):
			branch = i+1
			control = 1
	if (control == 0):
		return ("Erro")
	else:
		return (branch)

def bne(inst,res,INSTRUCOES):
	try:
		reg1 = list(inst[4:6])
		reg2 = list(inst[7:9])
		label = inst[10:]
		valor1 = 0
		valor2 = 0
		if (reg1[0] == "$"):
			valor1 = int(res[0][int(reg1[1])])
		else:
			valor1 = int(res[1][int(reg1[1])])
		if (reg2[0] == "$"):
			valor2 = int(res[0][int(reg2[1])])
		else:
			valor2 = int(res[1][int(reg2[1])])
	except:
		print("Erro de formatação na instrução bne!! (verifique os espaços)")
		return("Erro")
	else:
		if (valor1 != valor2):
			control = 0
			branch = 0
			for i in range(len(INSTRUCOES)):
				if(INSTRUCOES[i][:-1] == inst[10:]):
					branch = i+1
					control = 1
			if (control == 0):
				return ("Erro")
			else:
				return (branch)
		else:
			return 0

def beq(inst,res,INSTRUCOES):
	try:
		reg1 = list(inst[4:6])
		reg2 = list(inst[7:9])
		label = inst[10:]
		valor1 = 0
		valor2 = 0
		if (reg1[0] == "$"):
			valor1 = int(res[0][int(reg1[1])])
		else:
			valor1 = int(res[1][int(reg1[1])])
		if (reg2[0] == "$"):
			valor2 = int(res[0][int(reg2[1])])
		else:
			valor2 = int(res[1][int(reg2[1])])
	except:
		print("Erro de formatação na instrução bne!! (verifique os espaços)")
		return("Erro")
	else:
		if (valor1 == valor2):
			control = 0
			branch = 0
			for i in range(len(INSTRUCOES)):
				if(INSTRUCOES[i][:-1] == inst[10:]):
					branch = i+1
					control = 1
			if (control == 0):
				return ("Erro")
			else:
				return (branch)
		else:
			return 0

main()