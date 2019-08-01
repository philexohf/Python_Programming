x = int(input('输入一个整数：'))
pwr = 1
counter = 0
while pwr < 6:
    root = 0
    while root**pwr < abs(x):
        root += 1    
    if root**pwr == abs(x):
        if x < 0:
            root = -root
            print('root=', root,'pwr=', pwr)
            counter += 1
        else:
            print('root=', root,'pwr=', pwr)
            counter += 1
    pwr += 1

if counter == 0:
    print('不存在这样的一对整数。')
