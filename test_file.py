a = 7
b = 6
for i in range(2021 - 2):
    a, b = b, int(str(a + b)[-1])

print(b)
