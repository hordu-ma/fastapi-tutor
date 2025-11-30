# 斐波那契数列


from functools import cache


@cache
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2) if n > 1 else n


def fib_iter(n: int) -> int:
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print(f"Recursive (cached): {fib1(10)}")  # 输出 55
    print(f"Iterative: {fib_iter(10)}")  # 输出 55


"""
时间复杂度优化说明:

1. 原始递归 (Naive Recursion):
   - 复杂度: O(2^n)
   - 原因: 存在大量重复计算。例如计算 fib(5) 时, fib(3) 会被计算两次, fib(2) 会被计算三次。随着 n 增大, 计算量呈指数级爆炸。

2. 缓存递归 (Cached Recursion) - @cache:
   - 复杂度: O(n)
   - 原因: 使用记忆化 (Memoization) 技术。装饰器会自动缓存已计算过的 fib(n) 结果。当再次需要 fib(n) 时, 直接查表返回, 避免了重复计算。每个 n 只计算一次。

3. 迭代法 (Iterative) - fib_iter:
   - 复杂度: O(n)
   - 原因: 使用循环自底向上计算。
   - 优势: 相比递归, 它不需要 O(n) 的栈空间, 空间复杂度仅为 O(1), 且没有递归深度限制 (RecursionError) 的风险。
"""
