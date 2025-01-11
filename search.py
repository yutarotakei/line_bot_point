from import_json import campaigns_list 


def search_campaign_by_name(keyword):
    """
    キーワードに基づいてキャンペーンを検索し、結果をポイントごとに整形して返す。
    """
    # 条件に一致するキャンペーンを抽出
    result = [
        [campaign[0], campaign[1], campaign[2]]  # ポイント名、キャンペーン名、リンクを抽出
        for campaign in campaigns_list
        if keyword in campaign[1]  # キャンペーン名にキーワードが含まれるかチェック
    ]

    # 結果がある場合
    if result:
        # ポイント名ごとに分類
        campaigns_by_point = {}
        for campaign in result:
            point_name = campaign[0]
            if point_name not in campaigns_by_point:
                campaigns_by_point[point_name] = []
            campaigns_by_point[point_name].append(campaign)

        # メッセージを整形
        formatted_results = []
        for point_name, campaigns in campaigns_by_point.items():

            formatted_results.append("\n")  # 改行を1つ追加
            formatted_results.append("\n")  # 改行を1つ追加
            formatted_results.append(f"- {point_name}-")
            formatted_results.extend(
                [f"『{campaign[1]}』\n{campaign[2]}" for campaign in campaigns]
            )

        return f"おっ、『{keyword}』に関連するキャンペーンを探しておるのか？ふむふむ……おおっ、こんなのが見つかったぞい！これは見逃せんぞい！\n\n" + "\n".join(formatted_results)
    else:
        return f"""……ん？残念ながらその名前ではキャンペーン情報は見つからんのう。ワシはポイントサイトや色んな会社の公式情報を参考にしておる。\n\n融通が利かなくて申し訳ないのじゃが正式名称じゃないとワシは認識できないのじゃ。ひらカナを変えたり、他のやり方で試せば出せるかもしれん。\n
ちなみに、自治体商品券を探すなら、末尾に『市・区・町・村』をつけてくれると助かるぞい。ワシも頑張って探してみるから、また声をかけてくれのう！"""
