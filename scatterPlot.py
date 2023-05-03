# pip freeze > .\requirement.txt
#散点图
import random
from matplotlib import pyplot as plt
plt.rc('font',family=['SimHei']) #用来显示中文 
plt.rc('font',size=6) #用来显示字体大小
plt.rc('axes',unicode_minus=False) #解决坐标显示负号的问题
y1=[20+random.randint(0,20) for i in range(30)]
y2=[30-random.randint(0,20) for i in range(30)]
flg=plt.figure(figsize=[4,3],dpi=180)
_x1=range(1,len(y1)+1)
_x2=range(51,51+len(y2))
_x=list(_x1)+list(_x2)
_label=["{}号".format(i) for i in _x1]+["{}号".format(i-50) for i in _x2]
plt.xticks(_x[::3],labels=_label[::3],rotation=45)#设置x轴的刻度 ::3是用来缩小显示比例
# plt.savefig("./temp.png")#保存图片
plt.scatter(_x1,y1,label="7月",color="#ff0000",alpha=0.8,s=10)#s是点的大小
plt.scatter(_x2,y2,label="10月")
plt.xlabel("时间") #设置xlabel
plt.ylabel("最高气温")#设置ylabel
plt.title("7月10月最高气温变化图")
plt.grid(alpha=0.4)
plt.legend(loc="upper right")#绘制图例 设置显示位置吧
plt.show()