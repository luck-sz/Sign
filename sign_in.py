import requests
import time

url = "https://apiaws.enseat-hanger.com/v1/checkin"

# 获取当前时间戳
current_time = int(time.time())

# 请求头
headers = {
    "lang": "cn",
    "versionid": "com.palipali",
    "version": "2.6.0",
    "platform": "Android",
    "time": str(current_time),  # 将时间戳转换为字符串
    "userid": "cfNkA8SBWn03v1fSh",
    "hash": "8b34afc712737050b14d1a30ad4f95b0",
    "usertype": "5352cfed7cd8e567ffefc0e38e36ef2e",
    "img": "https://encimgf.beijingjiaoyou.net",
    "User-Agent": "okhttp/4.11.0"
}

# 请求参数
params = {
    "token": "eyJ1c2VyX2lkIjoxMzc4NTkzMywibGFzdGxvZ2luIjoxNjk0MTcwMDk2fQ.06a3a832968d4de26d42e16920d5df23.2f02926da9b5b0782c149779d580f5c3d7cb377c390f8c9e322d03a9"
}

try:
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(response.content)
    else:
        print(f"签到失败，响应码：{response.status_code}")
except Exception as e:
    print(f"发生异常：{e}")
