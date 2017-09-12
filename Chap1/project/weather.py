#!/uer/bin/python
# -*- coding: utf-8 -*-

#以utf-8的编码模式打开txt文件
with open('/Users/zjiaqiao/Py101-004/Chap1/resource/weather_info.txt','r', encoding = 'utf-8') as f:
    data = f.readlines()

dict = {}
# 把每一行头尾的空字符串去掉，并转化为list，然后添加到字典
for line in data:
    dict[line.strip().split(',')[0]] = line.strip().split(',')[1]

history ={}

while True:
    print('请输入指令或您要查询的城市名')
    city = input('>')

    if city in dict.keys():
        print('%s的天气状况为: %s' % (city,dict[city]))
        history[city] = dict[city]
    elif city == 'help':
        print("""
- 输入城市名，获取该城市的天气情况；
- 输入help，获取帮助文档；
- 输入history，获取查询历史；
- 输入quit，退出天气查询系统。
""")
    elif city == 'history':
        print("历史查询记录:%s" % history)
    elif city == 'quit':
        print("历史查询记录:%s" % history)
        exit(0)
    else:
        print("抱歉，无法查询到%s的天气状况。" % city )
