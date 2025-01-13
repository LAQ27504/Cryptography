k_pr = int(input("k pr: "))
k_pub = input("k public: ").split(" ")
p, a , b = k_pub
p = int(p)
a = int(a)
b = int(b)
x_b = int(input("x: "))
k_e = int(input("k e: "))

r = pow(a, k_e, p)
print(r)

s = ((x_b - k_pr * r) * pow(k_e, -1, (p - 1))) % (p - 1)
print(s)
b = pow (a,k_pr ,p)
print(b)
t = (pow(b,r,p) * pow(r, s,p)) % p

valid = pow(a, x_b, p)
print(t)
print(valid)
print(t == valid)

# mes = input("message: ").split(" ")
# x_1, r_1 , s_1 = mes
# x_1 = int(x_1)
# r_1 = int(r_1)
# s_1 = int(s_1)

# t_1 = pow(b, r_1) * pow(r_1, s_1) * p

# temp1 = pow(a, x_b, p)   
# temp2 = pow(a, x_1, p)
# print(t == temp1)
# print(t == temp2)
# print(t_1 == temp1)
# print(t_1 == temp2)