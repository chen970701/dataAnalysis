# pip freeze > .\requirement.txt
from matplotlib import pyplot as plt
plt.rc('font',family=['SimHei']) #用来显示中文 
plt.rc('font',size=6) #用来显示字体大小
plt.rc('axes',unicode_minus=False) #解决坐标显示负号的问题
x=range(2,26,2)
y=[15,14,13,12,16,17,18,18,20,17,13,11]
y2=[19,13,9,4,12,15,9,11,23,14,23,21]
flg=plt.figure(figsize=[4,3],dpi=180)
_x=range(0,24)
label=["{}点".format(i) for i in list(_x)]
plt.xticks(_x,labels=label,rotation=45)#设置x轴的刻度
# plt.savefig("./temp.png")#保存图片
plt.plot(x,y,label="7月1日",color="#ff0000",lineStyle="--",lineWidth=2,alpha=0.8)
plt.plot(x,y2,label="7月2日")
plt.xlabel("时间") #设置xlabel
plt.ylabel("气温")#设置ylabel
plt.title("一天的温度变化")
plt.grid(alpha=0.4)
plt.legend(loc="upper right")#绘制图例 设置显示位置吧
plt.show()