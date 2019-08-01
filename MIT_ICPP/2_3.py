counter = 0
odd = 0

while counter < 10:
    x = int(input("请输入第{}个整数".format(counter+1)))
    if x%2 != 0 and (odd == 0 or x - odd > 0):
        odd = x
    counter += 1

if odd == 0:
    print("没有奇数.")
else:
    print("最大的奇数为：{}".format(odd))
