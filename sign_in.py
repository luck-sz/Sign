import requests

# API端点URL，替换为您的实际令牌
url = "https://apiaws.enseat-hanger.com/v1/checkin?token=eyJ1c2VyX2lkIjoxMzc4NTkzMywibGFzdGxvZ2luIjoxNjkyODA5MTA4fQ.9190117885606e43782e809272488270.fede309b321e279cc8e2dc027bdefd4e4c638bc44c807d51570243dd"

# 发送GET请求
response = requests.get(url)

# 检查响应
if response.status_code == 200:
    print("签到成功！")
else:
    print(f"签到失败，响应码：{response.status_code}")
