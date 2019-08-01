x = float(input('请输入一个数:'))
epsilon = 0.01
num = 0
if x >= 0.0:
    low = 0.0
    high = max(1.0, x)
else:
    low = min(-1.0, x)
    high = 0.0
ans = (high + low) / 2.0
while abs(ans**3 - x) >= epsilon:
    print('low=', low, 'high=', high, 'ans=', ans)
    num += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num=', num)
print(x,'的立方根是：', ans)
