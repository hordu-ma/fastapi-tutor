# 使用结果缓存(memoization)来优化斐波那契数列的计算

memo: dict[int, int] = {0: 0, 1: 1}  # 预先存储已知的斐波那契数值


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # 递归计算并缓存结果
    return memo[n]


if __name__ == "__main__":
    print(f"Recursive (memoized): {fib3(5)}")  # 输出 5
    print(f"Recursive (memoized): {fib3(10)}")  # 输出 55
    print(f"Recursive (memoized): {fib3(50)}")  # 输出 12586269025


"""
复杂度分析与对比:

1. fib3 (手工记忆化):
   - 时间复杂度: O(n) - 每个数值只计算一次, 之后从 memo 字典查表
   - 空间复杂度: O(n) - memo 字典存储 n 个键值对
   - 优势: 代码清晰直观, 展示记忆化工作原理
   - 劣势: 全局变量污染, memo 持久存储在内存中

2. @cache 装饰器 (相比 fib3):
   - 复杂度: 同为 O(n) 时间, O(n) 空间
   - 优势: 代码更简洁, 自动化缓存管理 (推荐使用)
   - 劣势: 同样消耗 O(n) 空间

3. fib_iter (迭代法):
   - 时间复杂度: O(n) - 循环执行 n-1 次
   - 空间复杂度: O(1) - 仅需两个变量 a, b
   - 优势: 空间效率最高, 无递归深度限制风险
   - 劣势: 每次调用都需重新计算

最佳实践:
- 频繁调用 -> 使用 @cache 装饰器 (简洁, Pythonic)
- 内存敏感 -> 使用 fib_iter 迭代法 (O(1) 空间)
- 教学示例 -> fib3 手工记忆化 (理解原理)
"""
