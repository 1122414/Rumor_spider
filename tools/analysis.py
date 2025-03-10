import os
import json
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