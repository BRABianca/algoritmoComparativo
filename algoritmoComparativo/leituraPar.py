import pandas as pd

def receber_entradas_grupo1():
    valores_grupo1 = []
    print("=== Grupo 1 ===")
    while True:
        entrada = input("Digite os valores do grupo 1 (pressione Enter para finalizar): ")
        if entrada == "":
            break
        valores_grupo1.extend(entrada.split())
    return valores_grupo1

def receber_entrada_grupo2():
    valores_grupo2 = []
    print("\n=== Grupo 2 ===")
    while True:
        entrada = input("Digite os valores do grupo 2 (pressione Enter para finalizar): ")
        if entrada == "":
            break
        valores_grupo2.extend(entrada.split())
    return valores_grupo2

def encontrar_valores_nao_pares(valores_grupo1, valores_grupo2):
    valores_nao_pares = []

    for valor in valores_grupo1:
        if valor not in valores_grupo2:
            valores_nao_pares.append(valor)

    for valor in valores_grupo2:
        if valor not in valores_grupo1 and valor not in valores_nao_pares:
            valores_nao_pares.append(valor)

    return valores_nao_pares

valores_grupo1 = receber_entradas_grupo1()
valores_grupo2 = receber_entrada_grupo2()

valores_nao_pares = encontrar_valores_nao_pares(valores_grupo1, valores_grupo2)

print("\nValores que não têm par correspondente:")
print(valores_nao_pares)
