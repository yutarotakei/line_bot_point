from import_json import campaigns_list 


def search_local(user_message):
    # 入力に基づくキャンペーン検索
    result = [
        [campaign[0], campaign[1], campaign[2]]  # キャンペーン名、詳細、リンクを抽出
        for campaign in campaigns_list
        if user_message in campaign[1]
    ]
    
    # フォーマット結果
    if result:
        formatted_results = "\n".join(
            [
                f"\n・{campaign[0]}: {campaign[1]}\n{campaign[2]}"
                for campaign in result
            ]
        )
        return f"おっ、{user_message}ではこんなキャンペーンがあるようじゃぞ！これは活用せん手はないのう。詳細や条件はリンクからしっかり確認してくれい！：\n\n{formatted_results}"
    else:
        # 地域に関連するキャンペーンを検索（市、区、町、村を含む）
        excluded_keywords = ['楽天市場', '眼鏡市場', '都市電気', '都市ガス']
        related_campaigns = [
            [campaign[0], campaign[1], campaign[2]]
            for campaign in campaigns_list
            if any(keyword in campaign[1] for keyword in ['市', '区', '町', '村'])
            and all(excluded not in campaign[1] for excluded in excluded_keywords)
        ]
        if related_campaigns:
            formatted_related = "\n".join(
                [
                    f"\n\n{campaign[0]}: {campaign[1]}\n{campaign[2]}"
                    for campaign in related_campaigns
                ]
            )
            return f"おっ{user_message}について知りたいんじゃな？ちょっと待っとれ\n\n……ふむふむ、調べてみたが、今のところ自治体と提携したキャンペーンや商品券は見当たらんようじゃ。残念じゃのう。\n\nちなみに今実施中の自治体とコラボしたキャンペーンは下記じゃぞ！\n{formatted_related}"
        else:
            return f"おっ{user_message}について知りたいんじゃな？ちょっと待っとれ\n\n……ふむふむ、調べてみたが、今のところ自治体と提携したキャンペーンや商品券は見当たらんようじゃ。残念じゃのう。\nとはいえ、最近は大きな自治体を中心にこういったキャンペーンが増えてきとるから、定期的にチェックするのが吉じゃぞ！"

def search_gift():
    # 商品券に関するキャンペーン検索
    results = [campaign for campaign in campaigns_list if "商品券" in campaign[1]]
    
    if results:
        formatted_results = "\n".join(
            [f"\n\n{campaign[0]}: {campaign[1]}\n{campaign[2]}" for campaign in results]
        )
        return f"お、自治体商品券についてじゃな。調べてみたところ、今は下記のものが実施中じゃ{formatted_results}"
    else:
        return "お、自治体商品券についてじゃな。しかし、現在該当するキャンペーンは見つからなかったぞ。"
