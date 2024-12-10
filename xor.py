def xor_list(num_list):
    result = num_list[0]
    for i in range(1, len(num_list)):
        result ^= num_list[i]
    return result

def convert_to_binary(numbers):
    binary = []
    while numbers > 0:
        binary.append(numbers % 2)
        numbers //= 2
    binary.reverse()
    return binary
