import xml.etree.ElementTree as ET

# 1. 加载XML文件
tree = ET.parse('test.xml')
root = tree.getroot()

# 2. 定义命名空间映射（和XML里的定义对应）
namespaces = {
    'h': 'http://www.w3.org/TR/html4/',
    'f': 'http://example.com/furniture'
}

# 3. 解析HTML表格（h:table）
print("=== 解析HTML表格数据 ===")
html_table = root.find('h:table', namespaces)
for row in html_table.findall('h:tr', namespaces):
    name = row.find('h:td[1]', namespaces).text
    age = row.find('h:td[2]', namespaces).text
    print(f"姓名：{name}，年龄：{age}")

# 4. 解析家具桌子（f:table）
print("\n=== 解析家具桌子数据 ===")
furniture_table = root.find('f:table', namespaces)
material = furniture_table.find('f:material', namespaces).text
color = furniture_table.find('f:color', namespaces).text
size = furniture_table.find('f:size', namespaces).text
print(f"材质：{material}，颜色：{color}，尺寸：{size}")