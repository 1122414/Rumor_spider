﻿import os
import json
import pandas as pd
current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, "data", "rumor.json")
def analysis_rumor():
  with open(file_path, "r", encoding="utf-8-sig") as f:
    data = json.load(f)
  
  rumor_list = []
  
  for rumor in data['datasource']:
    single_rumor = {}
    single_rumor["rumor_title"] = rumor["title"]
    single_rumor["rumor_keywords"] = rumor["keywords"]
    single_rumor["rumor_quote"] = rumor["quote"]
    single_rumor["rumor_url"] = rumor.get("imageUrl", "")
    single_rumor["rumor_sourceText"] = rumor["sourceText"]
    rumor_list.append(single_rumor)
  return rumor_list


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

def analysis_main(timestamp,data):
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