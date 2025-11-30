# 类的基础示例


class Person:
    species = "Homo sapiens"  # 类属性, 共享属性
    count = 0  # 类属性, 记录实例数量

    def __init__(self, name: str, age: int):
        self.name = name  # 实例属性
        self.age = age  # 实例属性
        Person.count += 1  # 每创建一个实例, 计数加1

    # 实例方法
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # 类方法
    @classmethod
    def get_count(cls) -> int:
        return cls.count


# 实例化与验证
if __name__ == "__main__":
    # 1. 创建实例
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)

    # 2. 调用实例方法
    print(p1.greet())  # 输出: Hello, my name is Alice and I am 30 years old.
    print(p2.greet())  # 输出: Hello, my name is Bob and I am 25 years old.

    # 3. 访问类属性
    print(f"Species: {Person.species}")  # 输出: Species: Homo sapiens
    # 也可以通过实例访问类属性
    print(f"p1 Species: {p1.species}")

    # 4. 调用类方法 (验证计数器)
    print(f"Total Person count: {Person.get_count()}")  # 输出: Total Person count: 2

# 解释:
# 1. 类属性 (Class Attributes):
#    - `species` 和 `count` 是定义在类体中, 但在方法之外的变量。
#    - 它们属于类本身, 被所有实例共享。
#    - `Person.count` 在每次 `__init__` 时自增, 实现了全局计数功能。
#
# 2. 实例属性 (Instance Attributes):
#    - `self.name` 和 `self.age` 是定义在 `__init__` 中的变量。
#    - 它们属于具体的对象 (p1, p2), 每个对象的数据互不干扰。
#
# 3. 实例方法 (Instance Methods):
#    - `greet(self)` 第一个参数必须是 `self`, 指向调用该方法的实例对象。
#    - 它可以访问实例属性 (self.name)。
#
# 4. 类方法 (Class Methods):
#    - 使用 `@classmethod` 装饰器。
#    - 第一个参数必须是 `cls`, 指向类本身 (Person)。
#    - 它只能访问类属性 (cls.count), 不能访问实例属性。
