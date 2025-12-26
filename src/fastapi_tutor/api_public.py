# 示例: Github API

import requests

response = requests.get("https://api.github.com/users/hordu-ma")
data = response.json()

print(data)
