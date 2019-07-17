from matplotlib import pyplot as plt


city = input('请输入您要查询的城市：')
hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
temp_hefei = [23, 24, 23, 23, 22, 23, 23, 22, 25, 26, 27, 28, 29, 30, 31, 31, 32, 32, 31, 31, 30, 29, 27,26]
temp_luan = [25, 24, 23, 24, 23, 23, 24, 26, 27, 28, 30, 31, 31, 32, 32, 32, 32, 31, 31, 30, 29, 25, 26, 26]
temp_xian = [28, 26, 25, 23, 23, 22, 25, 24, 25, 26, 29, 30, 31, 32, 34, 32, 32, 31, 30, 29, 28, 28, 27, 26]

if city == '合肥':
    sum_temp = 0
    for  a in temp_hefei:
        sum_temp += a
    avg_temp = sum_temp / len(temp_hefei)
    AVG_TEMP = [avg_temp]*len(temp_hefei)

    plt.plot(hour, temp_hefei)
    plt.plot(hour, AVG_TEMP)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title('合肥24小时气温')

elif city == '六安':
    sum_temp = 0
    for  a in temp_luan:
        sum_temp += a
    avg_temp = sum_temp / len(temp_luan)
    AVG_TEMP = [avg_temp]*len(temp_luan)

    plt.plot(hour, temp_luan)
    plt.plot(hour, AVG_TEMP)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title('六安24小时气温')

elif city == '西安':
    sum_temp = 0
    for  a in temp_xian:
        sum_temp += a
    avg_temp = sum_temp / len(temp_xian)
    AVG_TEMP = [avg_temp]*len(temp_xian)

    plt.plot(hour, temp_luan)
    plt.plot(hour, AVG_TEMP)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title('西安24小时气温')
else:
    print("未查询到您输入的城市！")

plt.show()
