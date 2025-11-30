# Python 作用域与 global/nonlocal 区别演示

# 1. 全局作用域 (Global)
x = 100  # 这是一个全局变量


def outer():
    # 2. 嵌套作用域 (Enclosing)
    x = 200  # 这是 outer 函数的局部变量, 对于 inner 来说是嵌套作用域变量

    def inner_local():
        # 情况 A: 既没有 global 也没有 nonlocal
        # Python 认为这是一个新的局部变量, 与外面的 x 无关
        x = 300
        print(f"[inner_local]    x = {x} (创建了新的局部变量)")

    def inner_nonlocal():
        # 情况 B: 使用 nonlocal
        # 声明这里的 x 指向的是 outer 函数里的那个 x (200)
        nonlocal x
        x = 400  # 修改的是 outer 的 x
        print(f"[inner_nonlocal] x = {x} (修改了 outer 的变量)")

    def inner_global():
        # 情况 C: 使用 global
        # 声明这里的 x 指向的是模块最顶层的那个 x (100)
        global x
        x = 500  # 修改的是全局的 x
        print(f"[inner_global]   x = {x} (修改了 全局 的变量)")

    print(f"--- 进入 outer 函数, 初始 x = {x} ---")

    inner_local()
    print(f"调用 inner_local 后, outer 的 x = {x} (未变)")

    inner_nonlocal()
    print(f"调用 inner_nonlocal 后, outer 的 x = {x} (变了!)")

    inner_global()
    print(f"调用 inner_global 后, outer 的 x = {x} (未变, 因为改的是全局的)")


print(f"1. 初始全局 x = {x}")
outer()
print(f"2. 执行 outer 后, 全局 x = {x} (被 inner_global 改了!)")
