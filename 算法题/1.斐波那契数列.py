'''
1 使用列表，生成一个斐波那契数列（20位），并打印出来。 [1,1,2,3,5,8,13,…..]
'''
def fib(n):
    '''输入n，返回前n位数列
    思路：递归
    '''
    a,b=0,1 #初始化数据
    fib=[]
    for i in range(n):
        c = a + b # 第三位等于前两位之和
        a = b #每次循环往后退一位
        b = c
        fib.append(c)
    return fib


if __name__ == '__main__':
    n=fib(20)
    print(n)