from GCD import gcd
from xor import convert_to_binary

inputs = []

with open("lap_2_input.txt", "r") as f:
    inputs = f.read().split("\n")[:-1]
print(inputs)
inputs = [[int(i) for i in inputs[j].split(",")] for j in range(len(inputs))]
results = []

#ex1:
a, b = inputs[0]
results.append([gcd(a,b)])

#ex2
my_list = inputs[1]
result = []

for i in range(len(my_list)):
    for j in range(i, len(my_list)):
        if (gcd(my_list[i], my_list[j]) == 1):
            result.append([my_list[i], my_list[j]])

results.append(result)

#ex3
base, expo, mod = inputs[2]
bin_expo = convert_to_binary(expo)

r = base 
print(bin_expo)
for i in range(len(bin_expo) - 2, -1, -1):
    r = (r*r) % mod
    if bin_expo[i] == 1:
        r = (r * base) % mod
results.append([r])

with open("LeAnhQuang_22BI13380.txt", 'w') as f:
    for i in range(len(results)):
        output = results[i][0]
        if i == 1:
            output = results[i]
        f.write(f"#1: result is {output}")
        f.write('\n')

