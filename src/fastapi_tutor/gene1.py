# 基本生成器的示例


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


for num in count_up_to(5):
    print(num)  # 输出 1 到 5

# 解释:
# 1. 定义生成器函数 count_up_to(max):
#    - 使用 yield 语句返回一个值, 并暂停函数状态。
#    - 每次调用生成器的 __next__() 方法时, 函数从上次暂停的地方继续执行, 直到遇到下一个 yield。
# 2. 使用 for 循环迭代生成器:
#    - for 循环会自动调用生成器的 __next__() 方法, 获取下一个值, 直到 StopIteration 异常。
# 3. 这样可以节省内存, 因为不需要一次性生成所有值, 而是按需生成。

# 详细执行流程:
# 1. 调用 count_up_to(5):
#    - 创建一个生成器对象, 并初始化状态。
# 2. 第一次迭代:
#    - 调用生成器的 __next__() 方法。
#    - 执行到 yield count, 返回 1, 暂停状态。
# 3. 第二次迭代:
#    - 继续执行, count 变为 2。
#    - 执行到 yield count, 返回 2, 暂停状态。
# 4. 重复上述过程, 直到 count 超过 max (5)。
# 5. 当 count 为 6 时, 不满足 while 条件, 函数结束, 抛出 StopIteration 异常, 迭代终止。
