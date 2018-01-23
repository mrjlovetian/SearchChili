# coding=utf-8


def aTryCatch():
    a = 10
    b = 0
    m = 0
    try:
        m = (a / b)
        print('a/b = %f' % m)
    except:
        print("发生异常")
    finally:
        print("最后处理")



aTryCatch()