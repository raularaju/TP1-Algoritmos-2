def descomprimir_binario(nome_arq_bin, num_codigos, num_bytes_int):
    with open(nome_arq_bin, "rb") as f:
        for i in range(num_codigos):
            bytes_indice = f.read(num_bytes_int)
            indice = 0
            for j in range(num_bytes_int):
                indice |= bytes_indice[j] << (8 * j)
            print(indice)