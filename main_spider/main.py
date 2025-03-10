import os
import sys
import time
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 添加项目根目录

from tools import spider
from tools import analysis

current_path = os.path.dirname(__file__)
file_path = os.path.join( current_path, "../", "tools", "data", "rumor.csv")

def analysis_summary(summary_data,analysis_dir):
  summary_df = pd.DataFrame(summary_data)
  summary_path = os.path.join(analysis_dir, "analysis_summary.csv")
  summary_df.to_csv(summary_path, index=False, encoding='utf_8_sig')
  print(f"分析概览已保存至：{summary_path}")

def kewords_analysis(keywords_count,analysis_dir):
  # 保存关键词统计（带表头）
  keywords_df = keywords_count.reset_index()
  keywords_df.columns = ['关键词', '出现次数']
  keywords_path = os.path.join(analysis_dir, "keywords_analysis.csv")
  keywords_df.to_csv(keywords_path, index=False, encoding='utf_8_sig')
  print(f"关键词分析已保存至：{keywords_path}")
  

def source_analysis(source_counts,analysis_dir):
  # 保存来源分析（带表头）
  source_df = source_counts.reset_index()
  source_df.columns = ['来源机构', '出现次数']
  source_path = os.path.join(analysis_dir, "source_analysis.csv")
  source_df.to_csv(source_path, index=False, encoding='utf_8_sig')
  print(f"来源分析已保存至：{source_path}")

def analysis_main(data):
  # 数据保存
  df = pd.DataFrame(data)
  df['split_keywords'] = df['rumor_keywords'].str.split(',')

  # 分析处理
  keywords_count = df['split_keywords'].explode().value_counts()
  source_counts = df['rumor_quote'].value_counts()

  # 保存原始数据
  df.to_csv(file_path, index=False, encoding='utf_8_sig')

  # 新增保存路径处理
  analysis_dir = os.path.dirname(file_path)  # 获取data目录路径

  # 保存基础分析报告
  summary_data = {
      '统计项': ['总记录数', '标题非空数', '关键词非空数', '来源引用数', '图片URL数'],
      '数值': [
          len(df),
          df['rumor_title'].count(),
          df['rumor_keywords'].count(),
          df['rumor_quote'].count(),
          df['rumor_url'].count()
      ]
  }
  analysis_summary(summary_data,analysis_dir)
  # ----------
  kewords_analysis(keywords_count,analysis_dir)
  # ----------
  source_analysis(source_counts,analysis_dir)
  # ----------



if __name__ == '__main__':
  # 生成时间戳文件名防止重复
  timestamp = str(int(time.time()))

  # url = "https://www.piyao.org.cn/bq/ds_0615b39e6744461c8af75b06dd4f1c46.json"
  url = "https://www.piyao.org.cn/jrpy/ds_e0bb8399925745768458fc917f771895.json"
  spider.spider(timestamp,url)
  # data = analysis.analysis_rumor()
  # analysis_main(data)


  


  pass