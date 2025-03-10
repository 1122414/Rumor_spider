import os
import sys
import time
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 添加项目根目录

from tools import spider
from tools import analysis
from tools import analysis_1

current_path = os.path.dirname(__file__)
file_path = os.path.join( current_path, "../", "tools", "data", "rumor.csv")

if __name__ == '__main__':
  # 生成时间戳文件名防止重复
  timestamp = str(int(time.time()))

  # url = "https://www.piyao.org.cn/bq/ds_0615b39e6744461c8af75b06dd4f1c46.json"
  # url = "https://www.piyao.org.cn/jrpy/ds_e0bb8399925745768458fc917f771895.json"
  # spider.spider(timestamp,url)
  data = analysis_1.analysis_rumor()
  analysis_1.analysis_main(data)

  pass