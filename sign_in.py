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
    "token": "eyJ1c2VyX2lkIjoxMzc4NTkzMywibGFzdGxvZ2luIjoxNjkzNjE5MTAyfQ.07e56f26b777eb953d6a3510196bc384.f9defc11d22c59f6b01978aa90cc6b29b1f5059ad8da000254008ce8"
}

try:
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(response.content)
    else:
        print(f"签到失败，响应码：{response.status_code}")
except Exception as e:
    print(f"发生异常：{e}")
