class DynamicArray:
    """动态数组实现"""

    def __init__(self, capacity: int = 8):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]

    def append(self, value) -> None:
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index: int, item) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def remove(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")

        item = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._size -= 1
        return item

    def _resize(self, new_capacity: int) -> None:
        old_data = self._data
        self._data = [None] * new_capacity
        for i in range(self._size):
            self._data[i] = old_data[i]
        self._capacity = new_capacity


# 代码详解:
#
# 1. 类定义与初始化 (__init__):
#    - `DynamicArray` 模拟了 Python 列表或 Java ArrayList 的底层实现。
#    - `_capacity`: 数组当前的物理容量 (能存多少个元素)。
#    - `_size`: 数组当前的逻辑大小 (实际存了多少个元素)。
#    - `_data`: 实际存储数据的底层列表, 初始化为固定大小的 `[None] * capacity`。
#
# 2. 魔法方法 (__len__, __getitem__):
#    - `__len__`: 允许使用 `len(arr)` 获取数组实际元素个数。
#    - `__getitem__`: 允许使用 `arr[i]` 索引访问元素。包含边界检查, 防止越界。
#
# 3. 添加元素 (append):
#    - 向数组末尾添加元素。
#    - **关键逻辑**: 如果当前容量已满 (`_size == _capacity`), 触发 `_resize` 进行扩容 (通常是翻倍)。
#    - 这是一个均摊 O(1) 的操作。
#
# 4. 插入元素 (insert):
#    - 在指定索引 `index` 处插入元素。
#    - 同样会检查是否需要扩容。
#    - **数据搬移**: 从 `index` 开始的所有后续元素都需要向后移动一位 (`self._data[i] = self._data[i - 1]`), 为新元素腾出空间。
#    - 这是一个 O(n) 的操作。
#
# 5. 删除元素 (remove):
#    - 删除指定索引 `index` 处的元素。
#    - **数据搬移**: 从 `index` 后的所有元素向前移动一位 (`self._data[i] = self._data[i + 1]`), 覆盖掉被删除的元素。
#    - 这是一个 O(n) 的操作。
#
# 6. 扩容机制 (_resize):
#    - 当数组满了, 创建一个新的、更大的数组 (通常是旧数组的 2 倍)。
#    - 将旧数组的所有元素复制到新数组中。
#    - 更新 `_data` 指向新数组, 并更新 `_capacity`。
#    - 这是动态数组能够"动态"增长的核心。
