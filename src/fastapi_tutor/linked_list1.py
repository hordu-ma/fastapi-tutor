class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """单向链表实现"""

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val: int) -> None:
        """在链表末尾添加节点"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, val: int) -> None:
        """在链表头部添加节点"""
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def insert(self, index: int, val: int) -> None:
        """在指定位置插入元素"""
        if index == 0:
            self.prepend(val)
            return

        if index >= self.size:
            self.append(val)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node = ListNode(val, current.next)
        current.next = new_node
        self.size += 1

    def remove(self, index: int) -> None:
        """删除第一个匹配的元素"""
        if not self.head:
            return False

        if self.head.index == index:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next and current.next.index != index:
            current = current.next

        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True

        return False

    def find(self, val: int) -> int:
        """查找元素并返回索引, 未找到返回 -1"""
        current = self.head
        index = 0
        while current:
            if current.val == val:
                return index
            current = current.next
            index += 1
        return -1

    def to_list(self) -> list:
        """将链表转换为 Python 列表"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result


# 代码详解:
# 1. ListNode 类:
#    - 定义了链表的节点结构, 包含节点值 val 和指向下一个节点的指针 next。
# 2. LinkedList 类:
#    - 管理链表的整体结构, 包含头节点 head 和链表大小 size。
# 3. append(val):
#    - 在链表末尾添加新节点。如果链表为空, 则新节点成为头节点。
# 4. prepend(val):
#    - 在链表头部添加新节点, 并更新头节点指针。
# 5. insert(index, val):
#    - 在指定索引位置插入新节点。处理边界情况 (头部和尾部)。
# 6. remove(index):
#    - 删除指定索引位置的节点, 并更新链表结构。
# 7. find(val):
#    - 查找节点值并返回其索引, 未找到返回 -1。
# 8. to_list():
#    - 将链表转换为 Python 列表, 方便查看和验证链表内容。
