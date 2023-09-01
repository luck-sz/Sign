import requests

# API端点URL，替换为您的实际令牌
url = "https://apiaws.enseat-hanger.com/v1/checkin?token=YOUR_TOKEN_HERE"

# 发送GET请求
response = requests.get(url)

# 检查响应
if response.status_code == 200:
    print("签到成功！")
else:
    print(f"签到失败，响应码：{response.status_code}")
