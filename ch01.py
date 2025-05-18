import requests

url = "https://api.weatherapi.com/v1/current.json"
params = {
    "key": "58ba32798864465ba4d21954251805",  # 替换为控制台获取的密钥
    "q": "Guangzhou",
    "aqi": "no"  # 可选参数：关闭空气质量数据以减少响应体积
}

response = requests.get(url, params=params)
response.raise_for_status()  # 自动抛出 HTTP 错误
data = response.json()

print(f"城市：{data['location']['name']}")
print(f"温度：{data['current']['temp_c']} °C")
print(f"天气状况：{data['current']['condition']['text']}")