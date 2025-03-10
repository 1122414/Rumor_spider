import os
import re
import time
import requests
import subprocess
from DrissionPage import *
# 获取当前路径
current_path = os.path.dirname(__file__)


def spider(timestamp,url):
  url = url
  heeader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
  }

  file_path = os.path.join(current_path, "data", timestamp)

  response = requests.get(url, headers=heeader)

  # 如果文件夹不存在,则创建
  if not os.path.exists(file_path):
    os.makedirs(file_path)

  with open(os.path.join(file_path, f"{timestamp}_rumor.json"), "wb") as f:
    f.write(response.content)

  # print(response)

