# 闭包示例
def make_multipilier(n):
    def multipilier(x):
        return x * n

    return multipilier


double = make_multipilier(2)
print(double(5))  # 输出 10

# 解释: 为什么 double(5) 执行的是 multipilier(5) 而不是 make_multipilier(5)?
#
# 1. 在执行 double = make_multipilier(2) 时:
#    - 调用了外部函数 make_multipilier(2)。
#    - 外部函数返回了内部函数 `multipilier` 的函数对象本身。
#    - 变量 `double` 接收了这个返回值。此时, `double` 实际上就是 `multipilier` 函数的一个别名,
#      但它携带了闭包环境 (记住了 n=2)。
#
# 2. 在执行 double(5) 时:
#    - 既然 `double` 现在就是 `multipilier` 函数对象, 那么调用 `double(5)` 就完全等同于调用 `multipilier(5)`。
#    - make_multipilier 的任务在生成函数并返回时就已经结束了。
#
# 比喻:
# make_multipilier 是“机器制造工厂”, n=2 是配置参数。
# double = make_multipilier(2) 是工厂生产了一台特定的机器 (double)。
# double(5) 是你使用这台机器处理数据 5, 而不是重新去工厂。
