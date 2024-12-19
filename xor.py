def xor_list(num_list):
    result = num_list[0]
    for i in range(1, len(num_list)):
        result ^= num_list[i]
    return result

def convert_to_binary(numbers, bits = False):
    binary = []
    while numbers > 0:
        binary.append(numbers % 2)
        numbers //= 2
    if (bits) and bits >= len(binary): 
        while len(binary) < bits :
            binary.append(0)
    binary.reverse()
    return binary
def convert_binary_back(binary):
   binary.reverse()
   result = 0
   for i in range(len(binary)):
      if binary[i] == 0:
         continue 
      result += pow(2,i)
   return result 
