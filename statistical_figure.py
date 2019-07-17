from matplotlib import pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
labels = ['油脂类', '奶类和豆类', '鱼、禽、肉、蛋类', '蔬菜和水果类','谷类']
ratio = [0.013, 0.118, 0.158, 0.237,0.474]

plt.figure()
# 绘制扇形统计图
plt.subplot(2, 2, 1)
colors = ['y', 'w', 'dodgerblue', 'darkorange', 'lightskyblue']  #自定义颜色列表
plt.pie(ratio, labels=labels, autopct='%.1f%%', counterclock=False, startangle=-75, colors=colors)
plt.title('扇形统计图')
# 绘制条形统计图
plt.subplot(2, 2, 2)
plt.bar(labels, ratio, color='pink', edgecolor='black', width=0.4)
plt.grid(color='r', linestyle='-.', linewidth=1, alpha=0.3)
for x, y in zip(labels, ratio):
    plt.text(x, y, '%.2f%%'%(100*y), ha='center')
plt.title('条形统计图')
# 绘制折线统计图
plt.subplot(2, 2, 3)
plt.plot(labels, ratio, color='orange', marker='*')
for x, y in zip(labels, ratio):
    plt.text(x, y, '%.2f%%'%(100*y), ha='center',  va='bottom')
plt.title('折线统计图')
# 绘制散点图
plt.subplot(2, 2, 4)
plt.plot(labels, ratio, 'o', color='r')
for x, y in zip(labels, ratio):
    plt.text(x, y, '%.2f%%'%(100*y), ha='center',  va='bottom')
plt.title('散点图')

plt.show()
