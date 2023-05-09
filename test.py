char = '🙂'
encoding = 'utf-8'
char_size  = len(format(ord(char), '08b'))
char_size = char_size + 7
char_size -= (char_size % 8)
byte_count = len(char.encode(encoding)) * 8
print(char_size)
print(byte_count)
""" data = [('ç', 123), ('a', 456), ('é', 789)]

with open('binary_file.bin', 'wb') as file:
    for item in data:
        char_byte = item[0].encode('utf-8')
        int_byte = item[1].to_bytes((item[1].bit_length() + 7) // 8, 'little')
        file.write(char_byte + int_byte)

with open('binary_file.bin', 'rb') as file:
    while True:
        char_byte = file.read(1)
        if not char_byte:
            break
        char_ord = char_byte[0]
        if char_ord & 0b10000000 == 0:
            char = chr(char_ord)
        else:
            char_bytes = [char_ord]
            char_byte_count = bin(char_ord)[2:].index('0') - 1
            for i in range(char_byte_count):
                char_bytes.append(file.read(1)[0])
            char = bytes(char_bytes).decode('utf-8')
        int_byte_count = (123).bit_length() // 8 + 1
        int_byte = file.read(int_byte_count)
        integer = int.from_bytes(int_byte, byteorder='little')
        print(char, integer)

 """