import json

# JSONファイルを読み込む
with open("campaigns.json", "r", encoding="utf-8") as file:
    campaigns_list = json.load(file)