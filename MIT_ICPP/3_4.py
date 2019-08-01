epsilon = 0.0001
k = 2
guess = k/2.0
num = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2)-k)/(2*guess))
    num += 1
print('num=', num)
print(k, '的平方根为：', guess)
