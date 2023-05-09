from trie import Trie
from compressor import comprimir_texto
from descompressor import descomprimir_binario
import argparse
""" 
OPCAO_COMPRESSAO = "compressao"
OPCAO_DESCOMPRESSAO = "descompressao"

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
    nome_arq_saida = nome_arq_bin + ".txt" """

nome_arq_texto = "entrada.txt"
nome_arq_bin = "bin.z78"
nome_arq_saida = "saida.txt"
dicionario = Trie()
""" if(opcao_escolhida == OPCAO_COMPRESSAO):
    dicionario = comprimir_texto(nome_arq_texto, nome_arq_saida)
elif(opcao_escolhida == OPCAO_DESCOMPRESSAO):
    descomprimir_binario(nome_arq_bin,nome_arq_saida,27, 1, dicionario) """

dicionario = comprimir_texto(nome_arq_texto, nome_arq_bin)
descomprimir_binario(nome_arq_bin,nome_arq_saida,27, 1)
