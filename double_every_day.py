i = 1.0
j = 1.0

for k in range(2, 32):
    j *= 2
    i += j

print(i)
