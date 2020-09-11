'''
链表
'''
#定义链表
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

#实例化节点
n1= ListNode(4)
n2= ListNode(5)
n3= ListNode(1)
# 构建链接
n1.next(n2)
n2.next(n3)


'''
栈
'''
#栈的定义
stack=[]
#栈的操作
stack.append(1)
stack.append(2)
stack.pop()
stack.pop()


'''
队列
'''
#队列定义
from collections import  deque
queue = deque()
#队列操作
queue.append(1)
queue.append(2)
queue.popleft() 
queue.popleft()


'''
树
'''
#树定义
class TreeNode:
    def __init__(self, x):
        self.val = x      # 节点值
        self.left = None  # 左子节点
        self.right = None # 右子节点

#  树的建立
#        3
#      /    \
#    4        5
#  /    \
# 1      2
n1 = TreeNode(3) 
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(2)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5


'''
图：分为无向图和有向图
'''

'''
散列表：通过利用 Hash 函数将指定的「键 key」映射至对应的「值 value」
'''
# 初始化散列表
dic = {}

# 添加 key -> value 键值对
dic["小明"] = 10001
dic["小华"] = 10002
dic["小红"] = 10003

# 从姓名查找学号
dic["小明"] # -> 10001
dic["小华"] # -> 10002
dic["小红"] # -> 10003

names = [ "小明","小华","小红" ]
hash(id) {
    index = (id - 1) % 10000
    return index
}
names[hash(10001)] // 小明
names[hash(10002)] // 小华
names[hash(10003)] // 小红


'''
堆
'''
from heapq import heappush, heappop

# 初始化小顶堆
heap = []

# 元素入堆
heappush(heap, 1)
heappush(heap, 4)
heappush(heap, 2)
heappush(heap, 6)
heappush(heap, 8)

# 元素出堆（从小到大）
heappop(heap) # -> 1
heappop(heap) # -> 2
heappop(heap) # -> 4
heappop(heap) # -> 6
heappop(heap) # -> 8

