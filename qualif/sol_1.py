def out_string(case, a, b):
    return "Case #" + str(case) + ': ' + str(a) + ' ' + str(b)


t = int(input())
n_i = [input() for _ in range(t)]

n_o = []

for n in n_i:
    b = ['0']*len(n)
    a = list(n)
    for pos, c in enumerate(n):
        if c == '4':
            a[pos] = '3'
            b[pos] = '1'
    n_o.append((int(''.join(a)), int(''.join(b))))


for i, (a, b) in enumerate(n_o):
    print(out_string(i, a, b))
