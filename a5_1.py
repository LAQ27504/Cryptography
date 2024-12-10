from xor import convert_to_binary, xor_list

def major(number_list : list):
    if (number_list.count(0) >= number_list.count(1)):
        return 0
    return 1

x = int(input("Enter the number X: "))
y = int(input("Enter the number Y: "))
z = int(input("Enter the number Z: "))
len_key = int(input("Enter the lenght keystream: "))

bin_x = convert_to_binary(x)
print(f"The number X after convert to binary: {bin_x}") 
bin_y = convert_to_binary(y)
print(f"The number Y after convert to binary: {bin_y}")
bin_z = convert_to_binary(z)
print(f"The number Z after convert to binary: {bin_z}")

keystream = []

for i in range(len_key):
    move_list = [True, True, True]

    s = xor_list([bin_x[len(bin_x) - 1], bin_y[len(bin_y) - 1], bin_z[len(bin_z) - 1]])

    m = major([bin_x[8], bin_y[10], bin_z[10]])

    if (bin_x[8] != m) : move_list[0] = False
    if (bin_y[10] != m) : move_list[1] = False
    if (bin_z[10] != m) : move_list[2] = False

    if (move_list[0]):
        new_x = xor_list([bin_x[13],bin_x[16],bin_x[17],bin_x[18]])
        bin_x.pop()
        bin_x.reverse()
        bin_x.append(new_x)
        bin_x.reverse()
    if (move_list[1]):
        new_y = xor_list([bin_y[20],bin_y[21]])
        bin_y.pop()
        bin_y.reverse()
        bin_y.append(new_y)
        bin_y.reverse()
    if (move_list[2]):
        new_z = xor_list([bin_z[7],bin_z[20],bin_z[21],bin_z[22]])
        bin_z.pop()
        bin_z.reverse()
        bin_z.append(new_z)
        bin_z.reverse()
    keystream.append(s)
    print(f"The number after the {i} iteration: ")
    print(bin_x)
    print(bin_y)
    print(bin_z)

keystream.reverse()
print(keystream)
