#ETAPA 1  - DESCOBRIR O CEP ALVO
lendo_cidades = True
cep_alvo = ""
lista_cidades = []

with open("dados.txt", "r" , encoding="utf-8") as arquivos:

    for linha in arquivos:
        print(linha)
        linha_limpa = linha.strip()
        
        if linha_limpa == "--":
            lendo_cidades = False
            
        elif lendo_cidades == True:
            pedacos = linha_limpa.split(",")
            lista_cidades.append(pedacos)
        
        else:
            cep_alvo = linha_limpa
            print("CEP encontrado", cep_alvo)
        

#ETAPA 2 - DESCOBRIR A CIDADE DO CEP ALVO
cep_buscado = int(cep_alvo)
encontrou_cidade = False

for cidade in lista_cidades:
    nome_cidade = cidade[0]
    cep_inicial = int(cidade[1])
    cep_final = int(cidade[2])

    if cep_buscado >= cep_inicial and cep_buscado <= cep_final:
        print("Cidade encontrada", nome_cidade)
        encontrou_cidade = True
        

if not encontrou_cidade:
    print("Cidade não encontrada!")
        

    