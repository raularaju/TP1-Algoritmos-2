# TP1-Algoritmos-2

Implementação do algoritmo LZ78 para compressão e descompressão de arquivos.

## Intruções para execução:
Tanto a compressão quanto a descompressão é dado através de linhas de comando:
- Compressão
	./main.py -c <arquivo_entrada> [-o <arquivo_saida>]

- Descompressão
	./main.py -x <arquivo_entrada> [-o <arquivo_saida>]

## Implementação
### Trie
Foi implementada uma trie tradicional para auxiliar nas consultas e inserções no dicionário. Nessa estrutura, cada nó tem dois atributos: um caracter e um índice (inteiro). O primeiro indica o último caracter da cadeia que o nó representa e o último revela o índice do outro nó que representa o resto daquela cadeia. Os métodos mais importantes são:
#### get_raiz()
    Retorna a raiz da Trie, sendo que a raiz é sempre inicializada com a string vazia e o índice 0
#### buscar_por_cadeia(inicio, cadeia)
    Busca um determinada cadeia na trie usando a partir do nó de partida. Se encontra a cadeia, retorna o nó que a representa. Caso contrário, retorna None.
#### buscar_por_indice(inicio, indice)
    Busca uma determinada cadeia na Trie usando DFS a partir de um índice. Se encontra a cadeia, retorna a cadeia. Caso contrário, retorna a string vazia.
#### inserir(inicio, cadeia)
    Insere uma cadeia na Trie. Se a cadeia não ja estiver na Trie retorna uma tupla: (índice do antecessor, ultimo_caractere). Se já existir, retorna: (índice do antecessor, <string_vazia>)  


### Compressão
O arquivo de entrada é lido caractere por caractere até o final.
A lista de códigos que começa vazia. 
A variável que guarda a maior cadeia inédita até o momento começa como a string vazia. 
Então o arquivo de entrada é lido caractere por caractere até que a maior string inédita ainda não foi inserida no dicionário, a string inédita  é inserida e a string inédita recebe a string vazia. 
Cada vez que uma cadeia é inserida no dicionário, adiona-se uma tupla em que o primeiro elemento é o indice para o elemento do dicionario que representa ps primeiros caracteres da cadeia e o segundo elemento é o último caractere da cadeia.
Depois da inserção de todos os caracteres, começa-se a escrever no arquivo binário. Primeiro se escreve o número de bytes usados para escrever um caractere e um índice, respectivamente. A partir daí escreve-se todos os códigos da lista criado na etapa anterior.

### Descompressão
Lê-se o número de bytes usados para representar um caractere e um inteiro do arquivo binário. Com essa informação, a leitura do arquivo é continuada e vai-se contruindo o dicionário a partir de uma Trie somente com o nó da raiz.Sendo assim, para cada tupla (indice, caracter) procura-se a cadeia na trie pelo indice e insere-se um novo elemento no dicionário que consiste nessa cadeia concatenada com o caractere da tupla. Esse processo se segue até que todo o arquivo seja lido.

## Taxa de compressão

| Arquivo              | Tamanho arquivo original | Tamanho arquivo comprimido| Taxa de compressão |
| -------------------- |:------------------------:| -------------------------:|:------------------:|
| 13th.txt             | 67,8 kB                  | 42,4 kB                   | 62,54%             |
| a.txt                | 1,3 MB                   | 35,2 kB                   | 2,27%              |
| aids.txt             | 55,9kB                   | 53,3 kB                   | 95,34%             |
| constituicao1988.txt | 651,8 kB                 | 436,3 kB                  | 66,94%             |
| consulthow.txt       | 37,0 kB                  | 26,3 kB                   | 71,08%             |
| crypto.txt           | 12,3 kB                  | 10,2 kB                   | 82,93%             |
| dom_casmurro.txt     | 409,6 kB                 |  292,5 kB                 | 71,42%             |
| lusiadas.txt         | 344,5 kB                 | 192,8 kB                  | 55,96%             |
| sla.txt              | 60,1 kB kB               | 17,5 kB                   | 29,15%             |
| terminator2.txt      | 297,5 kB                 | 142,8 kB                  | 48,00%             |
