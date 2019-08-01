x = int(input("请输入x的值："))
y = int(input("请输入y的值："))
z = int(input("请输入z的值："))

odd = None
if x%2 != 0:
    odd = x

if y%2 != 0:
    if y > x:
        odd = y

if z%2 != 0:
    if z > x or z > y:
        odd = z

if odd == None:
    print("没有奇数.")
else:
    print("最大的奇数为：{}".format(odd))
