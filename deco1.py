# 装饰器 示例
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)
    return "Finished"


print(slow_function())  # 输出: slow_function took 2.000x seconds \n Finished

# 解释:
# 1. timer(func) 是一个装饰器(高阶函数), 它接收一个函数 func, 返回一个新的函数 wrapper。
# 2. wrapper(*args, **kwargs) 是增强后的函数, 它在执行 func 前后记录时间, 并打印耗时。
#    使用 *args, **kwargs 是为了能接收任意参数, 保证通用性。
# 3. @timer 是语法糖, 等同于执行了: slow_function = timer(slow_function)
#    - Python 解释器定义完 slow_function 后, 立即将其传入 timer。
#    - timer 返回 wrapper, 解释器将 wrapper 重新赋值给变量名 slow_function。
# 4. 因此, 最后调用 slow_function() 时, 实际上是在调用 wrapper()。
