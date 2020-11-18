##最小二乘法
import numpy as np   ##科学计算库 
import scipy as sp   ##在numpy基础上实现的部分算法库
import matplotlib.pyplot as plt  ##绘图库
from scipy.optimize import leastsq  ##引入最小二乘法算法

'''
    设定拟合函数和偏差函数
    函数的形状确定过程：
    1.先画样本图像
    2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
'''

##需要拟合的函数func :指定函数的形状
def func(p,x):
    k,b=p
    return k*x+b

##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
def error(p,x,y):
    return func(p,x)-y

def main():
    '''
    设置样本数据，真实数据需要在这里处理
    '''
    # 样本数据(Xi,Yi)，需要转换成数组(列表)形式
    Xi=np.arange(30,70,5)
    Yi=np.array([56.55,57.50,58.53,59.60,60.65,61.73,62.74,63.87])

    # p0表示k,b的初始值，可以任意设定,发现p0的值会影响cost的值：Para[1]
    # leastsq是scipy提供的最小二乘函数
    # leastsq函数的返回值是一个tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
    # 求解结果也是一个tuple，元素数量和args参数数量一致。
    p0=[1,20]
    Para=leastsq(error,p0,args=(Xi,Yi))

    #求解结果
    k,b=Para[0]
    print("cost："+str(Para[1]))
    print("求解的拟合直线为:")
    print("y="+str(round(k,2))+"x+"+str(round(b,2)))

    #画散点图，样本点
    plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
    plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2) 

    #画拟合直线
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    x=np.linspace(30,70,100) ##返回30-70之间100个均匀点
    y=k*x+b ##函数式，我们得到一个对应于x的y的列表
    plt.plot(x,y,color="red",label="拟合直线",linewidth=2) 
    plt.xlabel('温度/摄氏度')   #x轴名称
    plt.ylabel('电阻/欧姆')
    plt.title("铜电阻的温度特性曲线")
    plt.xticks(np.arange(30,71,5),["{:.2f}".format(i) for i in np.arange(30,71,5)])     #x刻度绘制
    plt.yticks(np.arange(55,66,1),["{:.1f}".format(i) for i in np.arange(55,66,1)])
    plt.legend(loc='lower right') #绘制图例
    plt.show()

if __name__ == "__main__":
    main()