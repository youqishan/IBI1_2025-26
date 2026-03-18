'''
This is my note during Monday's class
So there might have some Chinese characteristics.
It's just for me to review the course and the code.
'''


# import matplotlib.pyplot as plt
# import numpy as np
# # plt.rcParams['font.sans-serif'] = ['PingFang SC'] # 尝试解决font显示问题
# # plt.rcParams['axes.unicode_minus'] = False        # 但是我失败了

'''

# 1. 散点图：展示两个变量的关系
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y, marker='8', color='red', label='random dot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('scatter diagram sample')
plt.legend()
plt.show()

'''

# .	点（极小）	s	正方形	
# ,	像素点	D	菱形	
# ^	上三角	*	星形	
# v	下三角	+	加号	
# <	左三角	x	叉号	
# >	右三角	p	五边形	
# H	六边形	8	八边形	
# _	横线

"""
# 2. 柱状图：带误差棒，对比不同组
N = 5
scores = (20, 35, 30, 35, 27)
std = (2, 3, 4, 1, 2)
ind = np.arange(N)
width = 0.35
plt.bar(ind, scores, width, yerr=std, color='lightblue')
plt.ylabel('value')
plt.xlabel('group')
plt.title('Bar chart with error bars')
plt.yticks(np.arange(0, 81, 10))
plt.show()

"""

# 
'''
# 3. 饼图：展示各部分占比
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0) # 突出显示Hogs
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal') # 标准圆形
plt.title('pie graph')
plt.show()

'''
#
'''
# 4. 箱线图：展示数据分布
n = 20
score = np.random.uniform(0, 100, n)
plt.boxplot(score, vert=True, patch_artist=True, boxprops={'facecolor': 'silver'})
plt.ylabel('value')
plt.title('box plot')
plt.show()

'''




# 1. 定义与索引
L = [2, 'a', 4, 1]
print(len(L))   # 4
print(L[0])     # 2
print(L[2]+1)   # 5
i = 2
print(L[i-1])   # 'a'

# 2. 修改元素
L = [2,1,3]
L[1] = 5
print(L)        # [2,5,3]

# 3. 增加元素
L.append(5)     # 末尾加一个：[2,5,3,5]
L.extend([6,7]) # 末尾加多个：[2,5,3,5,6,7]
L2 = L + [8,9]  # 拼接生成新列表，原L不变
print(L, L2)    # 原L，还有原L的基础上多8和9

# 4. 删除元素
L = [2,1,3,6,3,7,8]
L.remove(2)     # 删除第一个2：[1,3,6,3,7,8]
L.remove(3)     # 删除第一个3：[1,6,3,7,8]
del(L[1])       # 删除索引1的元素：[1,3,7,8]
L.pop()         # 删除最后一个元素：[1,3,7]
print(L)

# 5. 排序与反转
L = [9,6,0,3]
print(sorted(L))# 生成升序新列表：[0,3,6,9]，原L不变
L.sort()        # 原列表升序：[0,3,6,9]
L.reverse()     # 原列表反转：[9,6,3,0]
print(L)

# 6. 遍历列表（计算总和，推荐直接遍历）
total = 0
for num in L:
    total += num
print(f"列表总和：{total}")

# 7. 避坑：遍历中修改列表（先复制）
L1 = [1,2,3,4]
L2 = [1,2,5,6]
L1_copy = L1[:]
for e in L1_copy:
    if e in L2:
        L1.remove(e)
print(L1) # [3,4]（正确删除）






import numpy as np
# 1. 定义与索引
arr = np.array([1,2,3,4])
print(arr[1])   # 2
print(arr[3])   # 4

# 2. 向量化运算（核心优势）
a = np.array([1,2])
b = np.array([3,4])
print(a + b)    # [4,6]
print(a * 2)    # [2,4]
print(b **2)   # [9,16]
print(a * b)    # [3,8]

# 3. 生物信息学案例：批量计算基因表达量标准化
expr = np.array([1.2, 2.5, 3.1, 0.8])
std_expr = (expr - np.mean(expr)) / np.std(expr) # 标准化
print(f"原始表达量：{expr}")
print(f"标准化表达量：{std_expr}")






# 1. 定义与取值（生物信息学案例：基因名-基因长度）
genes = {'Shh':9410, 'NBAS':3944141, 'Dlx5':4442, 'PTEN':105338}
print(genes['Shh']) # 9410
# print(genes['TP53']) # 键不存在，报错

# 2. 增加键值对
genes['CTCF'] = 76779
print(genes)

# 3. 删除键值对
del(genes['Dlx5'])
print(genes)

# 4. 判断键是否存在
print('NBAS' in genes) # True
print('TP53' in genes) # False

# 5. 遍历字典（键/值/键值对）
# 遍历键
for gene in genes:
    print(f"基因名：{gene}")
# 遍历键值对（推荐）
for gene, length in genes.items():
    print(f"基因{gene}的长度为：{length}")

# 6. 生物信息学案例：样本名-表达量
sample_expr = {'Sample1':2.3, 'Sample2':1.8, 'Sample3':4.5}
# 筛选表达量>2的样本
for sample, expr in sample_expr.items():
    if expr > 2:
        print(f"高表达样本：{sample}，表达量：{expr}")



fruits = {'apple', 'banana', 'cherry'}
for fruit in fruits:
    print(fruit)

person = {'name': 'youqishan', "age": 19}
print(person['name'])
print(person['age'])
person['age'] = 21
person['city'] = 'hangzhou'
print(person)

# 选中代码后，用 shift + enter 进行局部编译
product = {'itemid': 1234, 'name': 'youqishan', 'colour': 'white'}
print(product['itemid'])
product['size'] = "small"
print(product)

del product['size']
product['size'] = ['small', 'medium', 'large']
print(product)

print(product['size'][2])  # large



products = [
    {'itemid': '1001', 'name': 'tshirt', 'size': ['small', 'medium', 'large']},
    {'itemid': '1001', 'name': 'tshirt', 'size': []}  
]

# 修正变量名拼写
print(products[0]['itemid'], products[0]['name'], products[0]['size'][0])