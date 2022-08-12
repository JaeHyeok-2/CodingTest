A = int(input(), 2)
B = int(input(), 2)

mask = 2 ** 100000 - 1

and_op = bin(A & B)[2:].zfill(100000)
or_op = bin(A | B)[2:].zfill(100000)
ex_op = bin(A ^ B)[2:].zfill(100000)
not_a = bin(A ^ mask)[2:].zfill(100000)
not_b = bin(B ^ mask)[2:].zfill(100000)

print(f'{and_op}\n{or_op}\n{ex_op}\n{not_a}\n{not_b}')