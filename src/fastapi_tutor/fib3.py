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
