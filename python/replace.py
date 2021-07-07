leg = []
line = 692
for i in range(0, line - 1):
    lcp = input()
    if lcp != '삭제':
        leg.append(lcp)

print('------------')

for i in range(0, line - 1):
    print(leg[int(i)])


print(leg)
