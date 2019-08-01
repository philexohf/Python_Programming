total = 0
s = '1.23, 2.4, 3.123'
for c in s:
    for d in range(0, 10):
        if c == str(d):
            total += int(c)
print(total)
