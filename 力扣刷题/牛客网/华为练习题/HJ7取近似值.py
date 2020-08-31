"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""
def myround(a):
    if 10*a%10>=5:
        return int(a)+1
    else:
        return int(a)



if __name__ == '__main__':
    print(myround(0.8))