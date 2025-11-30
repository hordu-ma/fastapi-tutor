# 带参数的装饰器


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello!")


greet()  # 输出 "Hello!" 三次

# 解释:
# 这是一个"带参数的装饰器", 实际上是一个三层嵌套的函数结构。
#
# 1. repeat(times): 最外层函数 (装饰器工厂)。
#    - 它接收装饰器的参数 (times=3)。
#    - 它的任务是生成并返回一个真正的装饰器 (decorator)。
#
# 2. decorator(func): 中间层函数 (真正的装饰器)。
#    - 它接收目标函数 (greet)。
#    - 它的任务是生成并返回增强后的函数 (wrapper)。
#    - 它捕获了外层的 times 变量。
#
# 3. wrapper(*args, **kwargs): 最内层函数 (执行逻辑)。
#    - 它是最终被调用的函数。
#    - 它捕获了 func 和 times。
#    - 它实现了循环调用 func 的逻辑。
#
# 详细执行流程:
#
# 1. 工厂调用阶段:
#    - 解释器执行 `@repeat(3)` 中的 `repeat(3)`。
#    - `repeat` 函数运行, 记住 `times=3`, 返回 `decorator` 函数。
#
# 2. 装饰阶段:
#    - 解释器拿到返回的 `decorator`, 立即用它来装饰 `greet`。
#    - 相当于执行: `greet = decorator(greet)`。
#    - `decorator` 运行, 记住 `func=原始greet`, 返回 `wrapper`。
#    - `greet` 变量被重新赋值为 `wrapper`。
#
# 3. 调用阶段:
#    - 执行 `greet()` 时, 实际上是在运行 `wrapper()`。
#    - `wrapper` 使用闭包中的 `times=3` 和 `func=原始greet`, 循环打印 3 次 "Hello!"。
#
# 总结: @repeat(3) 等价于 greet = repeat(3)(greet)
