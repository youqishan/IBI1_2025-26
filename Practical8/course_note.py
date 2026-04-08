# def is_even(i):
#     '''
#     判断一个整数是否为偶数
#     '''
#     print(f"Checking if {i} is even...")
#     return i % 2 == 0  # 这一步其实导致结果返回为 True 或者 False！

# is_even(10)  # 这一步调用了函数 is_even()，但是没有把结果显示在屏幕上！
# print(is_even(10))  # 这一步才会把结果显示在屏幕上！

# # 或者
# result = is_even(10)  # 这一步调用了函数 is_even()
# print(f"10 是偶数吗？ {result}")  # 这一步才会把结果显示在屏幕上！

'''
return：只负责把结果「交出去」，不会自动显示在屏幕上；
    并且，return 只能在函数内部用，之后的代码都不会被执行了。
    其作用是返回一个值，或者说把一个值「交出去」，让函数的调用者能得到这个值。
print()：专门负责把内容「打印显示在终端」，让你能看见。
    print 在函数内部和外部都可以用，函数内部的 print 只负责把内容显示在屏幕上，
'''

# def f(x):
#     x = x + 1
#     print(' in f(x): x =', x)
#     return x
#     # 函数内部的 x 和函数外部的 x 是两个不同的变量，函数内部的 x 是局部变量，函数外部的 x 是全局变量
#     # 修改函数内部的 x 不会影响函数外部的 x，因为它们是两个不同的变量
# x = 3
# z = f(x)

# print(x, z)

''''''

# def f(y):
#     x = 1       # 这里是在函数内部，新建了一个「局部变量x」，和外面的x完全无关！
#     x += 1      # 局部x从1变成2
#     print(x)    # 打印局部x → 输出 2

# x = 5           # 全局变量x = 5
# f(x)            # 调用函数f
# print(x)        # 打印全局x → 输出 5（完全没被函数影响！）

''''''

# def g(y):
#     print(x)    # 函数内没给x赋值，Python去全局找x → 输出 5
#     print(x+1)  # 同样用全局x → 输出 6

# x = 5           # 全局变量x = 5
# g(x)            # 调用函数g
# print(x)        # 全局x没被修改 → 输出 5

''''''

# def h(y):
#     x += 1      # 这里是「修改操作」，Python默认把x当成局部变量，但局部x没被定义！

# x = 5           # 全局变量x = 5
# h(x)            # 调用函数h → 直接报错！
# print(x)        # 这一步根本不会执行，因为函数h()里已经报错了！
# # 除非在 h(y) 内先定义 x = 1，否则就会报错，
# # 因为 Python 认为 x 是一个局部变量，但它在使用前没有被定义

''''''

# def h(y):
#     global x    # 强制声明x是全局变量，但是强烈不推荐！
#     x += 1      # 现在可以修改全局x了

# x = 5
# h(x)
# print(x)  # 输出 6（全局x被修改了）

'''
创建类实例时，__init__()方法会被自动调用来初始化实例的属性。
在__init__()方法中，self参数代表正在创建的实例本身，可以通过self来访问和设置实例的属性。
当你创建一个类的实例时，Python会自动调用__init__()方法来初始化实例的属性。
注意双下划线（__）是Python中的特殊方法的命名约定，表示这是一个特殊方法，不应该直接调用，而是由Python解释器在特定情况下自动调用。
'''

'''
格式如下：
class 类名(父类):  # 父类默认是object（Python基础对象）
    def __init__(self, 属性1, 属性2, ...):
        """构造函数：创建实例时初始化属性"""
        self.属性1 = 属性1  # 给实例绑定属性
        self.属性2 = 属性2
    
    def 方法名1(self, 参数1, ...):
        """方法1：实例的功能"""
        # 方法逻辑，可通过self访问实例属性
        逻辑处理...
        return 返回值
    
    def 方法名2(self, 参数2, ...):
        """方法2：另一个功能"""
        逻辑处理...
'''

# class Coordinate:
#     def __init__(self, x, y):
#         self.x = x  # 将参数x赋值给实例属性self.x
#         self.y = y  # 将参数y赋值给实例属性self.y

# # 第1页：使用类，创建实例（具体的坐标点）
# p1 = Coordinate(3, 4)  # 创建第一个坐标点(3,4)
# p2 = Coordinate(-1, 2) # 创建第二个坐标点(-1,2)

# # 操作实例（访问实例的属性）
# print("p1的坐标：", p1.x, p1.y)  # 输出：p1的坐标： 3 4
# print("p2的坐标：", p2.x, p2.y)  # 输出：p2的坐标： -1 2

'''
在上面的代码中，我们定义了一个Coordinate类，包含一个__init__方法来初始化实例的属性x和y。
然后，我们创建了两个Coordinate类的实例p1和p2，
分别代表坐标点(3,4)和(-1,2)。最后，我们通过访问实例的属性来打印出它们的坐标。
'''

# # 1. 定义坐标类（模板）
# class Coordinate(object):
#     def __init__(self, x, y):
#         # 初始化x、y轴属性
#         self.x = x  # x, y是临时局部变量，self.x, self.y是实例属性
#         self.y = y
    
#     def distance(self, other):  # other是另一个Coordinate实例，用来接收 c2 传入的坐标对象
#         """计算当前坐标和另一个坐标（other）的距离"""
#         x_diff_sq = (self.x - other.x) ** 2  # self.x是当前实例的x
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq + y_diff_sq) ** 0.5  # 勾股定理计算距离

# # 2. 实例化对象（按模板造两个坐标）
# c1 = Coordinate(3, 4)  # 第一个坐标：x=3，y=4
# c2 = Coordinate(0, 0)  # 第二个坐标：x=0，y=0
# c3 = Coordinate(-12, 5) # 第三个坐标：x=-12，y=5

# # 3. 调用方法（计算两个坐标的距离）
# dist = c1.distance(c2)  # 这里调用了c1的distance方法，传入c2作为参数，计算c1和c2之间的距离
# print(dist)  # 输出：5.0（3-0、4-0的距离是5）

# dist2 = c2.distance(c3)  # 计算c2和c3之间的距离
# print(dist2)  # 输出：13.0（0-(-12)、0-5的距离是√169）

'''
复用父类的功能：
'''

# # 父类（超级类）：动物
# class Animal:
#     def __init__(self, name):
#         self.name = name  # 父类的属性：名字
    
#     def speak(self):
#         # 父类的方法：发出声音（通用版）
#         print(f"{self.name} 发出了声音")

# # 子类（派生类）：狗，继承自动物类
# class Dog(Animal):
#     def speak(self):
#         # 重写父类方法：把“发出声音”改成“汪汪叫”
#         print(f"{self.name} 说：Woof!")

# # 使用子类
# my_dog = Dog("Buddy")  # 实例化狗对象，名字Buddy
# my_dog.speak()  # 输出：Buddy 说：Woof!（调用重写后的方法）
# print(my_dog.name)  # 输出：Buddy（继承父类的name属性）

''''''

# 第二课时

'''
复杂度 O 与 排序算法
复杂度不关心具体运行秒数，只看「数据量n无限变大时，操作次数的增长趋势」
'''

''' 仅查找第一个元素的复杂度 '''
# arr = [9,1,8,2,7,3,6,4,5]
# # O(1)操作：直接按索引取元素，不管列表多长，只做1次操作
# first = arr[0]
# print(first)  # 输出9

''' 二分查找：查找有序数列中某个数的复杂度 '''
# def binary_search(sorted_arr, target):
#     left = 0
#     right = len(sorted_arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if sorted_arr[mid] == target:
#             return True
#         elif sorted_arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False

# # 先把无序数列排序成有序：[1,2,3,4,5,6,7,8,9]
# sorted_arr = [1,2,3,4,5,6,7,8,9]
# # 找元素5，只需要log₂(9)≈3次操作
# print(binary_search(sorted_arr, 5))  # 输出True

''' 遍历查找：查找无序数列中某个数的复杂度 '''
# def linear_search(arr, target):
#     for num in arr:
#         if num == target:
#             return True
#     return False

# arr = [9,1,8,2,7,3,6,4,5]
# # 找元素5，需要遍历到第9个元素，9次操作
# print(linear_search(arr, 5))  # 输出True

''' 线性时间排序（计数排序）：适用于整数范围较小的情况，复杂度O(n) '''
# def counting_sort(arr):
#     min_val = min(arr)
#     max_val = max(arr)
#     # 计数数组，统计每个数出现的次数
#     count = [0] * (max_val - min_val + 1)
#     # 第一次遍历：统计次数（O(n)）
#     for num in arr:
#         count[num - min_val] += 1
#     # 第二次遍历：重建有序数组（O(n)）
#     sorted_arr = []
#     for i in range(len(count)):
#         sorted_arr.extend([i + min_val] * count[i])
#     return sorted_arr

# arr = [9,1,8,2,7,3,6,4,5]
# sorted_arr = counting_sort(arr)
# print(sorted_arr)  # 输出[1,2,3,4,5,6,7,8,9]

''' 归并排序：分治法，复杂度O(n log n) '''
def merge_sort(arr):
    # 递归终止：长度<=1，已经有序
    if len(arr) <= 1:
        return arr
    # 分：把数组分成两半
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 合：合并两个有序数组
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    # 合并两个有序数组，O(n)操作
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 把剩余元素加进去
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [9,1,8,2,7,3,6,4,5]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # 输出[1,2,3,4,5,6,7,8,9]

''' 冒泡排序：每次比较相邻元素，复杂度O(n²) '''
def bubble_sort(arr):
    n = len(arr)
    # 外层循环：n-1轮，每轮把最大的数冒泡到最后
    for i in range(n-1):
        # 内层循环：每轮比较n-1-i次
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                # 交换相邻元素
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [9,1,8,2,7,3,6,4,5]
# 用copy避免修改原数组
sorted_arr = bubble_sort(arr.copy())
print(sorted_arr)  # 输出[1,2,3,4,5,6,7,8,9]

'''
排序 = 代码要干的「正事」代码的任务只有一个：把你给的乱数 [9,1,8,2,7,3,6,4,5] 排成整齐的 [1,2,3,4,5,6,7,8,9]→ 这是代码的工作，代码从来不数数！
数数 = 我们人类干的「对比工作」我们要数清楚：每种排序方法，代码需要动手操作多少次→ 数完才知道：哪种方法最快、最省力
时间复杂度 = 我们数完数，总结的「快慢规律」我们把规律告诉代码，教它用「最快的手法」去排序
'''

