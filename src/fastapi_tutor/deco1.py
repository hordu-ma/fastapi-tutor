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

# 详细执行流程解析:
#
# 1. 定义阶段 (Definition):
#    - 解释器读取 `def timer(func): ...`, 在内存中创建 timer 函数对象, 但暂不执行内部代码。
#
# 2. 装饰阶段 (Decoration) - 关键时刻:
#    - 当解释器读到 `@timer` 和 `def slow_function...` 时:
#      a. 先创建原始的 slow_function 函数对象 (包含 sleep 逻辑)。
#      b. 立即执行 `timer(原始_slow_function)`。
#      c. timer 内部定义 wrapper, 并将原始函数保存在闭包中。
#      d. timer 返回 wrapper。
#      e. 解释器将 wrapper 重新赋值给变量名 `slow_function`。
#    - 此时, timer 函数执行完毕并退场。
#
# 3. 调用阶段 (Execution):
#    - 执行 `print(slow_function())` 时, 实际上是在运行 `wrapper()`。
#    - wrapper 记录开始时间 -> 调用原始函数 -> 记录结束时间 -> 打印耗时 -> 返回结果。
