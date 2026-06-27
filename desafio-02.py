# ETAPA 1 - DESCOBRIR O CEP ALVO
etapa = 1
lista_cidades = []
lista_conexoes = []
ceps_finais = ""

with open("dados2.txt", "r", encoding="utf-8") as arquivos:
    for linha in arquivos:
        print(linha)
        linha_limpa = linha.strip()

        if linha_limpa == "--":
            etapa = etapa + 1
            continue

        if etapa == 1:
            pedacos = linha_limpa.split(",")
            lista_cidades.append(pedacos)

        elif etapa == 2:
            pedacos = linha_limpa.split(",")
            lista_conexoes.append(pedacos)

        elif etapa == 3:
            ceps_finais = linha_limpa
            print("CEP final encontrado: ", ceps_finais)

# ETAPA 2 - SEPARAR OS CEPS FINAIS
pedacos_ceps = ceps_finais.split(",")
cep_origem = int(pedacos_ceps[0])
cep_destino = int(pedacos_ceps[1])

cidade_origem = ""
cidade_destino = ""

for cidade in lista_cidades:
    nome_cidade = cidade[0]
    cep_inicial = int(cidade[1])
    cep_final = int(cidade[2])

    if cep_origem >= cep_inicial and cep_origem <= cep_final:
        cidade_origem = nome_cidade
        #print("Cidade de origem encontrada: ", cidade_origem)

    if cep_destino >= cep_inicial and cep_destino <= cep_final:
        cidade_destino = nome_cidade

print(f"Cidade de destino: Cidade {cidade_destino} (cep: {cep_destino})")
print(f"Cidade de origem: Cidade {cidade_origem} (cep: {cep_origem})")

grafo = {}

for conexao in lista_conexoes:
    origem = conexao[0]
    destino = conexao[1]
    custo = float(conexao[2])

    if origem not in grafo:
        grafo[origem] = {}
    grafo[origem][destino] = custo

    if destino not in grafo:
        grafo[destino] = {}
    grafo[destino][origem] = custo

import heapq

def encontrar_menor_caminho(mapa, inicio, fim):
    fila = [(0.0, inicio, [inicio])]
    visitados = set()

    while fila:
        (custo_atual, cidade_atual, caminho) = heapq.heappop(fila)

        if cidade_atual == fim:
            return caminho, custo_atual
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            vizinhas = mapa.get(cidade_atual, {})

            for vizinha, custo in vizinhas.items():
                if vizinha not in visitados:
                    custo_total = custo_atual + custo
                    heapq.heappush(fila, (custo_total, vizinha, caminho + [vizinha]))

    return None, float('inf')

rota, custo_total = encontrar_menor_caminho(grafo, cidade_origem, cidade_destino)

if rota:
    print("Rota encontrada: ", " -> ".join(rota))
    print("Custo total: ", custo_total)

else:
    print("Não foi possível encontrar uma rota.")




    
