from xor import convert_to_binary, convert_binary_back 
inputs = []
with open("lap_3_input.txt", "r") as f:
   inputs = f.read().split("\n")  

#ex1 
input_1 = inputs[0]
ascii_array = [ord(i) for i in input_1]
print(ascii_array)
binary_array  = []
for i in ascii_array:
   print(convert_to_binary(i, 8))
   binary_array += convert_to_binary(i, 8)
print(convert_binary_back(binary_array))
#ex2 
input_2 = int(inputs[1])
binary_array = convert_to_binary(input_2)
print(binary_array )
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
print(binary_lists)
a  = [convert_binary_back(i) for i in binary_lists]
a.reverse()
print([chr(i) for i in a])

#ex3

