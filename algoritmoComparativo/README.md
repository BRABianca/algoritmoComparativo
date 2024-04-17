# algoritmoComparativo
A ideia principal é: Um algoritmo de comparação, irá receber valores alfanuméricos em duas entradas (não poderá ter limite de valores para entrada, parará de ler quando eu der **enter** novamente) e retornará os valores que não tiverem par. 

O código procura códigos que não tenham seu par na outra pasta. Ele funciona da seguinte maneira:

**1. Leitura dos arquivos:**
- O código lê os arquivos de cada pasta, um por um.
- Para cada arquivo, ele extrai os códigos e os armazena em uma lista.

**2. Comparação dos códigos:**
- O código compara os códigos do grupo 1 com os códigos do grupo 2.
- Para cada código no grupo 1, ele verifica se existe um código correspondente no grupo 2.
- Se não existir um código correspondente, o código do grupo 1 é considerado um "valor não par".

**3. Gravação dos resultados:**
- O código grava os valores não pares em um arquivo de saída na pasta `saida`.
- O nome do arquivo de saída é formado pelo nome do arquivo original, com o sufixo `_saida`.

**Exemplo:**
- Se o código encontrar um código "1234" no grupo 1 e não encontrar um código "1234" no grupo 2, o código "1234" será gravado no arquivo de saída `saida_arquivo1.txt`.

**Observações:**
- O código considera que os códigos em cada arquivo são únicos.
- O código não verifica se os códigos são válidos.

# algoritmoSimplificado
1. Início
2. Defina uma função para ler os números de um arquivo dado o caminho do arquivo.
3. Defina uma função para extrair a localidade a partir do nome do arquivo.
4. Defina uma função para comparar duas localidades, ignorando maiúsculas e minúsculas e um número específico de caracteres no final.
5. Defina uma função para encontrar valores que não possuem pares correspondentes em dois conjuntos de valores.
6. Defina os diretórios das pastas contendo os arquivos do grupo 1 e do grupo 2.
7. Liste os arquivos nas pastas do grupo 1 e do grupo 2.
8. Defina o diretório para o arquivo de saída.
9. Se o diretório do arquivo de saída não existir, crie-o.
10. Crie um conjunto para armazenar os nomes dos arquivos já processados.
11. Crie um dicionário para armazenar os valores não pares por localidade.
12. Para cada arquivo no grupo 1:
    13. Leia os números do arquivo.
    14. Extraia a localidade do nome do arquivo.
    15. Encontre o arquivo correspondente no grupo 2.
    16. Se nenhum arquivo correspondente for encontrado, imprima uma mensagem e continue com o próximo arquivo.
    17. Leia os números do arquivo correspondente no grupo 2.
    18. Encontre os valores que não possuem pares correspondentes entre os dois grupos.
    19. Adicione os valores não pares ao dicionário, usando a localidade como chave.
13. Para cada arquivo no grupo 2 que não foi processado:
    20. Extraia a localidade do nome do arquivo.
    21. Encontre o arquivo correspondente no grupo 1.
    22. Se nenhum arquivo correspondente for encontrado, imprima uma mensagem e continue com o próximo arquivo.
    23. Leia os números do arquivo correspondente no grupo 1.
    24. Encontre os valores que não possuem pares correspondentes entre os dois grupos.
    25. Adicione os valores não pares ao dicionário, usando a localidade como chave.
14. Escreva os resultados no arquivo de saída.
15. Para cada localidade e seus valores não pares:
    26. Escreva a localidade no arquivo de saída.
    27. Escreva os valores não pares no arquivo de saída.
16. Fim


