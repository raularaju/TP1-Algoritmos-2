string = "Olá, mundo!" # includes non-ASCII characters

# Convert the string to a byte array using UTF-8 encoding
byte_array = string.encode("utf-8")

# Convert each byte to its binary representation and concatenate the results
#binary_string = ''.join(['{0:08b}'.format(byte) for byte in byte_array])

# Write the binary string to a file
with open("output.txt", "wb") as file:
    file.write(byte_array)