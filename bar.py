from matplotlib import pyplot as plt
plt.rc('font',family=['SimHei']) #用来显示中文 
plt.rc('font',size=6) #用来显示字体大小
plt.rc('axes',unicode_minus=False) #解决坐标显示负号的问题
plt.figure(figsize=(20,8))
# plt.xticks([0,1,2],["苹果","香蕉","葡萄"])
# plt.bar([0,1,2],[60,70,10])

plt.yticks([0,1,2],["苹果","香蕉","葡萄"])
plt.barh([0,1,2],[50,5,23],height=[0.5,1,0.6])


plt.show()