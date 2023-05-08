from trie import Trie
from compressor import comprimir_texto
from descompressor import descomprimir_binario
import argparse

OPCAO_COMPRESSAO = "compressao"
OPCAO_DESCOMPRESSAO = "deccompressao"

parser = argparse.ArgumentParser(description='Processa a linha de comando')
parser.add_argument('-c', '--arq-texto', help='Arquivo com o texto a ser comprimido')
parser.add_argument('-x', '--arq-bin', help='Arquivo a ser descomprimido')
parser.add_argument("-o", "--arq-saida", help="Arquivo de saida")


args = parser.parse_args()
opcao_escolhida = ""
nome_arq_texto = ""
nome_arq_bin = ""
nome_arq_saida= ""

if args.arq_texto:
    nome_arq_texto = args.arq_texto
    opcao_escolhida = OPCAO_COMPRESSAO
elif args.arq_bin:
    nome_arq_bin = args.arq_bin
    opcao_escolhida = OPCAO_DESCOMPRESSAO
else:
    print("Especifique o arquivo de entrada com a flag -c ou -x")


if args.arq_saida:
    nome_arq_saida = args.arq_saida
elif args.arq_texto:
    nome_arq_saida = nome_arq_texto + ".z78"
elif args.arq_bin:
    nome_arq_saida = nome_arq_bin + ".txt"




if(opcao_escolhida == OPCAO_COMPRESSAO):
    comprimir_texto(nome_arq_texto, nome_arq_saida)
elif(opcao_escolhida == OPCAO_DESCOMPRESSAO):
    descomprimir_binario(nome_arq_bin, 27, 1)

""" t = Trie()
raiz = t.get_raiz()
num_bytes_int = 0
codigos = []

with open(nome_arq_texto, 'r') as f:
    maior_cadeia = ""
    while True:
        char = f.read(1)
        maior_cadeia += str(char)
        n = t.buscar_por_cadeia(raiz, maior_cadeia)
        if (n == None):
            indice, char = t.inserir(raiz, maior_cadeia)
            codigos.append((indice, char))
            ind_min_bytes = min_bytes_necessarios(indice)
            if (ind_min_bytes > num_bytes_int):
                num_bytes_int = ind_min_bytes
            maior_cadeia = ""
        if not char:
            break
num_bytes_int = max(num_bytes_int, min_bytes_necessarios(len(codigos)))
print(codigos)
codigos_bin = []
while codigos:
    indice, char = codigos.pop(0)
    indice_bin = indice.to_bytes(num_bytes_int, byteorder= "big")
    codigos_bin.append(indice_bin)

escrever_binario(codigos_bin) """
