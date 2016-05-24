# coding=utf-8
'''
Created on 2016年5月24日
@author: a1

数学分析 & 概率论
概述：
1. 什么是机器学习？
    随着任务的不断执行，经验的积累会带来计算机性能的提升。
    可以看做是人工智能的一个分支：根据提供的训练数据按照一定方式来学习，使得系统性能不断提升。
2. 思考人类学习：
    有监督学习：不同日期的月亮，最后我们认知这个圆圆亮亮的东西就是月亮。
    无监督学习：从已有的情况/数据中发现一些潜在存在的规律(聚类等)
    增强学习：走路、踢球，不断尝试中不断学习，有种说法是半监督学习。
3. 机器学习方法
    最近邻、SVM、决策树、随机森林、朴素贝叶斯、LDA
    要知道：方法是特别多的，需要认清楚各个方法之间的配合、优劣。
回忆知识：微积分
4. 微积分：两边夹定理（26页）
    sinx < x < tanx
    lim sinx/x = 1
    问题：对数函数log a x,a为多少时，在x=1处的斜率为1？  
        我们使用到两边夹定理，求得a=(1 + 1/n)^n  n-->正无穷,a越等于e
5. 极限存在定理：
    单调有界数列必有极限
    我们就用来计算(q + 1/n)^n，得到其>2 & <3.
6. 导数：
    一阶导数：曲线的斜率
    二阶导数：斜率变化快慢的反映，表现曲线的凸凹性。例如：加速度一定指向运动轨迹凹的一侧
    幂指函数求导：f(x) = x^x求其最小值；一般两边同时求导，找到斜率为0的点。
    ln N! --> N(ln N -1) (n --> 正无穷)
7. Taylor公式的应用（初衷是用多项式来近似表示函数在某点周围的情况）：
    sin x = x/1! - x^3/3! + x^5/5! - x^7/7! +...
    e^x = 1/0! + x/1! + x^2/2! + x^3/3! + ...
    在实践中，往往需要做一定程度的变换：
        如：思考计算机中e^x是如何计算的？
        我们将x = k*ln 2 + r, |r|<=0.5*ln2
            从而e^x = e^(k*ln2 + r) = 2^k*e^r
8. 方向导数：变化最快的方向即梯度方向
    如果函数z = f(x,y)在点P(x,y)是可微的，那么函数在该点沿任意方向L的
    方向导数都存在.（维数更多导数计算略有不同）
    应用：随机梯度下降法（问题：局部最优值）
概率论：
9. 累积分布函数：单增函数
    思考：将值域为[0,1]的某单增函数y = F(x)可以看成是X事件的累计概率函数；
        求导即为某概率密度。
10. 古典概型
    概率 = 发生事件/总事件
    生日悖论：50个同学中，至少有2个人生日相同的概率为多少？  97%，与现实貌似不符，悖论？
    换一个角度，如果你进入了一个有着22个人的房间，房间里的人中会和你有相同生日的概率便不是50：50了，而是变得非常低。原因是这时候只能产生22种不同的搭配。
    生日问题实际上是在问任何23个人中会有两人生日相同的概率是多少。
    · 这个在下面做了一个测试，随机生成1-365之间的50个数字，其中出现重复数字的概率很高！
11. 商品推荐：
    过于聚焦商品推荐其实会损害用户体验。
    解决方式：A/B两个商品匹配度分别为0.8,0.2，我们为A/B分别生成一个均匀分布于0-0.8/0-0.2之间的最终得分，
    之后将最终得分较高的推荐给用户。（相当于有一定的可能推荐一些新奇的东西）
12. 贝叶斯公式：
    条件概率：A事件在B事件发生的情况下，发生的概率。
    全概率公式：A事件发生的概率 = B1发生时A发生的概率 + B2发生时A发生的概率 + ...
    贝叶斯公式：事件A发生的情况下，事件Bi发生的概率

    从概念上理解贝叶斯：应用
        以前我们是：有两个箱子，分别有红白球，已知从A箱子拿，拿到白球的概率为？
        贝叶斯：已知拿到白球，从A箱拿的概率为多少？
13. 两种认识下的两个学派：
    频率学派：假设某个参数是某未知的定值，求这些参数如何取值，能够使得目标函数取极大、极小；
    贝叶斯学派：假定参数是服从某个分布的，求在这个分布约束下使得目标函数极大、极小。
    （贝叶斯学派的理论解释较好）
14. 贝叶斯公式应用：
    给定某系统若干样本，计算该系统的参数，
        P(a|x) = P(x|a)*P(a) / P(x)
    (对应贝叶斯网络部分内容)
分布：
15. 二项分布：对应logistic回归,分类用
    泊松分布：可以由e^x的泰勒展开式推导，两边同时除以e^x，之后通项公式即是泊松分布通项公式
    均匀分布
    指数分布
    正态分布：（高斯发现的，也叫高斯分布），对应线性回归，
16. 指数族

思考题：


'''
from numpy import *

if __name__ == '__main__':
    d = {}
    for i in range(23):
        t = int(random.uniform(1,365))
        if d.has_key(t)==False:
            d[t]=1
    print len(d)
    print d



