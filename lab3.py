from xor import convert_to_binary, convert_binary_back 
from GCD import gcd
inputs = []
with open("lap_3_input.txt", "r") as f:
   inputs = f.read().split("\n")  

results = []
#ex1 
input_1 = inputs[0]
ascii_array = [ord(i) for i in input_1]
binary_array  = []
for i in ascii_array:
   binary_array += convert_to_binary(i, 8)
results.append(convert_binary_back(binary_array))
#ex2 
input_2 = int(inputs[1])
def convert_integer_to_string(inputs): 
   binary_array = convert_to_binary(inputs)
   binary_array.reverse()
   binary_lists = []
   for i in range(len(binary_array)//8):
      number_binary = binary_array[i*8:i*8+8]
      number_binary.reverse()
      binary_lists.append(number_binary)
      if (i == len(binary_array)//8 - 1):
         number_binary = binary_array[(i+1)*8:]
         number_binary.reverse()
         binary_lists.append(number_binary)

   a  = [convert_binary_back(i) for i in binary_lists]
   a.reverse()
   result = ""
   for i in a:
      result += chr(i)
   return result

results.append(convert_integer_to_string(input_2))
#ex3

def RSA_encryption(p, q, e, M):
   n = p * q
   phi = (p - 1) * (q - 1)
   if gcd(e, phi) != 1 and 1 < e and e < phi:
      return 
   d = pow(e, -1, phi)
   c = pow(M, e, n)
   return c

def RSA_decryption(p, q, e, C):
   n = p * q
   phi = (p - 1) * (q - 1)
   if gcd(e, phi) != 1 and 1 < e and e < phi:
      return 
   d = pow(e, -1, phi)
   m = pow(C, d, n)
   return m
input_3_1 = [int(i) for i in inputs[2].split(" ")]
input_3_2 = [int(i) for i in inputs[3].split(" ")]

c = RSA_encryption(input_3_1[0], input_3_1[1], input_3_1[2], input_3_1[3])
m = RSA_decryption(input_3_2[0], input_3_2[1], input_3_2[2], input_3_2[3])
results.append((c, m))

#ex4 

input_4 = [int(i) for i in inputs[4].split(" ")]

plain_text_integer = RSA_decryption(input_4[1], input_4[2], input_4[3], input_4[0])
results.append(convert_integer_to_string(plain_text_integer))

with open("LeAnhQuang_22BI13380.txt", 'w') as f:
    for i in range(len(results)):
        output = results[i]
        if i == 1:
            output = results[i]
        f.write(f"#{i + 1}: result is {output}")
        f.write('\n')
