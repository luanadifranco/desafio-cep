#ETAPA 1  - DESCOBRIR O CEP ALVO
lendo_cidades = True
cep_alvo = ""
with open("dados.txt", "r" , encoding="utf-8") as arquivos:
    for linha in arquivos:
        print(linha)
        linha_limpa = linha.strip()
        if linha_limpa == "--":
            lendo_cidades = False
            
        elif lendo_cidades == True:
                pass
        else:
            cep_alvo = linha_limpa
            print("CEP encontrado", cep_alvo)
        

#ETAPA 2 - DESCOBRIR A CIDADE DO CEP ALVO
cep_buscado = int(cep_alvo)
encontrou_cidade = False

with open("dados.txt", "r" , encoding="utf-8") as arquivos_leitura2:
    for linha in arquivos_leitura2:
        linha_limpa = linha.strip()
        if linha_limpa == "--":
            break

        pedacos = linha_limpa.split(",")
        nome_cidade = pedacos[0]
        cep_inicial = int(pedacos[1])
        cep_final = int(pedacos[2])

        if cep_buscado >= cep_inicial and cep_buscado<= cep_final:
             print("Cidade encontrada", nome_cidade)
             encontrou_cidade = True
             break
if not encontrou_cidade:
    print("Cidade não encontrada!")
        

    