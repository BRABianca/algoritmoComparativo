# RDA & HANDLE Comparador

Este é um programa desenvolvido para comparar arquivos de duas pastas diferentes, identificar valores não pareados entre eles e gerar um arquivo de saída com os resultados da comparação.

## Funcionalidades

- **Seleção de Pastas:** Permite ao usuário selecionar duas pastas, uma contendo arquivos do tipo RDA e outra contendo arquivos do tipo HANDLE.
- **Comparação de Arquivos:** Compara os arquivos de ambas as pastas, identificando valores que não possuem correspondência entre elas.
- **Geração de Arquivo de Saída:** Cria um arquivo de saída contendo as localidades e os valores não pareados encontrados durante a comparação.

## Requisitos

- Python 3.x
- Bibliotecas Python: `tkinter`

## Instalação e Execução

1. Faça o download ou clone este repositório em sua máquina local.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Abra um terminal e navegue até o diretório raiz do projeto.
4. Execute o seguinte comando para instalar as dependências necessárias:

bash

Copy code

`pip install interfaceGrafica`

5. Após a instalação das dependências, execute o arquivo `interfaceGrafica.py` para iniciar a interface gráfica.
6. Na interface gráfica, selecione as pastas contendo os arquivos RDA e HANDLE.
7. Clique no botão "Enter" para iniciar a comparação.
8. O arquivo de saída será gerado na pasta de instalação do programa.

## Estrutura do Projeto

- `interfaceGrafica.py`: Contém a definição da interface gráfica e a lógica para interagir com o usuário.
- `scriptPrincipal.py`: Contém a lógica principal do programa, incluindo funções para ler arquivos, extrair localidades, comparar valores e gerar o arquivo de saída.
- `README.md`: Este arquivo, contendo informações sobre o projeto, requisitos, instalação e execução.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.
