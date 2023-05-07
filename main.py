from trie import Trie
import argparse

parser = argparse.ArgumentParser(description='Process input file')
parser.add_argument('-c', '--arq-texto', help='the input file')
parser.add_argument('-x', '--arq-bin', help='the hexadecimal file')
parser.add_argument("-o", "--arq-saida", help="path to the output file")

args = parser.parse_args()

if args.arq_texto:
    with open(args.arq_texto, 'r') as f:
        data = f.read()
elif args.arq_bin:
    with open(args.arq_bin, 'rb') as f:
        data = f.read()
else:
    print("Especifique o arquivo de entrada com a flag -c ou -x")

def store_int(num, n_bytes):
    # Convert integer to bytes using the specified number of bytes
    
    # Write the bytes to a binary file
    a=    num.to_bytes(2, byteorder='big')
    with open('antes.bin', 'wb') as f:
        print("antes", a)
        f.write(a)
    byte_string = num.to_bytes(n_bytes, byteorder='big', signed=True)
    
    with open('depois.bin', 'wb') as f:
        print(byte_string)
        f.write(byte_string)
    
store_int(10, 1)

t = Trie()
raiz = t.get_raiz()
with open('entrada.txt', 'r') as file:
    maior_cadeia = ""
    while True:
        char = file.read(1)
        maior_cadeia += str(char) 
        n = t.buscar_por_cadeia(raiz, maior_cadeia)
        if (n == None):
            #print(maior_cadeia)
            indice, char = t.inserir(raiz, maior_cadeia)
            codigo = f'({indice},{char})'  # binary data
            print(codigo)
            with open(args.arq_saida, "wb") as f:
                for char in codigo:
                    binary_char = bin(ord(char))[2:].zfill(8)
                    f.write(binary_char.encode('utf-8'))
            maior_cadeia = ""
        if not char:
            break



import struct

int_size = struct.calcsize('i')
print(f"Size of integer: {int_size} bytes")
