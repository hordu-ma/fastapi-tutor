#!/usr/bin/env -S uv run python3
"""
演示 shebang 的使用和调试断点
- 使用 uv run 确保在虚拟环境中运行
- 无需手动激活虚拟环境
"""


def calculate_sum(a: int, b: int) -> int:
    """计算两数之和（在这行打断点观察参数）"""
    result = a + b  # 在这行打断点，查看 a, b, result 的值
    return result


def main() -> None:
    """主函数"""
    numbers = [1, 2, 3, 4, 5]
    total = 0

    # 在这行打断点，观察 numbers 列表
    for num in numbers:
        total += num  # 在这行打断点，观察循环中的 num 和 total 变化

    # 调用函数（在这行打断点，观察函数调用）
    result = calculate_sum(10, 20)

    print(f"列表总和: {total}")
    print(f"calculate_sum(10, 20) = {result}")
    print(f"Python 解释器路径: {__file__}")


if __name__ == "__main__":
    main()
