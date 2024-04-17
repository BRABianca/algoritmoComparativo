from pathlib import Path
import re

def ler_numeros_arquivo(caminho):
    numeros = []
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            numero = linha.split(';')[0].strip()
            numeros.append(numero)
    return numeros

def extrair_localidade(nome_arquivo):
    """Extrai a parte 'LOCALIDADE' do nome do arquivo."""
    match = re.match(r"(.*)_rdatrech|(.*)_RDA_handle_data", nome_arquivo.stem)
    if match:
        localidade = match.group(1) if match.group(1) else match.group(2)
        return localidade.lower()
    else:
        print(f"Não foi possível extrair a localidade do arquivo {nome_arquivo}")
        return None
    
def comparar_localidades(localidade1, localidade2):
    """Compara duas localidades ignorando maiúsculas e minúsculas, e ignorando um número específico de caracteres no final."""
    if localidade1 is not None and localidade2 is not None:
        return localidade1.lower() == localidade2.lower()
    else:
        return False


def encontrar_valores_nao_pares(valores_grupo1, valores_grupo2):
    valores_nao_pares = []

    for valor in valores_grupo1:
        if valor not in valores_grupo2:
            valores_nao_pares.append(valor)

    for valor in valores_grupo2:
        if valor not in valores_grupo1 and valor not in valores_nao_pares:
            valores_nao_pares.append(valor)

    return valores_nao_pares

# Diretórios das pastas contendo os arquivos
pasta_grupo1 = Path('C:/PRJ/ESTAGIARIOS/Bianca/algoritmoComparativo/algoritmoComparativo/src/rdatrech')
pasta_grupo2 = Path('C:/PRJ/ESTAGIARIOS/Bianca/algoritmoComparativo/algoritmoComparativo/src/handle')

# Lista os arquivos nas pastas
arquivos_grupo1 = list(pasta_grupo1.glob('*.txt'))
arquivos_grupo2 = list(pasta_grupo2.glob('*.txt'))

# Diretório para o arquivo de saída
arquivo_saida = Path('saida/saida_geral.txt')
if not arquivo_saida.parent.exists():
    arquivo_saida.parent.mkdir(parents=True)

# Armazenar os nomes dos arquivos já processados em um conjunto para referência
arquivos_processados = set()

# Dicionário para armazenar os valores não pares por localidade
valores_nao_pares_por_localidade = {}

# Ler e comparar os arquivos
for arquivo_grupo1 in arquivos_grupo1:
    valores_grupo1 = ler_numeros_arquivo(arquivo_grupo1)

    # Extrair a localidade do arquivo
    localidade_arquivo_grupo1 = extrair_localidade(arquivo_grupo1)

    # Encontrar o arquivo correspondente no grupo 2
    arquivo_grupo2_correspondente = None
    for arquivo_grupo2 in arquivos_grupo2:
        localidade_arquivo_grupo2 = extrair_localidade(arquivo_grupo2)
        if comparar_localidades(localidade_arquivo_grupo1, localidade_arquivo_grupo2):
            arquivo_grupo2_correspondente = arquivo_grupo2
            break

    if arquivo_grupo2_correspondente is None:
        print(f"Não encontrou arquivo correspondente para {arquivo_grupo1}")
        continue

    valores_grupo2 = ler_numeros_arquivo(arquivo_grupo2_correspondente)

    # Armazenar os arquivos processados
    arquivos_processados.add(localidade_arquivo_grupo1)
    arquivos_processados.add(localidade_arquivo_grupo2)

    # Encontrar valores não pares
    valores_nao_pares = encontrar_valores_nao_pares(valores_grupo1, valores_grupo2)

    # Armazenar os valores não pares por localidade
    if localidade_arquivo_grupo1 in valores_nao_pares_por_localidade:
        valores_nao_pares_por_localidade[localidade_arquivo_grupo1].extend(valores_nao_pares)
    else:
        valores_nao_pares_por_localidade[localidade_arquivo_grupo1] = valores_nao_pares

# Verificar arquivos não processados e processá-los
for arquivo_grupo2 in arquivos_grupo2:
    localidade_arquivo_grupo2 = extrair_localidade(arquivo_grupo2)
    
    if localidade_arquivo_grupo2 not in arquivos_processados:
        # Encontrar o arquivo correspondente no grupo 1
        arquivo_grupo1_correspondente = None
        for arquivo_grupo1 in arquivos_grupo1:
            localidade_arquivo_grupo1 = extrair_localidade(arquivo_grupo1)
            if comparar_localidades(localidade_arquivo_grupo1, localidade_arquivo_grupo2):
                arquivo_grupo1_correspondente = arquivo_grupo1
                break
                
        if arquivo_grupo1_correspondente is None:
            print(f"Não encontrou arquivo correspondente para {arquivo_grupo2}")
            continue
        
        valores_grupo1 = ler_numeros_arquivo(arquivo_grupo1_correspondente)
        valores_grupo2 = ler_numeros_arquivo(arquivo_grupo2)
        
        # Encontrar valores sem pares
        valores_nao_pares = encontrar_valores_nao_pares(valores_grupo1, valores_grupo2)
        
        # Armazenar os arquivos processados
        arquivos_processados.add(localidade_arquivo_grupo2)

        # Armazenar os valores não pares por localidade
        if localidade_arquivo_grupo2 in valores_nao_pares_por_localidade:
            valores_nao_pares_por_localidade[localidade_arquivo_grupo2].extend(valores_nao_pares)
        else:
            valores_nao_pares_por_localidade[localidade_arquivo_grupo2] = valores_nao_pares

# Escrever resultados no arquivo de saída
with open(arquivo_saida, 'w') as arquivo_saida:
    for localidade, valores_nao_pares in valores_nao_pares_por_localidade.items():
        arquivo_saida.write(f"Localidade: {localidade}\n")
        arquivo_saida.write("Valores que não têm par correspondente:\n")
        for valor in valores_nao_pares:
            arquivo_saida.write(f"{valor}\n")
            print(f"{valor}") # Imprimir no terminal o valor escrito no arquivo

print(f"Arquivo de saída '{arquivo_saida}' criado com sucesso.")