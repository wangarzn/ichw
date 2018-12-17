#!/usr/bin/env python3


"""tile.py:puzhuan

__author__ = "Qichao Wang"

__pkuid__  = "1800011837"

__email__  = "1800011837@pku.edu.cn"

"""

def puzhuan(m,n,a,b,ans,ans0,qiang):
    """铺砖函数：找到所有的用已知尺寸的砖填满已知尺寸的墙的方案 
    list ans ：记录可以铺满墙的铺法
    list ans0 :在当前方案下，暂时记录铺好的砖
    list qiang ：记录墙上每块方块的状态 
    """
    count = 0
    p = 0
    for i in range(m * n):               #便历墙，为了找到没有铺砖的方格
        if qiang[i] == 0 and p == 0:   #找出下一块没铺的墙
            x = i // n + 1
            y = i % n + 1
            p = 1
            if (x + b - 1) <= m and (y + a - 1) <= n:#判断横着铺是否超界
                for j in range(x,x + b):
                    for k in range(y,y + a):
                        if qiang[(j - 1) * n + k - 1] == 0:
                            count = count + 1              #每找到一个没有铺的方格，就记录下来
            if count == a * b:                       #判断能否横着铺
                nlist =  []                          #nlist里放砖占据的方块的标号
                for j in range(x,x + b):
                    for k in range(y,y + a):
                        nlist.append((j - 1) * n + k - 1)
                        qiang[(j - 1) * n + k - 1] = 1
                ans0.append(nlist)                    #ans0为已经铺好砖的方格标号的列表
                if 0 not in qiang:
                    ans.append(ans0.copy())           #ans为铺墙方法
                else:
                    puzhuan(m,n,a,b,ans,ans0,qiang)   #继续寻找下一块砖，继续铺
                for j in range(x,x + b):              
                    for k in range(y,y + a):
                        qiang[(j - 1) * n + k - 1] = 0  #把砖拿下来
                del ans0[-1]                          #把刚放上去的砖拿下来，以便可以竖着铺
            count = 0
            if (x + a - 1) <= m and (y + b - 1) <= n:#在同一个点也可以竖着铺
                for j in range(x,x + a):
                    for k in range(y,y + b):
                        if qiang[(j - 1)*n + k - 1] == 0:
                            count = count + 1 
            if count == a * b:                          #判断可不可以铺下一块砖，并重复横着铺的过程
                nlist =  []
                for j in range(x,x + a):
                    for k in range(y,y + b):
                        nlist.append((j - 1) * n + k - 1)
                        qiang[(j - 1) * n + k - 1] = 1
                ans0.append(nlist)                    
                if 0 not in qiang:
                    ans.append(ans0.copy())   
                else:
                    puzhuan(m,n,a,b,ans,ans0,qiang)
                for j in range(x,x + a):
                    for k in range(y,y + b):
                        qiang[(j - 1) * n + k - 1] = 0
                del ans0[-1]
    return ans

def visualization(m,n,a,b,ans0):
    """可视化函数：将墙的状态，和铺墙函数的结果用turtle画出来
    """
    import turtle
    t = turtle.Turtle()
    t.speed(3)
    t.color('blue')                       #画出墙的状态
    t.pensize(1)
    t.penup()
    t.goto(-20*n,-20*m)
    t.pendown()
    for i in range(m):                   #画横线和数字
        for j in range(n):
            t.forward(20)
            t.write(i*n + j)
            t.forward(20)
        t.penup()
        t.goto(-20*n,-20*m + (i + 1)*40)
        t.pendown()
    t.forward(40*n)
    t.left(90)
    t.penup()
    for i in range(n+1):                    #画竖线
        t.goto(-20*n + 40*i,-20*m)
        t.pendown()
        t.forward(40*m)
        t.penup()
    t.pencolor('black')
    t.pensize(8)
    for i in ans0:#画砖
        if i[-1] - i[0] == a*b - 1:
            t.goto(-20*n + 40*(i[0]%n), -20*m + 40*(i[0]//n))
            t.pendown()
            t.forward(40*b)
            t.right(90)
            t.forward(40*a)
            t.right(90)
            t.forward(40*b)
            t.right(90)
            t.forward(40*a)
            t.right(90)
            t.penup()
        else:
            t.goto(-20*n + 40*(i[0]%n), -20*m + 40*(i[0]//n))
            t.pendown()
            t.forward(40*a)
            t.right(90)
            t.forward(40*b)
            t.right(90)
            t.forward(40*a)
            t.right(90)
            t.forward(40*b)
            t.right(90)
            t.penup()
    
    
def main():
    """输入墙和砖的长，宽
    判断能否用给定大小的砖铺满墙
    能铺满墙就运行 puzhuan函数，算出所有可能的铺法，并运行 visualization函数可视化（用户需输入想要可视化的结果）
    """
    m = int(input('墙的长是'))
    n = int(input('墙的宽是'))
    a = int(input('瓷砖的长是'))
    b = int(input('瓷砖的宽是'))
    qiang = [0]*m*n
    if m*n%(a*b) != 0:     #判断能否铺
        print("墙不能铺满")
        return 
    else:
        ans = []
        ans0 = []
        ans1 = []     #除重后的结果列表
        puzhuan(m,n,a,b,ans,ans0,qiang)
        for i in ans:          #排除重复结果
            if i not in ans1:
                ans1.append(i)
        print('共有{}种铺法'.format(len(ans1)))
        for i in range(len(ans1)):
            print('第{}种'.format(i+1),ans1[i])
            print('\n')
        shy = int(input('选择的方案1-{}：'.format(i + 2)))
        visualization(m,n,a,b,ans1[shy-1])
    
if __name__ == '__main__':
    main()
