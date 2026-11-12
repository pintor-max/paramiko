import conexao 
import json

# Conectar-se ao equipamento R1 do inventário
#Lendo o arquivo JSON
with open('inventario.json','r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

#'dados' agora é um dicionário ou lista Python 
print(dados[0]["host"])

cliente=conexao.conectar(dados[0])


# Executar Whoami, hostname e uptime -p

codigo,saida, erro=conexao.executar(cliente,"whoami")

# Exibir, para cada comando, o código de saída, a saída e a saída de erro
print(f"Código: {codigo}")
print(f"Saída: {saida}")
print(f"Erro: {erro}")

# Executar também um comando inexistente 