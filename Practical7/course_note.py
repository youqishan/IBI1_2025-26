import re

'''
校验字符串格式 → 用 fullmatch()
只看开头是否符合 → 用 match()
找任意位置第一个匹配 → 用 search()
批量提取所有数据 → 用 findall()
替换文字 → 用 sub()
智能分割字符串 → 用 split()
'''

string = "From yuhao2.25@intl.zju.edu.cn Sat Jan 5 09:14:16 2008"

# 使用 fullmatch() 校验字符串格式，模拟邮件日志格式，包括 From，邮箱格式，日期时间
pattern = r'From\s+(\S+)@(\S+)\s+.*'
if re.fullmatch(pattern, string):
    print(pattern, "完全匹配")
'''
From：精确匹配开头的 From
\s+：匹配 1 个或多个空白字符（空格 / 制表符等）
(\S+)：第 1 个捕获组，提取邮箱用户名（yuhao2.25，非空白字符）
@：精确匹配 @ 符号
(\S+)：第 2 个捕获组，提取邮箱域名（intl.zju.edu.cn，非空白字符）
\s+：匹配邮箱后的空白字符
.*：匹配剩余所有字符（时间等内容）
'''


# 使用 match() 只看开头是否符合
match = re.match(pattern, string)
if match:
    print("字符串开头符合要求")
'''
作用：仅从字符串开头匹配，不要求匹配整个字符串。
结果：输出 字符串开头符合要求，因为原字符串以 From 开头，和模式开头一致
'''


# 使用 search() 找任意位置第一个匹配
search = re.search(pattern, string)
if search:  print("字符串中找到了匹配")
'''
作用：扫描整个字符串，找到第一个符合模式的片段（不限制位置）。
结果：输出 字符串中找到了匹配，因为整个字符串都符合模式。
和 match 的区别：如果模式不在开头，search 也能找到，match 会失败
'''


# 使用 findall() 批量提取所有数据
findall = re.findall(pattern, string)
if findall:
    print("提取到的数据:", findall)
'''
作用：返回所有捕获组的内容（模式里 () 包裹的部分）。
结果：输出 [('yuhao2.25', 'intl.zju.edu.cn')]，提取了邮箱的用户名和域名。
'''


# 使用 sub() 替换文字
replaced_string = re.sub(pattern, r'Email: \1@\2', string)
print("替换后的字符串:", replaced_string)
'''
作用：将匹配的部分替换为指定格式，\1 和 \2 分别引用第 1 和第 2 个捕获组。
结果：输出 替换后的字符串: Email: yuhao2.25@intl.zju.edu.cn
'''


# 使用 split() 智能分割字符串
split = re.split(r'\s+', string)
print("分割后的字符串列表:", split)
'''
作用：根据正则表达式分割字符串。
结果：输出 ['From', 'yuhao2.25@intl.zju.edu.cn', 'Sat', 'Jan', '5', '09:14:16', '2008']
'''

'''
r"" 里面只有 4 大类内容，所有正则都是这 4 类拼出来的：
普通字面量（写啥匹配啥）
元字符（万能匹配符）
锚点（定位置）
分组 / 捕获组（你要的「抓取组」）
'''

'''
普通字面量（最简单）
就是直接写的字母、数字、符号，完全原样匹配。
✅ 例子：r"From"、r"@"、r"R"、r"E"  
✅ 作用：写 A 就匹配 A，写 @ 就匹配 @
✅ 记忆：字面量 = 照抄匹配
'''

'''
元字符（万能匹配符）
特殊字符，具有特殊含义，可以匹配多种情况。
.  → 匹配任意单个字符（除了换行）
\d → 匹配任意数字（0-9）
\w → 匹配任意字母、数字或下划线（相当于 [a-zA-Z0-9_]）
\s → 匹配任意空白字符（空格、制表符等）
\S → 匹配任意非空白字符
\W → 匹配任意非字母、数字或下划线
*  → 匹配前一个元素零次或多次
+  → 匹配前一个元素一次或多次
?  → 匹配前一个元素零次或一次
{n} → 匹配前一个元素恰好 n 次
{n,} → 匹配前一个元素至少 n 次
{n,m} → 匹配前一个元素至少 n 次，至多 m 次
记忆：小写是本意，大写是反义；符号管数量
'''

'''
锚点（定位置）
^ → 匹配字符串开头  e.g. r"^From" 只能匹配以 From 开头的字符串
$ → 匹配字符串结尾  e.g. r"2008$" 只能匹配以 2008 结尾的字符串
\b → 匹配单词边界（单词与空格之间的位置）   e.g. r"\bFrom\b" 只能匹配独立的 From，不能匹配 Fromm 或 mFrom
\B → 匹配非单词边界 （单词内部的位置） e.g. r"\BFrom\B" 只能匹配 Fromm 或 mFrom，不能匹配独立的 From
记忆：^ 开头，$ 结尾，\b 定位单词边界
'''

'''
分组 / 捕获组（你要的「抓取组」）
() → 定义一个捕获组，提取匹配的内容     e.g. r"(\S+)@"
[] → 字符集 → 匹配方括号内的任一字符    e.g. r"[a-zA-Z0-9_]+"
| → 选择符 → 匹配符号两边的任一模式   e.g. r"cat|dog"
\1、\2、... → 引用前面定义的捕获组内容
记忆：() 定义组，\1 引用组
'''

'''
以后看到任何 r""，都按这个逻辑拆解：
正则公式 = 【锚点】 + 【元字符 / 字面量】 + 【捕获组】 + 【数量符】
口语化翻译：
「从哪里开始」+「匹配什么字符」+「把谁抓出来」+「匹配多少个」

例子 1：r'(\S+)\s+R'
(\S+)：捕获组，抓取连续非空白字符
\s+：空格
R：字面量
→ 翻译：抓取「空格 + R」前面的单词
例子 2：r'^(\S+)\s+E'
^：开头锚点
(\S+)：捕获组
\s+E：空格 + E
→ 翻译：从开头抓取「空格 + E」前面的内容
例子 3：邮箱 r'(\S+)@(\S+)'
两个捕获组，直接抓取用户名 + 域名
'''

# test.txt 位于：/Users/youqishan/Desktop/IBI1/其他

# 打开文件（只读模式）
file_handle = open("test.txt", "r")
# count = 0
# print("文件内容:", file_handle.read())  # 读取整个文件内容
# file_handle.seek(0)  # 将文件指针重置到文件开头
# # 逐行读取
# for line in file_handle:
#     print(line.strip())  # 打印每一行
#     count += 1
# print("总行数:", count)
# file_handle.close()  # 关闭文件（必须做！）

# file_handle = open("test.txt", "r")
# line1 = file_handle.readline()  # 读第一行
# line2 = file_handle.readline()  # 读第二行
# print(line1, line2)
# file_handle.close()

# 打开文件（覆盖模式）
file_handle = open("test.txt", "w")
file_handle.write("Lecture 7.2\n")  # 写字符串，换行符`\n`需手动加
file_handle.write("File Operation\n")
file_handle.close()  # 关闭文件（确保内容写入磁盘）

# 追加写入（不覆盖原有内容）
file_handle = open("test.txt", "a")
file_handle.write("Add new line\n")  # 在文件末尾加新行，原有内容保留
file_handle.close()

import re
with open("test.txt", "r") as file_handle:
    for line in file_handle:
        line = line.rstrip()
        # 筛选包含"From:"的行
        if re.search("From:", line):
            print(line)
        # 跳过不包含"@uct.ac.za"的行
        if "@uct.ac.za" not in line:
            continue
        print(line)

'''
学习使用 pandas
'''

import pandas as pd
# 从 xlsx 文件加载数据
data = pd.read_excel("HLFS_Raw_Data.xlsx")
# # 显示前 5 行数据
# print(data.head())
# # 显示前五列数据
# print(data.iloc[:, :5])

# 提取名为 How many days a week do you sleep at least 7 hours? 的列
sleep_data = data["How many days a week do you sleep at least 7 hours?"]
print(sleep_data)

df = pd.read_excel("HLFS_Raw_Data.xlsx")
print(df)  # 打印Excel表格
# 提取"Group"列数据
group = df["How many days a week do you sleep at least 7 hours?"].values
print(group)  # 打印提取的列数据