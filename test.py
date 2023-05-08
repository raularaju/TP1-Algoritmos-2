import struct

s = "ç"
encoded = s.encode('utf-8')
print(encoded)
print(len(encoded))  # prints 5
print(encoded.decode())
n = 16
bits = n.bit_length()
print(bits)
""" 
x = 256  # an integer
c = 'a'   # a character

# Convert the integer to binary (4 bytes, little-endian)
x_bytes = x.to_bytes(2, byteorder= "big")

# Convert the character to binary (1 byte)
c_bytes = c.encode()

# Open the binary file in write mode and write the binary data to 
with open("output.bin", "wb") as file:
        for i in range(10):
            i_bytes = i.to_bytes(1, byteorder= "big")
            file.write(i_bytes)


with open("output.bin", "rb") as file:
    data = file.read()
    print(data)
    value = int.from_bytes(data, byteorder='big')  
    print(value) """