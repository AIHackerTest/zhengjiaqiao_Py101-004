# -*- conding:utf-8 -*-
import requests
history = []

def help():
    print("""
    - 输入城市名，获取该城市的天气情况；
    - 输入help，获取帮助文档；
    - 输入history，获取查询历史；
    - 输入c，切换到摄氏度
    - 输入f，切换到华氏度
    - 输入quit，退出天气查询系统。
    """)

def get_location():
    unit = 'c'
    while True:
        user_input = input('请输入指令(如：help)或您要查询的城市名（如：北京）>>').strip()
        if user_input == 'help':
            help()
        elif user_input == 'history':
            print('历史查询记录为: ')
            for i in history:
                print(i)
            print('\n')
        elif user_input == 'c':
            unit = 'c'
            print('已切换到摄氏度\n')
        elif user_input == 'f':
            unit = 'f'
            print('已切换到华氏度\n')
        elif user_input == 'quit':
            print('成功退出天气查询系统')
            exit(0)
        else:
            fetchweather(user_input, unit)

def fetchweather(location, unit):
    url = "https://api.seniverse.com/v3/weather/now.json"

    params = {
        "key": "6kdw2auoyzhisehb",
        "location": location,
        "language": "zh-Hans",
        "unit": unit
        }

    try:
        result = requests.get(url, params, timeout=20).json()
        #print(result)
        name = result['results'][0]['location']['name']
        temperature = result['results'][0]['now']['temperature']
        if unit == 'c':
            temperature_ed = temperature + '摄氏度'
        else:
            temperature_ed = temperature + '华氏度'
        weather_info = result['results'][0]['now']['text']
        time = result['results'][0]['last_update']
        time_ed = time[:10] + ' ' + time[11:19]

        forecast = '\n'+"-"*10+'%s天气查询结果' % name+"-"*10+'\n'+'天气状况为：%s' % weather_info+'\n'+'温度为：%s' % temperature_ed+'\n'+'最后更新时间：%s' % time_ed
        print(forecast+'\n')
        history.append(forecast)

    except:
        print("\n" + "抱歉，无法查询到%s的天气状况。" % location)


if __name__ == '__main__':
    get_location()
